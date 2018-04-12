[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Filter Read by Label

## Key Investigators

- Aaron Milstein (Stanford)
- Ivan Raikov (Stanford)
- Ben Dichter (Stanford)

## Project Description

We would like to define a standard way to associate data points in an NWB file with multiple user-defined categorical labels, and then be able to selectively read from a dataset just the data points that satisfy a boolean filter based on those labels. An example would be a dataset of UnitTimes containing spike trains recorded from an extracellular electrophysiology experiment. Each neuron in the dataset could be assigned a categorical label according to its 1) cell_type, 2) feature_selectivity (grid cell or head direction cell?), 3) active during sleep / wake?, etc. Then the user could read into memory the spikes from all cells that match a query for 'cell_type' == 'basket_cell', 'selectivity' == 'running_speed', 'behavioral_state' == 'sleep', e.g.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Create a CategoricalLabels specification for assigning categorical labels to cell_identifiers in a SpikeTimes NWB dataset.
2. Write a python function that takes in 1) a PyNWB SpikeTimes dataset object, 2) a newly-defined PyNWB CategoricalLabels object, and 3) a filter query in the form of a python dictionary with category_names as keys and lists of category_labels as values. Have it return a list of cell_ids that satisfy the filter, possibly with RangeReferences to the actual corresponding values in the data array.

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
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

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
