[:rewind: Back to the projects list](../../README.md#ProjectsList)

# Stimulus representation and parametrization in NWB

## Key Investigators

* Pamela Baker
* Shreejoy Tripathy
* Lydia Ng


## Project Description

The problem: labs performing icephys are often delivering the same (or
very similar) types of stimuli (e.g., long steps, ramps, chirps,
etc). Despite the stereotyped nature of these stimuli, the NWB schema 
currently does not support a standardized stimulus representation,
leaving it up to the user to determine how to describe the stimulus
protocol and what stimulus metadata to include. This lack of standard
representation leads to difficulty in identifying similar protocols
across datasets and development of shared analysis scripts for
quantitative feature extraction.

In addition, there is often considerable redundancy in the stimulus
set that defines a single experimental protocol because the
stimuli typically differ by only a single parameter (e.g. amplitude,
latency, frequency) that is varied over some range of pre-selected
values to generate a tuning curve or compute a metric. These variable
parameters should be made explicit in the stimulus representation.
Parametrization also allows stimuli to be represented compactly, and
is practically a necessity for more complex types that can not be
represented as 1D time series. 

This work applies not only to patch clamp experiments but will also
be directly applicable to other 1D time-varying stimulus types,
including extracellular electrical stimulation and optogenetic
stimulation protocols.  


## Objectives

1.  Define a canonical set of 1D stimulus waveforms typically used in
  IC ephys experiments, and the parameters needed to describe each
  stimulus type (minimum to specify). 

2.  Develop a representation in NWB that supports parametrized
    stimulus definition and exposes variable parameters for
    search/revealing experimental design.

3.  Determine the minimum set of stimulus metadata
  that should be defined at each level of the experimental protocol
  (sweep/sequence/stimset/condition/etc) for comprehensive
  experimental descriptions.
 
4.  Design desired visualizations for stimuli and stimulus protocols
    with widgets.


## Approach and Plan

* For 1-D waveform types we already have e.g. the WaveformBuilder in
  MIES that defines a base set of stimulus types, with associated
  parameters, as a starting point. It appears that the Channelpedia
  stimuli can be constructed from the same set of elements as well. 

* Stimulus representation also dovetails into the issue of overall
  experimental protocol representation, so we will also end up touching
  on issues that relate to provenance. I would like to discuss some ideas
  for how stimulus parameterization and metadata representation
  (objectives 3 and 4) could be integrated with the IC ephys
  hierarchical tables extension. 


## Progress and Next Steps

<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->


## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->


## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

* Luke Campagnola had a previous Hackathon project that made a good start
  on some of these issues, specifically the issue of stimulus
  atomization/composition (see [here:] 
  (https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK04_2018_Seattle/Projects/StimulusMetadata)).

