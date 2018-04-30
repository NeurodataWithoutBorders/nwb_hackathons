[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Converting e-phys/behavioral data into NWB:N data format (Kepecs lab)

## Key Investigators

<!-- - Investigator 1 (Affiliation)-->
Michael Wulf (Cold Spring Harbor Laboratory)
<!-- - Investigator 2 (Affiliation)-->
Torben Ott (Cold Spring Harbor Laboratory)
<!-- - Investigator 3 (Affiliation)-->
Adam Kepecs (Cold Spring Harbor Laboratory)

## Project Description

<!-- Add a short paragraph describing the project. -->
This project aims to convert electrophysiological, imaging and behavioral data into the nwb data format. Data was obtained from different projects in Adam Kepecs' lab at CSHL.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

<!-- 1. Objective A. Describe it in 1-2 sentences.-->
1. Converting electrophysiological data obtained from extracellular recordings as well as photometry data into the nwb format. Consider different cases for raw data, extracted events, and clustered spike times.
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
2. Converting behavioral data into the nwb format with timing aligned to neural data. Define and describe different behavioral events. Behavioral data was obtained with Bpod.

<!-- 1. ...-->

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->
We made progress converting voltage timeseries and spike events intwo NWB:B. For our trial-based behavioral data, there seems to be no appropriate neurodata type available at the moment. We discussed with Andrew that there could be a table-like neurodata type for organizing trial data, such as categories, doubles and logicals. And additional Trial neurodata type could be used to specify in particular the start times or epochs of each trial.

More generally, our trials are defined as a sequence of states, i.e. could be described using state machines, as Kris pointed out.

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References
Disscusion at 
https://github.com/NeurodataWithoutBorders/nwb-schema/issues/152
<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
