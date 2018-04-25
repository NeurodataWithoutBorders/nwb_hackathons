[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Conversion of Pesaran lab electrophysiology data to the NWB:N format

## Key Investigators

- Kevin Brown (NYU)
- Bijan Pesaran (NYU)

## Project Description

The goal of this project is to convert local field potential and spike time data from the Pesaran Lab to the NWB format. This data includes behavioral data from awake, behaving Rhesus Macaques. This data is typically analyzed by aligning spike times or local field potential data to behavioral events of interest, such as the initiation of a saccade. Therefore, it would be useful to have a clean mechanism for associating data from combinations of arbitrary behavioral conditions (e.g. a saccade to the left during an instructed delay task two-alternative forced choice task), user-defined data conditions (e.g. spike time data from cells tuned to saccade direction from electrodes in the lateral intraparietal sulcus) at user-specified events (e.g. the beginnning of an optogenetic stimulation sequence). As our lab continues to extend recording modalities (e.g. to 2-photon calcium imaging), it would also be useful to have the ability to seamlessly integrate new data formats and types. 

Our lab has previously developed in house solutions for working with the above data in Matlab. Here we hope to allow seamless import and export to NWB using the available APIs. 

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Objective A. Convert Pesaran lab single-unit spike time electrophysiology data into the NWB:N file format
1. Objective B. Convert Pesaran lab local field potential data into NWB:N file format
1. Objective C. Create tools for filtering and aligning data to user-specified epochs


## Approach and Plan

We will focus on a single previously published experiment consisting of data from a working memory task in Rhesus Macaques to develop and test the implementation. 

1. Load spike times from a single aribtrary unit into the NWB:N format, test event-locked responses from the NWB:N format against in-house 
1. Load spike times from multiple single units into NWB:N format
1. Load LFP data from a single electrode into NWB:N format
1. Load LFP data from multiple simultaneously recorded electrodes into NWB:N format
1. Align above time series data to a specific epoch and behavioral condition of interest. 

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

Published description of data: http://www.pnas.org/content/112/35/11084


<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
