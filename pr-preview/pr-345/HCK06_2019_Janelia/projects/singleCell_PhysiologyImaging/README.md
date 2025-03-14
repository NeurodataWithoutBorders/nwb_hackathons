[:rewind: Back to the projects list](../../README.md#ProjectsList)

# Simultaneously recorded physiology and imaging data from single cells in slice

## Key Investigators
Andrew Landau (Harvard Medical School)
Bernardo Sabatini (Harvard Medical School)

## Project Description
Goals:
  1. Integrate single-cell physiology and imaging data in NWB:N.
  2. File extension for kymograph data - probably an extension of time series linked to an image.  

General Challenges: 
  1. Physiology and imaging data recorded at different sampling rates
  2. Acquisitions for each ROI are hierarchically labeled, Cell-Dendrite-Spine

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->
Objective A: Develop a NWB:N organization method for saving discrete acquisitions of single cell physiology and imaging data. The key is that a recording from each cell has many time series associated with it grouped into separate discrete epochs. 

Objective B: Develop an extension for kymographs - useful for single cell imaging and lots of cell biology. These are a data format organized as a matrix with time on one axis and space on another axis. 


## Approach and Plan
For Objective B: 
- create a "kymograph" extension for time series data. 
  - it will be a linear vector (time series) where each line scan is concatenated consecutively
  - meta data:
    - number of pixels per line
    - spatial position of each pixel
    - sampling rate
    - flag for whether each line was recording in the same direction (to accomodate bidirectional scans)

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
