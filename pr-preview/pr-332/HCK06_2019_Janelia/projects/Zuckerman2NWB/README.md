[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Create demonstration code to convert files from Zuckerman to NWB format

## Key Investigators

Jochen Weber (Zuckerman Research Computing)

## Project Description

This project is meant to demonstrate to the institute's faculty and their labs,
associated with one of the two U19 projects (Costa and Miller), that data
routinely used in data processing pipelines in the labs can be readily converted
into and store as NWB:N files.

## Objectives

1. Identify meta data mapping. Investigate each of the provided files/datasets
   w.r.t. what meta data is provided, and create a brief text file for each.

2. Create initial pass of (stub) code. Read in the data (either in Python or
   MATLAB, depending on the input format!), and using pynwb or matnwb respectively
   convert into NWB:N format, while preserving as much of the meta data from
   (1) as possible.

3. Test formats. Read in the written out NWB:N objects in both Python and MATLAB
   to confirm that data can be read back and interchanged between environments
   (taking care of indexing differences, in terms of dimension order and 0- vs.
   1- based indexing!).

## Approach and Plan

1. Initial pass of loading each of the input formats into memory/inspecting existing
   fields, and writing down what meta data exists; this is mainly an information
   gathering mission--some formats will probably lack a lot of additional information
   to fully appreciate the meaning of fields, just the situation that NWB:N sets out
   to remedy!

2. Using existing format conversion projects (from github repositories or the pyNWB
   tutorial projects page), adapt those code files for use with the datasets provided
   by Zuckerman researchers for this hackathon.

3. Ensure that the files (objects) can be read back into Python/MATLAB, and compare
   their contents with the objects prior to writing to disk (ensuring stability), and
   then perform cross-platform comparisons.

## Progress and Next Steps

### Day 1:

1. created (this) project description page

## Materials

The following data objects were provided

1. Sean Perkins (Churchland lab): Monkey 256-channel ephys recording of 50 trials (in MATLAB table)
2. Nic Thibodeaux (Hillman lab): one mouse/session/run/stim example file with codebase (optical imaging)
3. Mario DiPoppa (Theory Center): processed cellular (CA+?) imaging data with extracted traces and masks
4. Mario DiPoppa (Theory Center): additional data for testing from mouse retinotopy (source: ?)
5. U19 project collaborator: raw TIF stack from two-photon calcium imaging (motion not yet corrected, no meta data?)

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
