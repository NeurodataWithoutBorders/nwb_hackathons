[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Fieldtrip Integration

## Key Investigators

Steffen Buergers (University of Birmingham)

Jens Klinzing (Princeton University)

Tara van Viegen (Princeton University)

## Project Description

Convert data structures in FieldTrip format to NWB format and vice versa. 

## Objectives

1. Read-in of NWB data in Fieldtrip
2. Export to NWB data format 

## Approach and Plan

1. Understand data formats properly 
2. Read in NWB Header information (ft_read_header)
3. Read in NWB LFP data (ft_read_data)
4. Read in NWB LFP metadata (ft_preprocessing, ft_read_event)
5. Read in NWB spike data (ft_read_spikes)
6. Write NWB data to Fieldtrip format

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planning to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

Example datasets: both ephys and calcium imaging
https://www.nwb.org/example-datasets/
...incl. a small reference dataset: https://drive.google.com/drive/folders/1g1CpnoMd9s9L-sHBWVyklp3-xJcLGeFt

NWB:N 2.0 Reference paper
https://www.biorxiv.org/content/10.1101/523035v1.full.pdf

NWB:N 2.0 Matlab API b
https://github.com/NeurodataWithoutBorders/matnwb

Fieldtrip datatype: Raw data
http://www.fieldtriptoolbox.org/reference/ft_datatype_raw/

Fieldtrip datatype: Spike data
http://www.fieldtriptoolbox.org/reference/ft_datatype_spike/



Potential issues:
1
The Fieldtrip data format seems not to allow units shared across contacts (see https://github.com/fieldtrip/fieldtrip/issues/721#issuecomment-603080632). It allows several units per contact (described in spike.unit which contains one integer for each channel and spike in that channel.

2
Dealing with different sampling rates. Comment Jan Mathijs: "...build in some glue-code in ft_read_header that 1) only selects the 'cont' type channels for further processing, and 2) then uses the majority Fs (by default). This would of course only work if the 'proper' LFPs are in the majority (as compared to the 40kHz cont-channels)"



