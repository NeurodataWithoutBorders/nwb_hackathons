[:rewind: Back to the projects list](../../README.md#breakout-sessions)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

#  NWB and DataJoint

**Session Chair:** Shan Shen (Vathes)


## Participants

* Oliver Ruebel
* Shan Shen
* Ryan Ly
* Benjamin Dichter
* Andrew Tritt
* Satrajit Ghosh

## Objectives

* Figure out directions to improve interoperability between NWB and DataJoint

### Proposed discussion topics

* Demo working on NWB objects and files with DataJoint
* Discuss strategies and needs for NWB DataJoint integration

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->
1. DataJoint developed the feature dj.AttributeAdapter to support arbiturary data types
2. This repository provides a simple demo for how to create an customized data type (e.g. NWB object), insert and fetch that data type to/from the DataJoint table
3. There are two major ways to implement an NWB object as an DJ adaptive fields
    a. save all parameters as a dictionary in the `put` function and reconstruct the nwb object in the `get` function
    b. save the object in an nwb file with an external link to the master file in the `put` function and return the filepath in the `get` function


## Progress and Next Steps

Notes:
+ A potential NWB extension for DataJoint, which packs the NWB object corresponding DJ attribute adapters.
+ b) in the last section is preferable because every instantiation of an nwb object will assign a new object id. A better way to store meta information is to put them in the master file in the

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
https://github.com/vathes/DataJoint-NWB-showcase
