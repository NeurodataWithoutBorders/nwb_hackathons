[:rewind: Back to the projects list](../../README.md#ProjectsList)

# Conversion of Adesnik lab calcium imaging data to the NWB:N format

## Key Investigators

Evan Lyall (Evan Lyall, UC Berkeley)


## Project Description

The goal of this project is to convert the whole-cell electrophysiology data from the Sabatini lab to the NWB format.
This data includes voltage-clamp and current-clamp recordings from neurons in acute brain slices. This data is typically analyzed
for the presence or absence of synaptic responses or changes in membrane potential. However, we often extract other features such
as response amplitude, latency, onset and offset kinetics, frequency of synaptic events or action potentials, and variability of responses 
in repeated trials. Therefore, a standard toolset to analyze this data in the NWB data format would also be useful. Finally, we often
record electrophysiology data in tandem with 2-photon imaging, and would like to be able to incorporate imaging data into the NWB:N file format.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Objective A. Develop understanding of NWB:N format for multi-plane calcium imaging data 
1. Objective B. Save one Adesnik lab calcium imaging experiment into the NWB:N file format
1. Objective C. Build out basic analysis notebook
1. Objective D. Cleanup conversion script to convert all Adesnik lab data to NWB:N format

## Approach and Plan

1. Prior to the hackathon: read through NWB:N documentation and prepare conda environment
1. Convert a single movie to NWB:N format including all experiment metadata
1. Write analysis notebook that loads in NWB:N data and interactively plots different views of the data
1. Polish conversion script to generalize to all Scanbox data in the lab

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
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

