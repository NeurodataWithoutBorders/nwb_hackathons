Back to [Projects List](../../README.md#ProjectsList)

![Mocked up widgets](https://github.com/tarelli/geppetto-nwbexplorer/raw/master/styles/images/nwbExplorer.png)

## Key Investigators

- Matteo Cantarelli ([MetaCell](http://metacell.us))
- Giovanni Idili ([MetaCell](http://metacell.us))

# Project Description

Building on the [preexisting visualisation for NWB1](http://live.geppetto.org/geppetto?load_project_from_id=18) based on [Geppetto](http://www.geppetto.org) we are building an application that can be used by scientists to explore the content of NWB files. Reusing exisiting Geppetto widgets the focus is to build an application that can expose visualisations and workflows that can be useful for scientists.

## Objective

1. Objective A. Create a Django based Geppetto application for NWB Explorer - COMPLETED
1. Objective B. Create a NWB Model Interpreter which uses PyNWB - COMPLETED
1. Objective C. Hook up preexisting frontend to visualise content of NWB2 file - COMPLETED

## Approach and Plan

1. Create application skeleton
1. Explore PyNWB API and prototype the model interpreter
1. Extract metadata and traces

## Progress and Next Steps

### [Kanban board for all present and future tasks](https://waffle.io/tarelli/nwb-explorer)

The application is [here](https://github.com/tarelli/nwb-explorer), the geppetto extension is [here](https://github.com/tarelli/geppetto-nwbexplorer).

The first step after creating the skeleton was to hook up mocked up images for some target plots inside widgets to quickly provide a visual proof of concept. 

![Mocked up widgets](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/mockupPlots.png)

Then we implemented a Geppetto Model Interpreter using PyNWB and few tests to test the read API. We used the model interpreter to fetch some traces and reused preexisting Geppetto components to visualize the variables.

![Variables List](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/someVariables.png)

and plot them:

![Real plots](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/realPlots.png)

Short animation:

![Real plots](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/nwbexplorer.gif)

### Simulation output (Using NWB2 extension from Ben and Kael)

We extended the model interpreter to work with the extension Ben and Kael created to store the simulation output. We can now also plot simulation outputs stored using NWB. Here we are plotting the membrane potential for two different cell somas.

![Sim plots](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/sim1.png)
![Sim plots](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/sim2.png)
![Sim plots](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/sim3.png)

# Previous version using a Java backend and NWB1

![NWB1](https://github.com/NeurodataWithoutBorders/nwb_hackathons/raw/master/HCK04_2018_Seattle/Projects/NWBExplorer/nwbExplorer.png)

# Background and References

- Source code: https://github.com/tarelli/nwb-explorer + https://github.com/tarelli/geppetto-nwbexplorer
- Documentation: https://docs.geppetto.org
- Tests: https://github.com/tarelli/nwb-explorer/tree/master/tests

