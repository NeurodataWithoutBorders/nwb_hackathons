[:rewind: Back to the projects list](../../README.md#breakout-sessions)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB via the web: Linking data and accessing NWB files via the web

**Session Chair:** Andrew Tritt (LBNL)

The goal of this session is to discuss needs and approaches for linking data via NWB and access of parts of NWB files via the network.

## Participants

* Andrew Tritt (LBNL)
* Oliver Ruebel (LBNL)
* Yaroslav Halchenko (Dartmouth College)
* Pam Baker(Allen Insititute for Brain Science)
* Michael Grauer (Kitware, Inc.)
* Satrajit Ghosh (MIT)
* Ariel Rokem (UW)
* Josh Siegel (Allen Insititute for Brain Science)
* ...

## Objectives

* Identify use-cases and requirements for accessing parts of NWB files via the network (Local, LAN, and WAN)
* Identify possible approaches for enabling linking of data via NWB

### Proposed discussion topics

Participants should add topics of possible interest for discussion here

* How can we support foreign fields in NWB (i.e., support linking to data from NWB)?
* How can we enable web-based access to NWB files?
* Do we need alternative storage backends to facilitate web-based data access (e.g., HDF5, KITA, ZARR, ...)?

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

* Two main use cases determined:
    1. accessing of partial datasets 
       * chunks of objects or whole objects
    2. interlinking between related datasets
       * e.g. connect separate files for LFP and spiking data 

* investigate HDF5 VOL for creating VOL that can access data over the web without downloading entire datasets
* https://github.com/pierlauro/H5PyVOL
    * https://github.com/pierlauro/H5PyVOL

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
