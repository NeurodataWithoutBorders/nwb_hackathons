[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Convert Ephys data to NWB format to be distributed with publication.

## Key Investigators

- Laurel Keyes (Salk Institute of Biological Studies)

## Project Description

I am converting the electrophysioloy and behavioral data into NWB formats for a paper that will soon be published.
In this experiment, two mice competed for a reward.  Each mouse was fitted with a headset to monitor neural activity.  While we have complete ephys data for each subject, each competing pair has a single video containing both animals.  Their positions are extracted from the video via an automated tracking software called AlphaTracker. I want to identify which animal is which in the video so their position information is loaded into the correct nwb structure.


## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. (Objective A) Understand how to convert epys data to nwb format and put the data into that format.
1. (Objective B) Determine if any special extensions are required to get the data into the correct form and figure out how to do so.
1. (Objective C) Understand how nwb formats can fit into the larger workflow of the Tyelab.
1. (Objective D) Gain a greater familiarity with nwb and see how to add it to our existing processing pipelines.

## Approach and Plan

1. I plan to convert the data for a single subject all the way to the end, then work on automating the process for the remaining subjects.  However, the naming convention was not standardized when the data was collected, so this could prove difficult.

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

- [] I need to convert the raw data collected by SpikeGadgets into nwb format.
  - [] I am investigating some code by Frank Loren's lab that may do this.
- [] Convert the video data and extracted positions of subjects.
- [] I need to add links between the competitors so the files can be joined

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

Data is described in here (DOI: https://doi.org/10.21203/rs.3.rs-94115/v1)
<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

