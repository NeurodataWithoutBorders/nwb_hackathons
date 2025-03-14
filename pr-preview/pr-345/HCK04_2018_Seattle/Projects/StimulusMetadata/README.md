Back to [Projects List](../../README.md#ProjectsList)

# Stimulus Metadata

## Key Investigators

- Luke Campagnola (Allen Institute)


# Project Description

Schema extension to allow flexible description of stimulus protocols, with a focus on being able to compose the description from multiple independent elements. 

**Main discussion:** https://github.com/NeurodataWithoutBorders/nwb-schema/issues/131


## Objective

1. Objective A. Develop a schema for describing ephys stimuli (pulses, pulse trains, ramps, etc.) where each sweep may contain multiple stimuli combined together. The important part here is to allow descriptions for each type of stimulus to be composed together without creating a new class for each combination.
2. Objective B. Extend / generalize this work (if possible) to describe stimuli in other domains (photostimulation, sensory stimuli, etc.)

## Approach

1. Add a base class called `StimulusComponent` with `name` and `description` attributes.
2. Add a subgroup called `stimulus_components` to `CurrentClampStimulusSeries` and `VoltageClampStimulusSeries` that can contain any number of `StimulusComponent` subgroups.
3. Create a library of `StimulusComponent` subclasses, each of which describes different aspects of the stimulus that can be summed together to generate the final waveform:
```
    square_pulse
        start_time
        duration
        amplitude
    pulse_train
        start_time
        duration
        n_pulses
        pulse_duration
        interpulse_interval
    ramp
        start_time
        duration
        slope
        initial_amplitude
    white_noise
        start_time
        duration
        amplitude
        random_seed
    chirp
        start_time
        duration
        amplitude
        initial_frequency
        dfdt
    sine_wave
        start_time
        duration
        amplitude
        frequency
        initial_phase
```

As an example, a common stimulus encountered in multipatch experiments might be a current injection of several seconds containing:
* A small square "test pulse" near the beginning 
* A 2 second delay, followed by a train of 8 larger, regularly-spaced pulses 
* A 250 ms delay, followed by a similar 4-pulse train
From the experimenter's perspective, the most important features here are the frequency of pulses in the pulse trains and the delay period between the two pulse trains. We would like to be able to read out these parameters without parsing the stimulus waveform itself.

This stimulus could be described by combining some very common primitives--a square pulse and two pulse trains:
```
CurrentClampStimulusSeries
    stimulus_components
        SquarePulseStimulusComponent
            name: "test pulse"
            description: "A small hyperpolarizing pulse to measure the input resistance of the cell"
            start_time: 0.1
            duration: 0.03
            amplitude: -50e-12
        PulseTrainStimulusComponent
            name: "induction train"
            description: "A train of 8 pulses to evoke action potentials and induce short term plasticity"
            start_time: 2.0
            n_pulses: 8
            interpulse_interval: 0.02
            pulse_duration: 2e-3
            amplitude: 1.6e-9
        PulseTrainStimulusComponent
            name: "recovery train"
            description: "A train of 4 pulses to evoke action potentials and test recovery from short term plasticity"
            start_time: 2.41
            n_pulses: 4
            interpulse_interval: 0.02
            pulse_duration: 2e-3
            amplitude: 1.6e-9
```
Each of the components listed above specifies some part of the total waveform, and we should be able to reconstruct the waveform just by adding these together. In this way, a complex stimulus is built up from smaller components and annotated such that the important criteria (in this case, the timing of pulses) can be easily extracted without parsing the waveform.

For this particular example, it might even make sense for the experimenter to define a custom `StimulusComponent` describing the combination of all 12 pulses:
```
CurrentClampStimulusSeries
    stimulus_components
        SquarePulseStimulusComponent
            name: "test pulse"
            description: "A small hyperpolarizing pulse to measure the input resistance of the cell"
            start_time: 0.1
            duration: 0.03
            amplitude: -50e-12
        STPStimulusComponent    # defined in a custom extension
            name: "stp test"
            description: "A train of 12 pulses intended to induce short term plasticity and then test recovery."
            start_time: 2.0
            n_induction_pulses: 8
            n_recovery_pulses: 4
            pulse_frequency: 50
            recovery_delay: 0.25
            pulse_duration: 2e-3
            amplitude: 1.6e-9
```


## Progress

While attempting to implement the solution above, it became clear that the kind of composition we wanted was a much more general problem that should be solved at a lower level first. Progress on #131 is halted until those issues are worked out.
