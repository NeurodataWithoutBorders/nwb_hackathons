Back to [Projects List](../../README.md#ProjectsList)

# NWB for Neuropixels Experiments

## Key Investigators

- Josh Siegle (Allen Institute) @jsiegle
- Xiaoxuan Jia (Allen Institute) @jiaxx
- Nile Graddis (Allen Institute) @nilegraddis
- Tom Davidson (UCSF) @tjd2002
- Dan Millman (Allen Institute) @everythingevolves

# Project Description

We will represent high-density exctracellular electrophysiology (ecephys) data in NWB.

## Objective

1. Flexible representation of spike-sorting outputs
1. Build analogous functionality for Ophys data (DM).

## Approach and Plan

1. Identify and obtain a pool of raw datasets.
1. Write these datasets to NWB files (and read them back!).
1. Ensure that common features of these datasets are supported by the core 
NWB namespace or an extension.
1. Document the process of writing ecephys data to NWB.

## Progress

- Implemented generic unit metrics group (for storing snr/peak amplitudes) in core. See [pr #435](https://github.com/NeurodataWithoutBorders/pynwb/pull/435)
- Packaged kilosort/phy outputs with pynwb. See [notebook](notebooks/Packaging%20Kilosort%20+%20phy%20outputs%20using%20pynwb.ipynb)

## Next Steps

- We need to associate mean/std waveforms and electrode table regions with UnitTimes in core. See [issue #431](https://github.com/NeurodataWithoutBorders/pynwb/issues/431)
- Create a tutorial for packaging Kilosort/phy outputs with pynwb

## Functionality Table
A table of things that we want to write to NWB files.  Please fill in/edit entries! Columns are:
- functionality: short description
- tools supported: if the functionality is kilosort-specific, for instance
- PyNWB class: the PyNWB class(es) that currently supports this feature (or the closest match).
- notes: additional information.

|**functionality** | **tools supported** | **PyNWB class** | **notes** |
|:---:|:---:|:---:|:---:|
| Sorted units | all | ~~ecephys.Clustering~~ misc.UnitTimes | NB: UnitTimes was recently refactored ([pynwb pr #382](https://github.com/NeurodataWithoutBorders/pynwb/pull/382)). Doc fixes outstanding ([nwb-schema issue #117](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/127)) |
| Event tiimes | all | ~~ecephys.Clustering~~ misc.UnitTimes  |  |
| Unitwise metrics (peak amplitude, snr, classifications)  | all | ~~ecephys.Clustering~~ [pr #435](https://github.com/NeurodataWithoutBorders/pynwb/pull/435) | Created a new UnitMetrics class to handle unitwise metrics generically |
| Eventwise metrics (amplitude, PCs) | all | ecephys.FeatureExtraction (?) | These are likely to be lab specific. A solution based on MultiContainerInterface seems sensible |
| Unit waveforms | all | ecephys.ClusterWaveforms | Currently, it's not clear how to relate waveforms to unit IDs. [issue #431](https://github.com/NeurodataWithoutBorders/pynwb/issues/431) |
| LFP | all | ecephys.LFP ecephys.ElectricalSeries | |
| Current Source Density | all | ecephys.ElectricalSeries (?) | not sure if the dimensionality works. Should attach to LFP? |

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Forum: https://github.com/orgs/NeurodataWithoutBorders/teams/neuropixels/discussions
- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data

