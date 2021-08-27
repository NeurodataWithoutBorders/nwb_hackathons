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

Behavior Data
  * Data has been cleaned into pandas dataframes from the raw csv files and
  then written to HDF5. However, after speaking with Ryan Ly, it should be
  done in a different way so people writing in MATLAB _or_ Python can use it.
  1. Write raw csv into NWB HDF5
  1. Clean data into timestamps and populate a dynamic table for stimuli and
  an events list for licking behavior
  1. Write out configuration file of experimental metadata to the NWB file

2P Data
  * Data is written at runtime to disk in Bruker's proprietary format and then
  converted into tiffs using their imaging ripping utility. These tiffs are
  merged into one HDF5 file in MATLAB but not in NWB format.
  1. Use Deisseroth Lab's repository to containerize the image ripping utility
  and deploy on SNL hardware.
  1. Take results of their ripper and put them into NWB file seamlessly
  1. Use Suite2p/CaImAn to perform motion correction, DeltaF/F
  calculation, and cell registration for the dataset.

## Progress and Next Steps

8/25/21: Didn't work on this much this day.
8/26/21: Starting building base NWB file as part of experiment runtime.
I can build NWB files no problem, but need to determine which fields
I can automate/gather from XML file for imaging/configuration files.
I'm also trying to find out how to make the NWB Subject format fit
into the data framework, need some assistance there. Containerization
for 2P writing will be worked on tomorrow/this weekend using both
CaImAn and Suite2p so I can compare the process for each version.
I also need to ask about how to put the raw CSV file, XML file, and
raw Bruker format into NWB as well/determine if it's needed at all.

## Materials

The developments can be followed along in the bruker_control folder
in the git repo below's source code in the branch:
"bruker_control_refactor"

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
