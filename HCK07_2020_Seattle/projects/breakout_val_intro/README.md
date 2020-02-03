[:rewind: Back to the projects list](../../README.md#breakout-sessions)

Currently edited online in https://hackmd.io/z6GJrRSdRySMo1LAppabJw


<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

#  Validation and Introspection

**Session Chair:** Yaroslav Halchenko (Dartmouth College) and Thomas Braun (byte physics e.K.)

<!-- Add a short paragraph describing the topic and breakout session. -->

Needs, requirements and expectations for validation and introspection of NWB files

## Participants

* Yaroslav Halchenko (Dartmouth College)
* Thomas Braun (byte physics e.K.)
* Oliver Ruebel (LBNL)
* ...

## Objectives


<!-- Briefly describe the objectives of the breakout session. What would you like to achive?-->

* Identify requirements, use cases, and expectations for validation of NWB files
* Identify requirements, use cases, and expectations for light-weight introspection of NWB file (via PyNWB)
* ...

### Proposed discussion topics

Participants should add topics of possible interest for discussion here

* Discuss open validation issues: https://github.com/NeurodataWithoutBorders/pynwb/issues/1160,
  * [validator fails for the extensions tutorial when namespace file provided
 #1058](https://github.com/NeurodataWithoutBorders/pynwb/issues/1058),
  * https://github.com/NeurodataWithoutBorders/pynwb/issues/836,
  * https://github.com/NeurodataWithoutBorders/pynwb/issues/1091,
  * https://github.com/NeurodataWithoutBorders/pynwb/issues/957,
  * https://github.com/NeurodataWithoutBorders/pynwb/issues/1162
* Implementation details of checking for extra fields (https://github.com/NeurodataWithoutBorders/pynwb/issues/1162)

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Current state
<!--Populate this section as you are making progress before/during/after the hackathon-->

### Validation

pynwb provides validation of .nwb files to follow specific schema.  Could also be invoked from command line via `python -m pynwb.validate [FILES]` but at best should be invoked per each file separately since the whole process would fail as soon as the current file fails validation.

[dandi](https://github.com/dandi/dandi-cli/) `validate` (and also during `upload`) provide a way to validate files (delegates actual validation to pynwb) from command line:

```shell
$> dandi validate v2.0.1/test_*
...
v2.0.1/test_CurrentClampStimulusSeries.nwb: ok
v2.0.1/test_DecompositionSeries.nwb: 1 error(s)
  DynamicTable/colnames (processing/test_mod/LFPSpectralAnalysis/bands.colnames): incorrect type - expected 'text', got 'ascii'
v2.0.1/test_Device.nwb: ok
v2.0.1/test_DynamicTable.nwb: 1 error(s)
  Units/colnames (units.colnames): incorrect type - expected 'text', got 'ascii'
v2.0.1/test_ElectricalSeries.nwb: 1 error(s)
  DynamicTable/colnames (general/extracellular_ephys/electrodes.colnames): incorrect type - expected 'text', got 'ascii'
v2.0.1/test_ElectrodeGroup.nwb: ok
...
Summary: Validation errors in 14 out of 31 files
```


### Introspection

[dandi](https://github.com/dandi/dandi-cli/) `ls` provides easy way to see basic information about any .nwb file. For pre-v2 nwb files it would at least provide NWB version information.  E.g.:

```shell
$> dandi ls v2.0.1/test_Cluster*
PATH                             SIZE    IDENTIFIER            SESSION_DESCRIPTION                                   SESSION_START_TIME   NWB  ND_TYPES
v2.0.1/test_Clustering.nwb       17.8 kB TEST_Clustering       a file to test writing and reading a Clustering       1971-01-01/12:00:00  2.0b Clustering
v2.0.1/test_ClusterWaveforms.nwb 20.0 kB TEST_ClusterWaveforms a file to test writing and reading a ClusterWaveforms 1971-01-01/12:00:00  2.0b ClusterWaveforms, Clustering (2)
Summary:                         37.7 kB                                                                             1971-01-01/12:00:00>
                                                                                                                     1971-01-01/12:00:00<
```

## Progress and Next Steps

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
