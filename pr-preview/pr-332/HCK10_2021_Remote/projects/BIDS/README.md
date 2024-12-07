[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB-DANDI-BIDS integration

## Key Investigators

<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->
* Ben Dichter (LBNL/CatalystNeuro/Stanford)
* Julia Sprenger (INT, CNRS, Marseille, France)
* Sylvain Takerkart (INT, CNRS, Marseille, France)
* Jeremy Garcia (INT, CNRS, Marseille, France)
* Saksham Sharda (CatalystNeuro, ?)
* (...feel free to add yourself)

## Project Description

<!-- Add a short paragraph describing the project. -->
With the recently proposed standard for the organization of data and metadata obtained with animal electrophysiology (see the [BIDS extension proposal, BEP32](http://bit.ly/BIDS-animal-ephys)), we here aim at maximizing the integration and inter-operability between the NWB, DANDI and BIDS ecosystems. A dedicated breakout session is scheduled to present this BIDS-animal-ephys to the audience and to discuss all this with all interested parties! Come join us, it's on Wednesday March 31 at 9am PDT, in Room1).

Also, this BIDS extension proposal is actively looking for user feedback! So do not hesitate to go through the document and comment on it (don't be shy, add whatever you think, the mode comments from the community the wider the consensus at the end)

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->
Here are our main objectives:
* Create an example NWB dataset following the BIDS-animal-ephys standard.
* Release a small package for extracting the necessary data from NWB files and creating the BIDS-ephys structure.
* Validation of file structure. I think I recall we already have a draft for this.
* Discuss with DANDI, which has created its own file structure, and see if we can find compromises between the formats to bring them more in line with each other.

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->
Three practical items are on the agenda to start with at the beginning of this hackathon:
* homogeneize directory validation structure in the existing tools (Saksham, Jeremy, Julia, ?)
* finalize a BIDS-compliant NWB dataset and integrate it in the BIDS extension proposal (Ben, Sylvain, ?)
* discuss the metadata consistency between BIDS, DANDI and NWB to progress towards conversion/integration tools (Julia, Ben, a DANDI guru?)

The first two should be easy, the third is fairly open... After completing the first two, we'll see alltogether on how to move forward!

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->
* discuss the inter-operability and consistency with other data modalities that live at the intersection of BIDS, DANDI & NWB (e.g optical physiology & the BIDS extension proposal dedicated to microscopy, BEP31)

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->
* the [BIDS-animal-ephys extension proposal](http://bit.ly/BIDS-animal-ephys)
* the corresponding validation tool, for now called [AnDOChecker](https://github.com/INT-NIT/AnDO)
* the draft of a BIDS-compliant NWB [dataset](https://drive.google.com/drive/u/1/folders/1-5HgytYZQLkXgm3-R9kpZj-EhEqHs_2f)
* the first version of a conversion tool [from NWB to BIDS](https://github.com/catalystneuro/BIDS_ephys/blob/master/BIDS_ext.py)
* the [DANDI CLI](https://www.dandiarchive.org/handbook/10_using_dandi/#uploading-a-dandiset), that include tools to organize NWB files for DANDI

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
* [BIDS](https://bids.neuroimaging.io/get_involved.html)
* [NWB](https://www.nwb.org/)
* [DANDI](http://www.dandiarchive.org)

