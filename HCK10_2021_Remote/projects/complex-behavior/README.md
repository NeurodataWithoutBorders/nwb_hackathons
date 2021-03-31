[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Complex Behavior

## Key Investigators

- Akshay Jaggi
- Talmo Pereira
- Arie Matsliah
- Kanishk Jain
- Jim Bohnslav
- Laurel Keyes

## Project Description

Write a set of basic neurodata types to cover commonly used behavioral data in novel complex behavioral quantification schemes

## Objectives

1. ndx-labels: both supervised and unsupervised behavioral labels for single- and multi- animal sessions
2. ndx-datatransforms: structuring matrix transformations (PCA, NMF, tSNE, etc.) and metadata
3. ndx-multi: allowing multi-animal coordination of NWB sessions. Likely will be an extension of objects like Subject

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps
1. [ndx-labels](https://github.com/ndx-complex-behavior/ndx-labels): Consolidated ndx-labels and ndx-datatransforms into one extension called ndx-labels. We wrote up a [simple schematic](https://docs.google.com/presentation/d/1fm3O5euwQjAbvewN22YEt9INxPaSViszgw43MfDkZlI/edit?usp=sharing) for how to relate a behavioral video to a general label class and how to relate a general label class to a potential learned, low-dimensional "representation" of the raw data (say PCs or tSNE factors). We spec'd this schema, wrote a roundtrip test, and finished with a working example .py file. Potential extensions include making the representation class more flexible to include relevant metadata for certain representations (say PC loadings / eigenvalues), writing unit tests, testing that labels and representations could be used with neural data instead of a video, and more ideas. 
2. [ndx-pose](https://github.com/ndx-complex-behavior/ndx-pose): Extended ndx-pose to include support for part grouping procedures for creating animal instances and support for animal identity estimation in multi-animal experiments. Wrote unit tests. Potential extensions include writing up a schema diagram for documentation, writing a round trip test, integrating this with ndx-labels, and more ideas. Special shoutout to Talmo for working on wrapping this up. 

## Materials

Overview Presentation: https://docs.google.com/presentation/d/1LFkAbY-lNrwpxQkO1J1S8lcBlJCF8kUQ8EJlSkTb-Z8/edit?usp=sharing

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
