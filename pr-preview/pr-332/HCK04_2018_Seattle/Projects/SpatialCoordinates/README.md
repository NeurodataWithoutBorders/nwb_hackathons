Back to [Projects List](../../README.md#ProjectsList)

# Spatial Coordinates

## Key Investigators

- Luke Campagnola (Allen Institute)
- Jed Perkins (Allen Institute)

## Project Description

Schema and API for incorporating information about spatial coordinates, coordinate systems, and transforms. The major goals are to make it easy to (1) determine the spatial relationships between any two objects in an NWB file, and (2) map the coordinates of data within the NWB file to external, standardized coordinate systems. 

**Main discussion**: https://github.com/NeurodataWithoutBorders/nwb-schema/issues/103

## Objective

1. Objective A. Develop a schema extension that allows spatially-registered data to be described in a consistent way
    * Images have position/orientation/scale, electrodes have position/orientation, etc. 
    * All spatial information is described relative to a particular coordinate system, which must be declared elsewhere in the NWB.
    * NWB files may define multiple coordinate systems, and these may be related to each other by a transformation (such as offset, rotation, affine, etc)
1. Objective B. Suggest a set of standard coordinate systems (eg. CCF or stereotaxic) against which it is recommended to provide transformations, so that physical coordinates across multiple experiments can be automatically mapped to the same external coordinate system.
1. Objective C. Develop a python API to handle the details of accessing and mapping coordinates.

## Progress

* We collected many use cases / suggestions and came up with a plan for schema and API changes that met all use cases well. The proposed plan is described in #103.
* An initial attempt was made at developing the schema and API changes to support transform annotation: https://github.com/JFPerkins/pynwb/tree/spatial_coordinates
* An initial attempt was made to develop coordinate transformations for use in the python API: https://github.com/campagnola/transformy
