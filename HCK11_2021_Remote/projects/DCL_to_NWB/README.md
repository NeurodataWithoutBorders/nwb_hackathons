[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Conversion of a multimodal dataset from the DCL into the NWB standard

## Key Investigators

- Dennis Segebarth (Institute of Clinical Neurobiology, University Hospital of Wuerzburg, Germany)
- Nina Schukraft (Institute of Clinical Neurobiology, University Hospital of Wuerzburg, Germany)
- Jérémy Signoret-Genest (Institute of Clinical Neurobiology, University Hospital of Wuerzburg, Germany)
- Philip Tovote (Institute of Clinical Neurobiology, University Hospital of Wuerzburg, Germany)

## Project Description

As part of a collaborative research center, the [CRC Retune](https://retune.science/), our goal is the conversion of animal research data into the NWB standard.
As an initial use-case, we are starting with the conversion of several multimodal datasets acquired in the [Defense circuits lab](https://www.defense-circuits-lab.com/).
The ultimate goal of this project is described in some more detail in [our GitHub repository](https://github.com/DSegebarth/DCL_to_NWB), 
where you can hopefully can also keep track of our progress in the following months.

For this *project* within the NWB user days, I´d like to get in touch with the developers to ask some more detailed questions (see below).

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

In this little project, I´d like to get some support from the developers for some issues we are currently facing:

1. Integration of externally stored files, specifically large movie files / or options to write files that may exceed the RAM.
2. How shall behavioral episodes be stored in the NWB file?
3. When reading a NWB file I wrote before, I keep running into issues with NWBwidgets & it would be great to fix this.
<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

All issues could be adressed quite quickly.

1. One argument was passed in excess, preventing the external link
2. The scored behavioral intervals were stored in a TimeInterval table 
3. I was using a `with` statement to read the file and called the nwb2widget outside of it. Since the data is only read on demand (and was in fact closed before that demand actually arised by calling the nwb2widget outside of the `with` statement), only metadata was displayed in the widget and everything else raised an error. Thus, omitting the `with` statement solved the issue.

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

Source code: [DCL_to_NWB](https://github.com/DSegebarth/DCL_to_NWB)

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
