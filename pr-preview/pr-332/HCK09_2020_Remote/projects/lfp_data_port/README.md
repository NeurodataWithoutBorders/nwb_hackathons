[:rewind: Back to the projects list](../../README.md#ProjectsList)

# Port Current LFP/Behavioral Database to NWB 

## Key Investigators

Eric Thomson (NIEHS/NIH)    
Jesse Cushman (NIEHS/NIH)    
Korey Stevanovic (NIEHS/NIH)    

## Project Description

We currently have LFP and behavioral data from about 50 animals, three behavioral sessions for each animal. My goal is to port from the current (rather sprawling) SQLITE database with 11 tables to NWB, in a way that will scale well with our needs going forward to include multiple additional projects.

## Objectives

1. Port LFP and behavioral data to NWB.
2. Interface rudimentary processing workflow with NWB format.
3. Learn about NWB processing pipelines and Jupyter notebook opportunities.
4. Consider how well this local solution will scale to future projects.

## Approach and Plan

1. Add data from a single animal for single type of training session, to make sure workflow can go smoothly.
2. Add additional acquisition sessions for same animal (context and tone training).
3. Do same for multiple animals (I think a toy db with five animals is a good goal at first to get the basics in place).
4. Integrate current processing pipeline (spectrogram, filtering, etc) with above.
5. Consider scalability: how well will above generalize to future projects?
6. Consider what NWB offers in terms of processing pipelines, see if I can integrate anything new in there.


## Progress and Next Steps
1. Python code extracts data from current database.
2. Went through the intro and neurophys tutorials at NWB site.
3. Next step is Step 1 above from **Approach and Plan**.


## Materials
--
<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References
--
<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

