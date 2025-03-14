Back to [Projects List](../../README.md#ProjectsList)

# Patchmaster (HEKA) to NWB converter

## Key Investigators

- Sándor Bordé(University of Szeged)

# Project Description

This project aims to write a script which can convert Patchmaster .dat files to NWB format.

HEKA's Patchmaster software generates a binary file which contains every data of the experiment: acquired traces, properties of the acquisition and the stimulus. They described the format of the binary files, but there isn't any available software to read the whole file (only the acquisition data). 

## Objective

1. Get to know with the NWB format and PyNWB.
1. Write a script which reads HEKA data into Python.
1. Write a script which generates NWB files from the HEKA file's Python representation.

<!--## Approach and Plan-->



## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
### Progress
 1. I could understand the concept behind the NWB schema, and I learned how to create and write NWB files from Python using PyNWB.
 1. I found a HEKA to Python reader which reads acquisition data into a Python object. Using this script I could write sweeps into NWB.

### Next Steps
 1. I have to extend the reader script to handle stimulus data too. 
 1. Modify the NWB file writer script to include all data (not only the acquired data).

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
