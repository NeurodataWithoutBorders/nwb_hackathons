Back to [Projects List](../../README.md#ProjectsList)

# Experimental Structure Viewer

## Key Investigators

- Roni Choudhury (Kitware)
- Nicholas Cain (Allen Institute)
- Michael Grauer (Kitware)
- Ariel Rokem (UW)
- Lydia Ng (Allen Institute)

# Project Description

The ESV takes in an NWB file, then using the SlicerDicer, it extracts data from the file and creates a visualization to help scientists inspect and understand the contents of the file.

## Objective

1. Build on the ESV prototype to provide useful views, filtering and exploration abilities.
1. Use this as a starting point to think about what kinds of structuring would be useful to put into a tool that converts raw data into NWB files, so that the structure is readily apparent when seen with the ESV.
1. Figure out how to incorporate knowledge about how the experiment was performed, and how the steps correspond to contents of the NWB file, for aiding in visualization.

## Approach and Plan

1. Demo current capabilities with example dataset.
1. Have scientists on the project team bring their own use cases and files they want to inspect.
1. Decide what are the most valuable features to add to the ESV for the new use cases and implement those.

## Progress and Next Steps

- Look at [Neuroshape](https://github.com/INCF/neuroshapes/blob/master/provpatterns/assets/wholecellpatchclamp-recording-prov-template.svg) as a model for how to describe experimental structure
- Work with Marina and Justin to determine a one-off, example structure for one of their experiments
- Update the ESV prototype to reflect this structure, and also allow access to data in the NWB file

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Forum: https://github.com/orgs/NeurodataWithoutBorders/teams/experimentalstructureviewer
- Source code: https://github.com/dorukozturk/nwbsd/tree/master/esv
- Documentation: https://github.com/dorukozturk/nwbsd/tree/master/esv/README.md
- Test data: none yet
