[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Work on integrating lab ECoG, behavioral, and imaging data using PyNWB

## Key Investigators

<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->

- Jessie R. Liu (Chang Lab, UCSF)

## Project Description

<!-- Add a short paragraph describing the project. -->

The Chang Lab records from a TDT acquisition system and has an in-house preprocessing pipeline for converting the raw TDT files into raw and preprocessed HTK files. The goal is to update this pipeline to be completely in Python and to utilize the NWB format.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->

* Have experience integrating the most common types of lab data (TDT/htk, behavioral logs, imaging) into .nwb files
* Be able to help lab members convert their data/be familiar with existing efforts to convert lab data to NWB format

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

- Code has been/is currently being developed to help piece together a complete pipeline (Matlab script for TDT tanks to NWB, the preprocessing pipeline in Python that can read NWB files, visualization GUI that can read in NWB files)
- Become familiar with each of these pieces
- Make sure the parts all work together
- Utilize an example TDT block to go through the entire process

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

- TDT recently released a Python package to read in data from their raw files
  - Converted Matlab script to Python to go from TDT tanks to NWB files with the raw data in an ElectricalSeries
  - Utilize NWB ECoG extension to add subject's cortical surfaces information.
- Edit Python preprocessing pipeline to save the frequency decomposition of the raw data into a DecompositionSeries
- Used visualization GUI to read in NWB files with the raw data
- Verified that each generated file was able to be used by the next step
- Next steps:
  - Continue working with others to test/expand the visualization GUI
    - Display high gamma data
    - Visualize ERPs aligned to a stimulus onset
  - Work with lab members to introduce them to the NWB format and get them familiar with reading and writing to these files

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

- The TDT package: https://pypi.org/project/tdt/
