[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Convert, annotate, and co-analyze icephys datasets

## Key Investigators

* Shreejoy Tripathy (University of Toronto)
* Jim Berg (Allen Institute)
* Csaba Foldy (University of Zurich)
* Thomas Braun (byte physics e.K.)

## Project Description

Labs performing icephys are often delivering the same (or very similar) types of stimuli (e.g., steps, ramps, chirps, etc.). But labs have different ways of storing their data files (different formats and organization conventions) and have different ways of naming stimuli and groups of related stimuli. 

We here aim to use NWB as a common language for storing icephys datasets and to adapt existing tools for annotating stimulus types and performing feature extraction. We aim to co-cluster datasets and recorded cells by feature similarity, similar to how is commonly done for single-cell transcriptomics datasets.

While this project is ambitious in scope, we plan to make use of tools that have already been developed for these purposes.

## Objectives

1. Convert intracellular electrophysiological datasets provided by hackathon contributors to NWBv2 (if needed).
2. Annotate the usage of common stimulus protocols across datasets, making use of and extending the Allen Institute icephys stimulus ontology. This objective is related to the subproject on [Stimulus representation and parametrization in NWB](https://neurodatawithoutborders.github.io/nwb_hackathons/HCK07_2020_Seattle/projects/stim_onto/).
3. Extract features from icephys datasets using existing feature extraction libraries. This will likely require extending existing tools, like Allen Institute's IPFX toolbox, to accommodate greater variability of input datasets.
4. Co-cluster cells by electrophysiological feature similarity.

## Approach and Plan
Goal: Develop a prototype end-to-end pipeline for converting historical, external lab icephys datasets to NWBv2, annotating the usage of stimuli using a shared stimulus ontology, performing ephys feature extraction, and co-clustering cells by similarity in extracted ephys features onto icephys reference atlases provided by the Allen Institute.

Approach: We will focus our prototype on single-electrode icephys datasets reflecting somatic current clamp experiments that have been collected using pClamp with outputted files in Axon Binary File format (ABF). We will focus our stimulus annotation and feature extraction efforts on long current step stimuli.

Plan:
1. Convert: Convert external icephys files to nwbv2, focusing on current clamp icephys datasets stored in ABF (from Shreejoy’s collaborators and Csaba)
2. Annotate: Fork the AIBS [icephys stimulus ontology](https://github.com/AllenInstitute/ipfx/blob/master/ipfx/defaults/stimulus_ontology.json) to accommodate sweep names and categories from external datasets. For the hackathon, we will focus on the usage of long step current injections. This step will be performed in conjunction with the related hackathon project on [Stimulus representation and parametrization in NWB](https://neurodatawithoutborders.github.io/nwb_hackathons/HCK07_2020_Seattle/projects/stim_onto/).
3. Extract: Load in converted nwbv2 datasets into the appropriate data structures needed for ipfx’s internal data structure, (ephys_data_set)[https://github.com/AllenInstitute/ipfx/blob/master/ipfx/ephys_data_set.py]. Then use ipfx's feature extraction libraries to perform feature extraction. This will likely require disabling QC checking for IPFX.
4. Co-cluster: Co-cluster cells by ephys similarity.

## Progress and Next Steps

## Materials
1. Python based tools for converting icephys datasets to NWB [x_to_nwb](https://github.com/AllenInstitute/ipfx/tree/master/ipfx/x_to_nwb)
2. [icephys stimulus ontology](https://github.com/AllenInstitute/ipfx/blob/master/ipfx/defaults/stimulus_ontology.json)
3. [ipfx feature extraction library](https://github.com/AllenInstitute/ipfx)

## Background and References


