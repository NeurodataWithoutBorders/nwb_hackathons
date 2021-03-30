[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# NWB Extensions Infrastructure

## Key Investigators

Ryan Ly (LBNL) @rly

## Helping hands

Yaroslav O. Halchenko (Dartmouth, DANDI) @yarikoptic
John T. Wodder (Dartmouth, DANDI) @jwodder

## Project Description

NWB supports user-created extensions to the standard to add support for data types from new technologies and lab- or experiment-specific data types. Many of these extensions are published in the NDX Catalog. It would be nice if PyNWB users had a way to easily install extensions that are found in the catalog.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Publish catalog records for AIBS extensions that were not cached with the file.
2. Establish a CI testing across versions of hdmf+PyNWB and extensions to ensure
3. In PyNWB, update the error message for when an extension is not found. It should tell users to search for the extension in the NDX Catalog or run a command line tool to download and install the extension.
4. Create a command line tool to search for a given extension in the NDX Catalog, download it, and install it.
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
### 2. CI

- Cover following testing scenarios
   - save/load cycle resulting in identical data structure
     - have helper to produce "saved" .nwb files with clear "provenance" records to test against 
     - each extension should provide interface to produce "an example (lean but representative)" file 
   - ability to load NWB files saved by prior versions of hdmf/pynwb(/extension)
   - ability to work with an extension version(s) in the declared "compatibility" range  
   - absent side-effects from having other extensions loaded
- Have tests regularly run and update status
- Have (subset?) of testing across extensions ran for PyNWB PRs
- Borrow ideas/setup from possible existing setups:
  - https://github.com/datalad/datalad-extensions/ - github/github-actions driven dashboard for DataLad extensions
  - @yarikoptic had some related setup in elderly PyMVPA to ensure that h5save'd files could be later h5loaded

<!-- 1. ... -->

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

NDX Catalog: https://nwb-extensions.github.io/

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

