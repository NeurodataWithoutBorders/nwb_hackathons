[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB Camera Capture code

## Key Investigators

* Jochen Weber (Zuckerman Mind Brain Behavior Institute, Columbia University)
* David Nicholas (Zuckerman Mind Brain Behavior Institute, Columbia University)

## Project Description

<!-- Add a short paragraph describing the project. -->
This project will investigate the extension of existing Python code from 
David Nicholas's lab. The code currently in the terminal only. The goal is to 
extend this code to make use of the NWB:N framework as well as to add a GUI.

More specifically, the code captures 8-bit integer, single-channel frames and
currently stores them as a series of individual JPG files, which makes later processing
relatively cumbersome. Instead, we would like to seek a solution wherein the data is
stored in a compound format/framework, including meta data, etc.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Investigate how the NWB:N framework can be applied for storing frame-by-frame image
   data. Using the Python NWB:N interface, replace the existing portion of the code
   that stores the frames (images) into JPG files with (a) code that creates and
   handles an NWB:N framework object, (b) stores all necessary meta data into this
   object, and (c) then adds all frames into the same object.
   
2. Provide one sample application (in either Python or MATLAB) that uses such an object.
   As a proof-of-concept, we wish to develop a quick application that will open the
   NWB:N framework object containing the captured frames, and (together with the meta
   data) processes the frames in a meaningful way (e.g. quality control or some simple
   statistic).

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
