[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB Conversion Tools

## Key Investigators

* Cody Baker (CatalystNeuro)
* Ben Dichter (CatalystNeuro)
<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->

## Project Description
Develop [NWB Conversion Tools](https://github.com/catalystneuro/nwb-conversion-tools), a library for automatic conversion from a large variety of neurophysiology data formats to NWB. 
<!-- Add a short paragraph describing the project. -->

## Objectives

1. Understand needs of the community
1. Build software to support missing formats
1. Expand testing infrastructure
1. Enhance documentation and other forms of communication so it is easy to understand how to use
<!-- Briefly describe the objectives of your project. What would you like to achive?-->

<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->

## Approach and Plan

1. Begin with simple tutorial demonstrating currently support conversion types
2. Go into more detail about each step of the tutorial and interface
3. (optional if time) Display and analyze the underlying code structure of the classes and functions
4. Solicit requests from the community for future support of high-demand data types and formats not currently included
<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

Before: created generic classes for an NWBConverter class object reliant on modular DataInterface classes (one for each format/type). Added DataInterfaces for several `spikeextractors` and `roiextractors` formats, as well as a custom DataInterface for Movie objects (currently on dev branch `add_movie_interface`)

During:

After:
<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

`pip install -U nwb-conversion-tools` from a python environment or notebook
TODO: add/link to tutorials
<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

Source code: https://github.com/catalystneuro/nwb-conversion-tools (in development)
Documentation: https://nwb-conversion-tools.readthedocs.io/en/conversion_guide/ (in development)
<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

