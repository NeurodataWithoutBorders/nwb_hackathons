[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Integrate all types of data from the Neuromodulation Research Center

## Key Investigators

Lingling Yang (UMN)

## Project Description

Will integrate all types of data from the Neuromodulation Research Center
1. raw data (nwb.acquisition)
   - data from tdt system (*.sev file)
     - neural data (tdt.Neur)
       - electrode types
         - utah array
         - gray matter
     - not neural data 
       - touch pad data (tdt.Stpd)
       - eye movement data
         - x,y time series position (tdt.EYEa)
         - sync time series data from eye movement system (tdt.EYTt)
   
   - motion analysis system
   
   - eye tracking system
   
   - gait mat system
  
2. preprocessed data

3. general information
   - condition: ('normal', 'mild', 'moderate', '?')  % need to check the field to store this inf
   - therapy: ('none', 'DBS', 'DBS+Lodapa') . % check how to spell the word
   - .experimenter ('Ying', 'Ethan')
   - .

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->
1. The proper field to place data of various systems


## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->

### Achieved
Have convert raw data from tdt, ma systems 

<!--Describe the next steps you are planing to take to complete the project.-->

### Questions
1. Is it possible to store all the data in a structure from the same systsem? 
like:    nwb.acquisition.set('tdt').set('neur'), nwb.acquisition.set('tdt').set('tdtstpd')  
current: nwb.acquistion.set('tdtneur'), nwb.acquistion.set('tdtstpd')

learned: right now no, keep the previous setup.

2. Read select channels that are not continous? 
e.g [1 3 4] 

Learned: extract one channel by one

3. search pariticular condition?

learned: no search across files.

4. Learned: Keep the spreadsheet for the spatial location ('STN') which may be modified across time.

5. Learned: Use group for utah array, gray matter, dbs et.al

6. Is it possible to extract data through electrode index?

Learned: extract one channel by one
   

7. Video storage?

Learned: 


Learned:

Advanced I/O Storage:

-- raw data read-only, processed data with a separate file

-- all time data are stored relative to a single global clock: NWB.session_start_time or 

-- data is ultimately stored in one-dimensional compute memory

-- compress data 

Pop up:

1. hierarchy architecture for .acquisition field: acquisition -> tdt ->  tdtneur, tdtstpd, tdteyet,....

2. Search across files for one particular condition ?

3. Shared information for several files and manage the update.



## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
Relevant work:
https://github.com/yangll0620/DataStorageAnalysisArchitecture
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
