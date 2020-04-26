[:rewind: Back to the projects list](../../../HCK06_2019_Janelia/README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Tilt Brush to NWB

## Key Investigators

Andrew Tan (Yale University)
Marike Reimer (Yale University)

## Project Description

We are developing a workflow that uses Tilt Brush, a virtual reality illustration program, to trace neural anatomy.  We analyze these files with Fusion 360, which produces .obj files for image segmentation.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

Store renderings from .obj files in the 2 photon imaging module.

## Approach and Plan

Preliminary research suggests that the manifold should be used to store the reference coordinates for the .obj files.  ROIs may be a good fit for storing the triangular image faces.

## Progress and Next Steps

We convert image stacks from established workflows to .obj files.
The .obj files are loaded into TiltBrush and anatomy can be traced and exported as a .fbx file.
Fusion 360 is used to analyze the .fbx files and saves image segments as .obj files.

Next Steps: Store analysis results in NWB format

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
