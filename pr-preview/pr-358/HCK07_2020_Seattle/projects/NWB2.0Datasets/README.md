[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Convert and add NWB2 datasets to DANDI

## Key Investigators

- Satrajit (satra) Ghosh (MIT)
- Yaroslav (yarik) Halchenko (Dartmouth)
- Ben Dichter (Ben Dichter, LLC)
- Michael (mike) Grauer (Kitware, LLC)

## Project Description

There are several public NWB datasets out there, but they vary in their conformance to NWB and 
their readability via PyNWB. Thie project aims to make public datasets conformant to NWB 2.0 
and findable/accessible through the DANDI archive.

## Objectives

1. Extend PyNWB to determine what's missing to be NWB 2.0 compliant.
2. Convert current DANDI datasets to 2.0
3. Determine the necessary pieces for a DANDI dataset (dandiset).

## Approach and Plan

1. Verify that all files are matching with source files 

- http://datasets.datalad.org/?dir=/labs/buzsaki
- http://datasets.datalad.org/?dir=/labs/churchland
- http://datasets.datalad.org/?dir=/labs/svoboda
- http://datasets.datalad.org/?dir=/allen-brain-observatory

2. Create a list of non-compliant files and determine what makes these non-compliant.
3. Make files compliant while tracking the conversion.
4. Create `dataset_description.jsonld` using Metadata descriptor keys (see below). Discuss metadata harmonization and terms necessary.
5. Automate creation of `samples.tsv/jsonld` from individual NWB files
6. Package the dataset creation, validation, upload, and download process into dandi-cli
7. Add Metadata editing GUI to DANDI.

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

- [Metadata](https://docs.google.com/document/d/1WvRr9J2Ums0-CQIcdUeFZakE2RPeagRnexUBFDiiV7w/edit?ts=5defc58b)
- [PyNWB](https://github.com/NeurodataWithoutBorders/pynwb)
- [DANDI cli](https://github.com/dandi/dandi-cli)
- [DANDI gui](https://gui.dandiarchive.org/#/)
- [DANDI hub](http://hub.dandiarchive.org/)
- [Dandisets](https://github.com/dandisets)
