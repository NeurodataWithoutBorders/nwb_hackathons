[:rewind: Back to the projects list](../../README.md#ProjectsList)

# Review and refine ICEphys Metadata extension

## Key Investigators

* Oliver Ruebel (LBNL)
* Ryan Ly (LBNL)
* Thomas Braun (byte physics)
* Pam Baker (Allen Insititute for Brain Science)
* Liviu	S.	(Laboratory of Neural Microcircuitry, EPFL / Blue Brain Project, EPFL)
* Shreejoy Tripathy (University of Toronto)
* Benjamin Dichter (Ben Dichter LLC)
* ...

## Project Description

Review and refine the proposed extension for ICEphys.

## Objectives

* Evalute suitability of the proposed extension for ICEphys for various use cases
* Identify challenges 
* Refine proposal
* Fix known issues

## Approach and Plan

* Implement fixes for reported issues
* Convert ICEphys files from different labs using the extension to evaluate suitability of the extension
* Have working group to review and refine the proposal 
* Make extension pip installable
* Add extension to the NDX Catalog

## Progress and Next Steps

* Released ``ndx-icephys-meta`` extensions on PyPi https://pypi.org/project/ndx-icephys-meta/
* Submitted ``ndx-icephys-meta`` extension to the ndx-catalog
* Reviewed extension with developers and users as part of the breakout session and closing discussions https://neurodatawithoutborders.github.io/nwb_hackathons/HCK07_2020_Seattle/projects/breakout_icephys/
* Created [milestones](https://github.com/oruebel/ndx-icephys-meta/milestones): 
  1) ``Release V.0.2.0`` that includes all changes targeted before integration with NWB 
  1) ``Future`` which includes proposals for future changes 
* Identfied several changes for the extensions that should be implemented before merging the extension with NWB, described below.

### Changes identified as part of the hackathon

* Add separate ``stimulus`` and ``response`` tables that the ``intracellular_recordings`` table in turn references. See https://github.com/oruebel/ndx-icephys-meta/issues/31
* Define more descriptive names for the tables to more clearly communicate the purpose of the different tables and avoid existing terms with ambigious definitions in the community. See https://github.com/oruebel/ndx-icephys-meta/issues/32 Specifically:

  1) ``intracellular_stimulus``  (new, see #31)
  1) ``intracellular_response`` (new, see #31)
  1) ``intracellular_recordings`` (remain as is)
  1) ``sweeps`` ---rename to---> `` simultaneous_recordings``
  1) ``sweep_sequence``  ---rename to---> ``sequential_recordings``
  1) ``runs`` ---rename to ---> ``repetitions``
  1) ``conditions`` ---rename to---> ``experimental_conditions``

* Add ``stimulus_type`` coluns to the ``sequential_recordings`` (a.k.a, ``sweep_sequences`` table)
* Refine ``add_intracellular_recordings`` function to make arguments optional and add error checks. See https://github.com/oruebel/ndx-icephys-meta/issues/34
* Add documentation for entering time slices for ``add_intracellular_recordings``. See https://github.com/oruebel/ndx-icephys-meta/issues/35
* Avoid the use of the ``ic`` prefix in the API as it is ambigous with terminology used in the ICEPhys community. Use the prefix ``icephys`` instead. See https://github.com/oruebel/ndx-icephys-meta/issues/36

### Next steps

* The goal is to implement all changes for https://github.com/oruebel/ndx-icephys-meta/milestone/1 prior to integration with NWB
* Once implemented and tested the extension should be merged with NWB
* The goal is to complete all changes within the next 2 weeks and complete merging of the changes with NWB propoer within the next 4 weeks

### Follow-up

As part of the discussions several topics for future follow-up proposals to further refine the management of icephys metadata have been identified. These are currently managed as part of https://github.com/oruebel/ndx-icephys-meta/milestone/2

* Add the ability to define custom tables that branch of the existing hierarchy. E.g., see https://github.com/oruebel/ndx-icephys-meta/issues/24 This topic introduces a great deal of flexibility and requires further review of use-cases and impact. 
* Refactor strategy for storing large collections of ICEphys recordings with the goal to reduce the number of objects required in a file. One main goal here would be to optimize performance and reduce the need for iteration over large numbers of objects. This issue is also related to this https://github.com/oruebel/ndx-icephys-meta/issues/17
* Wrap stimulus/response columns to improve rendering and potentially improve performance by delaying resolution of references. See laos in part https://github.com/oruebel/ndx-icephys-meta/issues/23
* Add ``stimulus_types`` table for describing the stimulus types. See https://github.com/oruebel/ndx-icephys-meta/issues/37

## Materials

* Proposed extension: https://github.com/oruebel/ndx-icephys-meta
* [Extension proposal document](https://docs.google.com/document/d/1cAgsXv26BmQoVfa7Greyxs0oc4IGH-t5aJsm-AwUAAE/edit)

## Background and References

* ...

