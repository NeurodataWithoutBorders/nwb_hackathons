[:rewind: Back to the projects list](../../README.md#ProjectsList)

# NWB:N Jupyter widgets

## Key Investigators

- Matt McCormick (Kitware)
- Ben Dichter (LBL)

## Project Description

Visualize cortical surfaces from NWB:N in an interactive [Jupyter
widget](https://jupyter.org/).

## Objectives

- When browsing a NWB:N file with nwbwidgets in Jupyter and an ECoG cortical
  surface is encountered, a 3D, interactive visualization of the surface is
  available.

## Approach and Plan

1. Get NWB ECoG data
2. Reformat for display as a mesh with itk-jupyter-widgets / vtk.js
3. Implement `show_` function for cortical functions in nwb-jupyter-widgets
4. Add support for cortical electrodes.

## Progress and Next Steps

During the hackathon, we made considerable progress on the NWB Jupyter widgets
for visualizing NWB:N behavioral files from the Allen Institute:

![Mouse Behavior Stimulus Images](https://i.imgur.com/B99gh81.gif)

We made some progress on the cortical surface visualization. We will follow up
with this effort in the [nwb-jupyter-widgets Issue
Tracker](https://github.com/NeurodataWithoutBorders/nwb-jupyter-widgets/issues).

## Materials

- [NWB extension for ECoG data](https://github.com/bendichter/nwbext_ecog)1
- [Example visualization in MayaVI](https://github.com/ChangLabUcsf/img_pipe/blob/master/img_pipe/plotting/ctmr_brain_plot.py)

## Background and References

- Source code: https://github.com/NeurodataWithoutBorders/nwb-jupyter-widgets
- Test data: EC125.nwbaux
