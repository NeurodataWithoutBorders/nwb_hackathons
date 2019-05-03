[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Visualizing contents of NWB files with NWB Explorer and Open Source Brain 

## Key Investigators
- Matt Earnshaw (UCL)
- Padraig Gleeson (UCL; remote)
- Matteo Cantarelli Gleeson (MetaCell; remote)

## Project Description
[Open Source Brain](http://opensourcebrain.org) is an open source, web-based resource for visualising, simulating and 
disseminating standardised models of neurons and circuits from many brain regions including the neocortex, cerebellum 
and hippocampus. Over the next three years we will be extending OSB to include integrated visualisation and analysis of 
the experimental (anatomical, electrophysiological, imaging and behavioural) data used to build and test such models, 
alongside the models themselves. By closing the loop between data and models, this new version of OSB will provide 
accessible models of brain function that can be reused for new scientific questions, by the wider neuroscience community. 

At the 2018 Seattle Hackathon, a first step was made towards this vision with the 
[NWB Explorer project](https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK04_2018_Seattle/Projects/NWBExplorer). 
A workable proof of concept, there remains much work to be done. The NWB Explorer demo is based on the 
[Geppetto platform](http://www.geppetto.org/), as is the OSB 3D visualisation functionality. It is planned that NWB Explorer will be available both as:

- A **standalone desktop application** for visualising the contents of NWB files
- An **integrated component of OSB**, allowing visualation of shared NWB content (e.g. from Figshare) through the browser without installing any local software

Our primary goal at this hackathon will be to gather existing 
NWB datasets to check and improve compatibility with the basic parser of NWB Explorer, determine scientifically useful workflows 
and the components necessary to support them, and develop a basic widget for exposing in a readable fashion the structure of an NWB file.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Test the existing NWB Explorer with multiple data sets
2. Get initial user/usability feedback
3. Collect public datasets for (automated) testing of future versions of NWB Explorer
4. Determine scope of current/pending public NWB dataset releases (i.e. what types of data will be included and should be prioritized, image stacks, videos, etc.)

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
1. Exchange NWB files with other participants
2. Get other attendees to try out desktop & online version of NWB Explorer
3. Get other attendees to add example datasets/conversion scripts to https://github.com/OpenSourceBrain/NWBShowcase 
(or [add issue](https://github.com/OpenSourceBrain/NWBShowcase/issues)).
4. Get timelines of labs' data release plans; assess attendee demand for functionality in NWB

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References
- 2018 Hackathon NWB Explorer project: https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK04_2018_Seattle/Projects/NWBExplorer
- NWB Explorer: https://github.com/MetaCell/nwb-explorer
- Open Source Brain: http://opensourcebrain.org
- Showcase of NWB files for testing with NWB Explorer: https://github.com/OpenSourceBrain/NWBShowcase


