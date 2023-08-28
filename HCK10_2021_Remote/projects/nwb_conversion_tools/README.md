[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB Conversion Tools + Breakout

## Key Investigators

* Cody Baker (CatalystNeuro)
* Ben Dichter (CatalystNeuro)
<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->

## Project Description
Develop [NWB Conversion Tools](https://github.com/catalystneuro/nwb-conversion-tools), a library for automatic conversion from a large variety of neurophysiology data formats to NWB. 
<!-- Add a short paragraph describing the project. -->

## Objectives

1. Inform the community about the project: scope, goals, features, etc.
1. Solicit bug reports and feature requests
1. Recruit contributors
<!-- Briefly describe the objectives of your project. What would you like to achive?-->

<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->

## Approach and Plan

1. Begin with simple tutorial demonstrating currently support conversion types
1. Go into more detail about each step of the tutorial and interface
1. Overview of future directions
1. Contribution guidelines
1. Breakout into open discussion
<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

Before: created generic classes for an NWBConverter class object reliant on modular DataInterface classes (one for each format/type). Added DataInterfaces for several `spikeextractors` and `roiextractors` formats, as well as a custom DataInterface for Movie objects (currently on dev branch `add_movie_interface`)

During: Gave presentation on origins and use of the NWB conversion tools, as well as supported features and future directions. Went through notebook tutorials demonstrating the current capabilities and then opened to general discussion. Discussion focused on how to make the process not just automated, but code-independent so that non-programmers could easily specify the data formats they wanted to import and run the full conversion pipeline without ever interacting with python itself.

After: Began draft work and design stages of dynamic class construction from yaml files as well as a folder path iteration based on semantic structure specified by the user in order to run a full conversion over a directory without having to iterate over individual file paths.
<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

`pip install -U nwb-conversion-tools` from a python environment or notebook
Tutorials: [https://github.com/catalystneuro/nwb-conversion-tools/tree/add_tutorials](https://github.com/catalystneuro/nwb-conversion-tools/tree/add_tutorials)
<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

Source code: [https://github.com/catalystneuro/nwb-conversion-tools](https://github.com/catalystneuro/nwb-conversion-tools) (in development)
Documentation: [https://nwb-conversion-tools.readthedocs.io/en/conversion_guide/](https://nwb-conversion-tools.readthedocs.io/en/conversion_guide/) (in development)
Test data (some, not all): [https://gin.g-node.org/NeuralEnsemble/ephy_testing_data](https://gin.g-node.org/NeuralEnsemble/ephy_testing_data), [https://gin.g-node.org/CatalystNeuro/ophys_testing_data](https://gin.g-node.org/CatalystNeuro/ophys_testing_data)
<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

