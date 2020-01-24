[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Convert, annotate, analyze, and co-cluster intracellular electrophysiology datasets collected across labs

## Key Investigators

Shreejoy Tripathy (University of Toronto)

## Project Description

Labs performing icephys are often delivering the same (or very similar) types of stimuli (e.g., steps, ramps, chirps, etc.). But labs have different ways of storing their data files (different formats and organization conventions) and have different ways of naming stimuli and groups of related stimuli.

We here aim to use NWB as a common language for storing icephys datasets and to adapt existing tools for annotating stimulus types and performing feature extraction. We aim to co-cluster datasets and recorded cells by feature similarity, similar to how is commonly done for single-cell transcriptomics datasets. 

While this project is ambitious in scope, we plan to make use of tools that have already been developed for these purposes.

## Objectives

1. Convert intracellular electrophysiological datasets provided by hackathon contributors to NWBv2 (if needed).
2. Annotate the usage of common stimulus protocols across datasets, making use of and extending the Allen Institute icephys stimulus ontology.
3. Extract features from icephys datasets using existing feature extraction libraries. This will likely require extending existing tools, like Allen Institute's IPFX toolbox, to accommodate greater variability of input datasets.
4. Co-cluster cells by electrophysiological feature similarity.

## Approach and Plan


## Progress and Next Steps


## Materials
1. Python based tools for converting icephys datasets to NWB [x_to_nwb](https://github.com/AllenInstitute/ipfx/tree/master/ipfx/x_to_nwb)
2. [icephys stimulus ontology](https://github.com/AllenInstitute/ipfx/blob/master/ipfx/defaults/stimulus_ontology.json)
3. [ipfx feature extraction library](https://github.com/AllenInstitute/ipfx)

## Background and References


