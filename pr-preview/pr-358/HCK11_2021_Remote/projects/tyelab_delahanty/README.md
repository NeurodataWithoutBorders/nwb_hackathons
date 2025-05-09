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

8/28/21 & 8/29/21: Gathered metadata from Bruker's Prairie View and 
built project specific yml files for configuration values. One day
this should definitely be made into a database, probably with DJ.
These metadata then populate an NWB file which currently has the
following information built: Lab/experimenter, devices, imaging plane.
There's a few things I need to double check about what's the appropriate
values for the fields in the file, but I made a fair bit of progress
this evening with automating the building of relevant metadata for NWB
the moment the microscopy session (read: imaging plane) ends.

8/30/21: I've completed building a base NWB file but need to review
it with someone from the Dev team before I feel confident pushing it
into production. Struggled to understand the Subject file and how to
use it properly, but will be hopefully getting advice soon. Main
problem was how I'll need multiple weights accounted for per animal
but that functionality doesn't appear to be present in NWB. There's
additional metadata that I think makes sense to incorporate into the
system such as laser power and PMT gains, but I see no way to do so
in NWB. I still need to build a base behavior part of the dataset as
well and review what makes sense to have timestamp wise for given
behavior datasets.

9/13/21: A week ago, with the help of Ryan Ly, I finally got
all the available base metadata written to an NWB file the moment the
experiment is over! I've been informed of the different kinds of
things that require extensions so I will be working on those in the
coming weeks. Forgot to update here...

9/26/21: Started writing an extension for including Arduino config
metadata that's used for performing the behavior experiments this
evening. A little stuck on the next steps file, but slowly working
through it. The planned extensions I'll be writing are to include
the following:
- Arduino metadata used for configuring behavior experiment
- More specific surgery information for the surgery field in `Subject`
- Additional metadata about pockel and PMT values used during imaging
- Behavior specific metadata (i.e. sucrose concentration, air PSI)
- Mouse facial expression recordings with associated metadata

A complete NWB File for the Bruker 2P setup will thus include:
_Raw Data_
- Raw behavior data (voltage recording)
- Raw video of mouse face
- Raw 2P Data
- Raw Z-stacks (likely 8 - 16 of them) per indicator
- Arduino configuration
- Trial structure configuration
- Behavioral setup metadata
- Laser/PMT/Pockel/Scope objective configuration for T-Series
- Laser/PMT/Pockel/Scope objective configuration for Z-Stacks

_Processed Data_
- Reference image for recordings from Suite2P
- Suite2p configurations for segmentation/analysis
- Motion corrected t-series
- Cell registrations as `optical-channels`
- Cell traces
- Spike deconvolution (maybe...)
- Averaged z-stacks
- HOG Matrcies of mouse facial expression
- Mouse behavior timestamps from trial structures according to paper's analysis
- More?

## Materials

The developments can be followed along in the bruker_control folder
in the git repo below's source code in the branch:
"bruker_control_refactor"

8/29/21: If you want to see the updates from the above progress notes,
check out the nwb_utils.py file in the bruker_control folder. It's
quite messy in there for now, but hopefully it does make a little
sense if you look around.

9/13/21: The bruker_control refactor that includes the completed
nwb_utils module is complete! You can check it out on the repo if
you want. There's also better documentation for things now on the
linked readthedocs site below.

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
