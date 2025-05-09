# Conversion of Spike2 data into NWB

## Key Investigators

1. Deepti Mittal (participant at hackathon)
2. Rebecca Mease/Alexander Groh (PIs)
3. Ross Folkard

## Project Description

* Data were obtained from anesthetized mice.
* Data acquistion software : Spike2
* Spike sorting tool - Kilosort2
* **NEED PROBE GEOMETRY?**

## Objectives

1. Import silicon probe electrophysiology data collected with Spike2 into NWB format. Is it possible to convert .smrx or .mat file directly to NWB or are there any intermediate steps involved? if possible, We would like to import data files from SPIKE2 into Python and later to NWB. 
2. Establish consistent import of metadata about experiment (this should be a more-or-less common tool across the group, regardless of acquisition system).
3. Establish comparative spike sorting with SpikeInterface (tentatively, kilosort2 and klusta)
4. Understand how to access and edit trial information.
5. Understand how to access units' waveform information, do offline processing/categorization, then write results back to NWB
6. Establish restricted backwards-compatibility for time-consuming analysis that is already done (e.g. spike curation with Phy, post-hoc trigger-detection and trial definition)

## Approach and Plan

* [ ] Develop template for metadata and file creation. 

  _Preferably Python? Probe, histology, animal information, opto/chemogenetic information, sensory stimulus, experimenter manipulations (experimental model)_

* [ ] Import raw .smrx file (time-series data) to NWB. (To begin with,  use Spike2 to export data from the .smrx file to a  .mat file, then import the Matlab file into Python.)

 Include all channels (command stimuli and recorded stimuli if relevant) Animal state read-outs (respiration, temperature, heart beat)._

* [ ] Import electrophysiology experimental trial data to NWB 

  _Either from s2rx (?) file (preferable) OR from Conditions file in \*analysis.mat_

  * [ ] _Also custom user-defined trial inputs_

* [ ] Import data into SpikeInterface

  _Is this best to do with data already in NWB format? Or directly from Spike2 format_

  _What about .bin files that we already have from kilosort2? Are they generic enough to be used by SpikeInterface, or does it do its own conversion to farm out to many spike-sorting algorithms? Consider outputting a downsampled LFP directly from SpikeInterface._

* [ ] Understand how to do basic comparison of two spike-sorting algorithms, output results to NWB
  * [ ] _get two spike sorters running _
  * [ ] _basic comparison/breakdown_
  * [ ] _output to NWB_
  * [ ] _understand/document how different curation sessions are handled._
* [ ] Access clusterwaveform information via python and matlab stored in NWB.

## Progress and Next Steps

Will be updated later..

## Materials

Will be updated later..

## Background and References

Will be updated later..


