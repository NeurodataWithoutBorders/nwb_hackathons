[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Tilt Brush to NWB

## Key Investigators

Andrew Tan (Yale University)

Marike Reimer (Yale University)

## Project Description

We are developing a workflow that uses Tilt Brush, a virtual reality illustration program, to trace neural anatomy.  We analyze these files with Blender/Fusion 360, which produces .obj files for type of mesh created.  Our research focuses on dendritic spines and our analysis generates spine volume, points describing length and width, and center of mass.  Ultimately we would like to develop an add-in for Blender/Fusion 360 which writes our data to NWB files.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

Store renderings from .obj files in the 2 Photon imaging module.
Store points from spine analysis as ROIs.
Store volume and center of mass in image segmenation.

## Approach and Plan
Store renderings from .obj files in the 2 Photon imaging module.
Store points from spine analysis as ROIs.
Store volume and center of mass in image segmenation.

## Progress and Next Steps

Using PhotoShop/Fiji image stacks are converted to .obj files.
The .obj files are loaded into TiltBrush and anatomy can be traced and exported as a .fbx file.
Blender/Fusion 360 is used to analyze the .fbx files and saves image segments as .obj files.

Next Steps: Store meshes, ROIs, spine volume, and center of mass.

Future Development: Develop add-in for Blender/Fusion 360 to automate writing data to NWB.

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials
All code and sample data can be found here:
https://github.com/MarikeReimer/HackathonFiles/tree/master/HackthonFiles

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References


<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
