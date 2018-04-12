Back to [Projects List](../../README.md#ProjectsList)

# Advanced Data I/O via PyNWB

## Key Investigators

- Oliver Ruebel (LBNL)
- Andrew Tritt (LBNL)
- Ben Dichter
- Thomas Braun
- Jean-Christophe Fillion-Robin (Kitware)
- Aaron D. Milstein  (Stanford)

# Project Description

Enhance and gather requirements for advanced data I/O features, e.g.:
  * Compression
  * Iterative data write
  * Data streaming
  * MPI parallel I/O
  * External files

## Objective

1. Create list of requirments for the various advanced I/O features
1. Expand existing advanced I/O features as needed to better support the requirements
1. As approbriate, prioritize and define plan for how the features could be implemented

## Current functionality

1. Basic compression is currently supported via the [H5DataIO](http://pynwb.readthedocs.io/en/latest/pynwb.form.backends.hdf5.h5_utils.html#pynwb.form.backends.hdf5.h5_utils.H5DataIO) class. An example for how to use H5DataIO is part of the PyNWB docs http://pynwb.readthedocs.io/en/latest/example.html#compressing-datasets .
1. Iterative data write (and streaming) are currrently supported via:
  * [DataChunkIterator](http://pynwb.readthedocs.io/en/latest/pynwb.form.data_utils.html#pynwb.form.data_utils.DataChunkIterator) Class for defining and iterating over data chunks. A number of additional classes related to the iterative data write are defined in the [data_utils](pynwb.readthedocs.io/en/latest/pynwb.form.data_utils.html#pynwb.form.data_utils) module, e.g. [AbstractDataChunkInterator](pynwb.readthedocs.io/en/latest/pynwb.form.data_utils.html#pynwb.form.data_utils), [DataChunk](pynwb.readthedocs.io/en/latest/pynwb.form.data_utils.html#pynwb.form.data_utils), [ShapeValidator](pynwb.readthedocs.io/en/latest/pynwb.form.data_utils.html#pynwb.form.data_utils), etc.
  * [HDF5IO](http://pynwb.readthedocs.io/en/latest/pynwb.form.backends.hdf5.h5tools.html#pynwb.form.backends.hdf5.h5tools.HDF5IO) implements the actual iterative data write (see ``__chunked_iter_fill__`` function)
  * [monitoring](pynwb.readthedocs.io/en/latest/pynwb.form.monitor.html) 
  * A start for a tutorial for iterative data write is on the following branch but its far from complete: https://github.com/NeurodataWithoutBorders/pynwb/compare/iter_write_tutorial
1. External files are currently supported through "reuse" of NWBContainers and through passing in of h5py.Dataset objects. Some known needs are:
 * **See progress below** Instead of using h5py.Dataset as inputs to NWBContainers to then create external links, this behavior should be made explicit by wrapping the datasets using HDF5IO and then configuring things on the container. This is needed to 1) make it explicit to users whether ExternalLinks are being created, 2) enable copy vs. linking of data, 3) facilitate error checking for mismatching attributes
 * **TODO** Need to add error checking ot ensure that attributes on the dataset match what the user is providing 
  
## Approach and Plan

1. Review existing functionality in PyNWB for compression, iterative write, streaming,, external files, and parallel I/O
1. Identify missing features
1. Prioritize and define plan for implementing missing features and identify implementation leads for the different features. 

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
- The following pull request has been merged: https://github.com/NeurodataWithoutBorders/pynwb/pull/400
  - Allow use of HDF5IO to configure creation of external links 
  - Allow customization of default behavior when h5py.Dataset objects are used as input on write
  - Expand the list of supported I/O parameters on HDF5IO to allow chunking, compression, etc. options to be set explicitly
  - Some minor improvements to DataChunkIterator 
 - Next steps:
  - Oliver to create Advanced Data I/O tutorial for the hackathon at LBNL
  - Enhance HDF5IO to create a queue with all DataChunkIterators to allow customization of how the write of DataChunkItertors is handled
    (see use case described in https://github.com/NeurodataWithoutBorders/pynwb/pull/310 and https://github.com/NeurodataWithoutBorders/pynwb/pull/309)
  - MPI I/O
  
# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Forum: https://github.com/orgs/NeurodataWithoutBorders/teams/YourSubTeam
- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
