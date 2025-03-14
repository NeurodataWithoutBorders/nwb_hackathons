[:rewind: Back to the projects list](../../README.md#ProjectsList)

# Conversion of multimodal data between Losonczy Lab and NWB:N formats

## Key Investigators

Sebi Rolotti (Losonczy Lab, Columbia University)

## Project Description

Our lab collects 2-photon imaging and extracellular electrophysiological data in awake behaving mice.
Our overall goal is to increase the interoperability of our data structures and formats with those of NWB.
We already have fairly well developed repositories for working with our data, including a public package for sequential imaging data (SIMA) as well as in-house lab analysis bundle (LAB) for associating and analyzing these various data formats.
We therefore hope to allow for seamless import from and export to NWB using the APIs for these repos.

## Objectives

1. Objective A. Determine how to best store (multi-plane) imaging data in NWB, potentially including pre-processing information such as motion correction displacements and ROIs.
1. Objective B. Determine how to store extracted calcium signals, multi-channel electrophysiological signals, behavior data alongside imaging.
1. Objective C. Add import and export functions for imaging data to SIMA API
2. Objective D. Add import and export functions for all data types to LAB API

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

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
<!-- - Test data: https://link.to.test.data -->
Source code for SIMA: https://github.com/losonczylab/sima

SIMA API Documentation: http://www.losonczylab.org/sima/1.3.2/

SIMA Publication: https://www.frontiersin.org/articles/10.3389/fninf.2014.00080/full

MWE Source code for LAB: https://github.com/losonczylab/Zaremba_NatNeurosci_2017/tree/master/losonczy_analysis_bundle/lab
