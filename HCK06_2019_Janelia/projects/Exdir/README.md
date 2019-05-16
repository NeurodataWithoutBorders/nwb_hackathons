[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Implement Exdir as an alternative backend to HDF5

## Key Investigators

 - Mikkel Elle Lepperød (CINPLA, University of Oslo, Norway)

## Project Description

Exdir is a hirarchical data structure similar to HDF5 which operates on the filsystem instead of a HDF5 file. 
It stores data in binary files using numpy (npy files) and metadata in YAML files.
Having Exdir as a backend in NWB would enable users to operate directly on the filesystem.
This facilitate human readability of metadata, possibility to use version control systems such as git and share parts of a large NWB file.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Objective A. Implement object and region references in Exdir.
2. Objective B. Implement a working version of Exdir in hdmf.

## Approach and Plan

1. Implement a lookup table for all objects in a exdir file with uuid for each object.
2. Store references as ids.
3. Implement References and RegionReferences API in exdir.
4. Switch h5py imports with exdir in hdmf.

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
 - Source code: https://github.com/CINPLA/exdir
 - Documentation: https://exdir.readthedocs.io/en/latest/
