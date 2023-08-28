[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Implement NWB file adapters for NANSEN

## Key Investigators

Eivind Hennestad (University of Oslo)

## Project Description

Create a set of classes to interact with NWB data (read/write) from NANSEN. NANSEN is a matlab package for managing, processing and visualizing calcium imaging data: [https://github.com/VervaekeLab/NANSEN](https://github.com/VervaekeLab/NANSEN)

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achieve?-->

1. Objective A: Create a list of data variables with names according to the NWB Schemas
2. Objective B: Create a data input/output interface for NWB files. Read and write specific variables to NWB files.
3. Objective C: Learn more about how other people use NWB and what kind of data readers/writers already exists.

## Approach and Plan

1. Create an abstract VariableFileAdapter class. A class providing methods for a) reading and writing a predefined variable from/to a specified file format and b) specify how to open data for visualization.
2. Create an abstract DataIOModel. Class interface to read/write data from/to different datalocations, using different variable file-adapters
3. Create implementations of VariableFileAdapter for the NWB format
4. Use classes above to read experiment dataset from my phd work and save it to NWB file.
5. Use classes above to read an NWB dataset into a Nansen project.

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project, e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planning to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

See [https://github.com/ehennestad/Nansen-NWB.git](https://github.com/ehennestad/Nansen-NWB.git) for details

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
