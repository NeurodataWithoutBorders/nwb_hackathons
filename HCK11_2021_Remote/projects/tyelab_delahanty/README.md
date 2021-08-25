[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Tye Lab 2P Data NWB Conversion (Jeremy)

## Key Investigators

Jeremy Delahanty (The Salk Institute for Biological Studies)

## Project Description

This project is intended to convert currently existing 2P datasets - which
contain optical physiology, mouse headfixed behavior, mouse face recordings,
and configuration files - into datasets compliant with NWB.

## Objectives

I aim to convert at least the mouse behavior recordings and 2P datasets into
NWB compliant datasets.

1. Behavior Datasets: Convert the raw csv output from Bruker Microscopy DAQ
into a raw NWB file, clean it and format stimuli events into a dynamic table,
and finally incorporating licks into the dataset as events.

1. 2P Datasets: Convert raw Bruker Microscopy files into NWB complaint hdf5
format.


## Approach and Plan

1. Behavior Data
  * Data has been cleaned into pandas dataframes from the raw csv files and
  then written to HDF5. However, after speaking with Ryan Ly, it should be
  done in a different way so people writing in MATLAB _or_ Python can use it.
  1. Write raw csv into NWB HDF5
  1. Clean data into timestamps and populate a dynamic table for stimuli and
  an events list for licking behavior
  1. Write out configuration file of experimental metadata to the NWB file
1. 2P Data
  * Data is written at runtime to disk in Bruker's proprietary format and then
  converted into tiffs using their imaging ripping utility. These tiffs are
  merged into one HDF5 file in MATLAB but not in NWB format.
  1. Use Deisseroth Lab's repository to containerize the image ripping utility
  and deploy on SNL hardware.
  1. Take results of their ripper and put them into NWB file seamlessly
  1. Use Suite2p/CaImAn to perform motion correction, DeltaF/F
  calculation, and cell registration for the dataset.

## Progress and Next Steps

8/25/21:
<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

Bruker Microscopy built Prairie View for recording 2P data and provided an API
that can be interacted with in Python, MATLAB, and C/C++. The system I've
written to govern the experiment uses Python and is called 'bruker_control'.
It's part of a repository that was developed with my lab mates to unite
imaging, stimuli, behavior, and video of the mouse's face into one program.

The source code for the repository is linked below as is a first iteration of
some documentation hosted on readthedocs that is still very much under
development.

Source code: https://github.com/Tyelab/headfix_control
Documentation: https://bruker-control.readthedocs.io/en/latest/
