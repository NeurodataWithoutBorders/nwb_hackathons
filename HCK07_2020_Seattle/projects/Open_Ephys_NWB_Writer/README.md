[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB 2.0 Data Format Plugin for the Open Ephys GUI

## Key Investigators

- Josh Siegle (Allen Institute)
- Pavel Kulik (Allen Institute)

## Project Description

The Open Ephys GUI provides a modular interface for acquiring multichannel extracellular electrophysiology data. Its plugin architecture makes it straightforward to add new formats for recording data. The GUI currently supports writing in NWB 1.0 format, which is now deprecated. We plan to create a new plugin that can stream data directly to NWB 2.0 files.

## Objectives

1. Generate HDF5 files from Open Ephys that are compatible with the NWB 2.0 spec
2. Stream continuous and event data into the file (ideally from a Neuropixels probe)
3. Read data saved with Open Ephys using the Python or Matlab API

## Approach and Plan

1. Find an existing NWB 2.0 file containing raw ephys data, which we will attempt to replicate from Open Ephys.
2. Using the current `NWBFormat` plugin as a starting point, update the `NWBFile::createFileStructure()` method to match the example file.
3. Ensure that the `writeData`, `writeEvent`, `writeSpike`, and `writeTimestamps` methods are compatible with the new file structure.
4. Build the new plugin and stream 384 channels of data from a Neuropixels probe.
5. Confirm that the resulting file can be read with existing NWB tools, such as the Matlab or Python SDK.

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

* [NWBFormat plugin source code](https://github.com/open-ephys-plugins/HDF5Plugins)
* [Open Ephys data format documentation](https://open-ephys.atlassian.net/wiki/spaces/OEW/pages/491632/Data+format)

