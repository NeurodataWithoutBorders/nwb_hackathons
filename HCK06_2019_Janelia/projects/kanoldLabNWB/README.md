[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Integrate Thorlabs 2p calcium data into NWB

## Key Investigators

- Zac Bowen (UMD)
- Kelson Shilling-Scrivo (UMD/UMSOM)
- PI: Patrick Kanold (UMD)
- PI: Wolfgang Losert (UMD)

## Project Description

<!-- Add a short paragraph describing the project. -->
Our lab uses 2-photon calcium imaging to study auditory cortex. We run various types of experiments with variable metadata. We wish to convert 2-photon calcium imaging data into the NWB format in order to have a generalizable output from the Thorlabs scope.

## Objectives

- Objective A. Integrate common Thorlabs 2p raw data and relevant metadata into the NWB format.
- Objective B. Integrate alternative 2p data (volumetric, behavioral) into NWB format.
- Objective C. Carry raw data through subsequent data processing steps

## Approach and Plan

1. Get familiar with NWB format (Matlab) and assess whether python will need to be used
2. Work towards integrating as much data as possible into the NWB format (data with variable metadata and file formats) with the intention of training other lab members to use the format.
3. If time, assess NWB usage in further downstream analysis code.

## Progress and Next Steps

- Went through the two-photon tutorial just to familiarize with NWB storage and output.
- Started writing a script to store some sample 2-photon data in NWB
  - Stored raw data, registered data, mouse/subject data, experimental setup data, ROI masks
  - Formatted the above for volumetric data
    - Each plane of the volume is parsed seperately and saved as a separate imaging series
    - Same script will work for both volumetric and planar data
- Working towards storing processed data (extracted DFF traces)
- Still need further work towards storing behavioral data and pupil data
- Need to generalize script for usage by other lab members
  - Will likely need separate versions for converting old data versus storing new data as it is initially processed

## Materials

- Analysis code (MATLAB) and relevant sample data will be brought to the workshop.
- Sample data may include:
  - Raw ThorImage 2-photon data of a region of mouse auditory cortex responding to tonal stimuli
  - Similar data with a behavioral task and corresponding behaviorally relevant metadata
  - Volumetric 2p data from a similar tone presentation experiment

## Background and References

See www.kanold.org for relevant information on projects.



