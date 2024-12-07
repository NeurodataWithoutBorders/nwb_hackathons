[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Query and complex indexing for NWB data

## Key Investigators

Andrew Tritt (LBNL)
Tom Davidson (UCSF)
Nile Graddis (AIBS)

## Project Description

Add functionality to support complex slicing.

## Objectives

Determine implementation plan for query/complex slicing in NWB

## Approach and Plan

1. Add ability to specify dimension scales - [issue](https://github.com/NeurodataWithoutBorders/pynwb/issues/626)
2. Add ability to copy [Containers in HDMF](https://hdmf.readthedocs.io/en/latest/hdmf.container.html#hdmf.container.Container)- [issue](BROKEN)
3. Add \_\_getitem\_\_ to [Query class in HDMF](https://hdmf.readthedocs.io/en/latest/hdmf.query.html#hdmf.query.Query)
    * may need to rewrite Query to be a class that takes and performs slices on a *target* e.g. TimeSeries
    * this will be the helper class that executes the query: 
      ```python
      ts = DecompositionSeries(...)
      ts.q[Mask(...), 'loc == CA1', 'name == theta']
      ```
4. Decide on name for and add defined-over/domain/support/observation-intervals to [TimeSeries class in PyNWB](https://pynwb.readthedocs.io/en/latest/pynwb.base.html?highlight=pynwb.base#pynwb.base.TimeSeries)


5. Add abstract Mask class to HDMF
    * Mask should be resolved from a query and a the values to which it applies, and should return a list of `bools`, and the new values to which it applies. Example usage:
      ```python
      new_timestamps, bool_mask = mask.resolve(timestamps)
      ```
    * Make a TimeMask object that operates on timestamps, and is aware of defined-over/domain/support/observation-intervals
    
6. Add a class to represent list of non-overlapping intervals
    * needs functionality for *and* and *or*



## Progress and Next Steps

We made good progress on determining what features and methods need to be implemented. The next step is to move these into GitHub as issues, and start writing code.

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
