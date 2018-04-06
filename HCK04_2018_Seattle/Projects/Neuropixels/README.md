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


## Progress and Next Steps

- Implemented generic unit metrics group (for storing snr/peak amplitudes) in core. See [pr #435](https://github.com/NeurodataWithoutBorders/pynwb/pull/435)
- Identified requirement to associate mean/std waveforms and electrode table regions with UnitTimes in core. See [issue #431](https://github.com/NeurodataWithoutBorders/pynwb/issues/431)


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

