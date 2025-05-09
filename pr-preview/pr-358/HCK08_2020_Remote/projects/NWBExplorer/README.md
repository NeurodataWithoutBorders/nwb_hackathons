[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Visualizing contents of NWB 2 files with NWB Explorer and Open Source Brain 

## Key Investigators

- Padraig Gleeson (UCL)
- Matteo Cantarelli (MetaCell)
- Filippo Ledda (MetaCell)

## Project Description

[Open Source Brain](http://opensourcebrain.org) is an open source, web-based resource for visualising, simulating and 
disseminating standardised models of neurons and circuits from many brain regions including the neocortex, cerebellum 
and hippocampus. Over the next three years we will be extending OSB to include integrated visualisation and analysis of 
the experimental (anatomical, electrophysiological, imaging and behavioural) data used to build and test such models, 
alongside the models themselves. By closing the loop between data and models, this new version of OSB will provide 
accessible models of brain function that can be reused for new scientific questions, by the wider neuroscience community. 

At the 2018 Seattle Hackathon, a first step was made towards this vision with the 
[NWB Explorer project](https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK04_2018_Seattle/Projects/NWBExplorer). NWB Explorer is based on the 
[Geppetto platform](http://www.geppetto.org/), as is the OSB 3D visualisation functionality. It is planned that NWB Explorer will be available both as:

- An **integrated component of OSB**, allowing visualation of shared NWB content (e.g. from Figshare) through the browser without installing any local software
- A **standalone desktop application** for visualising the contents of local NWB files (see [here](https://github.com/MetaCell/nwb-explorer))

An instance of NWB Explorer can be accessed here: **[http://nwbexplorer.opensourcebrain.org](http://nwbexplorer.opensourcebrain.org/)**, and some background and example data sets can be seen here: https://github.com/OpenSourceBrain/NWBShowcase

![nwbexplorer](https://user-images.githubusercontent.com/39889/67516734-24c1e380-f66f-11e9-9fba-5151118f5e4d.gif)

Our primary goal at this hackathon will be to gather existing NWB:N v2 datasets to check and improve compatibility with the basic parser of NWB Explorer, determine scientifically useful workflows and the components necessary to support them, and develop a basic widget for exposing in a readable fashion the structure of an NWB file.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->
1. Test the existing NWB Explorer with multiple data sets
2. Get initial user/usability feedback
3. Collect public datasets for (automated) testing of future versions of NWB Explorer
4. Determine scope of current/pending public NWB dataset releases (i.e. what types of data will be included and should be prioritized, image stacks, videos, etc.)

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
1. Exchange NWB files with other participants
2. Get other attendees to try out the [desktop](https://github.com/MetaCell/nwb-explorer) & [online version of NWB Explorer](http://nwbexplorer.opensourcebrain.org/)
3. Get other attendees to add example datasets/conversion scripts to https://github.com/OpenSourceBrain/NWBShowcase 
(or [add issue](https://github.com/OpenSourceBrain/NWBShowcase/issues)).
4. Get timelines of labs' data release plans; assess attendee demand for functionality in NWB

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->
See https://github.com/MetaCell/nwb-explorer/milestone/5 and https://github.com/MetaCell/nwb-explorer/issues.

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
- NWB Explorer source : https://github.com/MetaCell/nwb-explorer
- Online version of NWB Explorer: http://nwbexplorer.opensourcebrain.org
- Open Source Brain: http://opensourcebrain.org
- Showcase of NWB files for testing with NWB Explorer: https://github.com/OpenSourceBrain/NWBShowcase
- 2018 Hackathon NWB Explorer project: https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK04_2018_Seattle/Projects/NWBExplorer

