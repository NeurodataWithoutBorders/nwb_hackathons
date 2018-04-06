Back to [Projects List](../../README.md#ProjectsList)

# SlicerDicer

## Key Investigators

- Doruk Ozturk (Kitware)
- Ben Dichter (Stanford)
- Andrew Tritt (Berkeley Lab)
- Oliver Ruebel (Berkeley Lab)

# Project Description

The SlicerDicer is a Python layer that is intended to allow scientists to inspect the contents of an NWB file, and to pull out relevant data fitting specific time slices or stimuli (the slicing and dicing). It provides an API that can be used by visualization or analysis tools. Currently the SlicerDicer is also using h5py for prototyping possible enhancements to the PyNWB read API.

## Objective

1. Objective A. Generate a tree from an NWB file which will include groups, datasets, soft and external links. 
2. Objective B. Provide an API with unified data accessing capabilities to datasets.
```
GET('/stimulus/presentation/natural_movie_one_stimulus/data[1000:1100])
```
3. Objective C. Include NWB specific helper methods for narrowing down scope of HDF, e.g. create helper methods that are NWB specific.

## Approach and Plan

1. Currently planning to use a combination of h5py, h5serv and hdf5-json as building blocks to achieve our goals.
2. Once the API is in place, ESV will use slicer-dicer as a mediator to talk to NWB files.
3. Need a lot of diverse NWB files and use cases to provide meaningful NWB specific helper methods.

## Progress and Next Steps

After seeing the query API presented by Andrew and Oliver in the Read API breakout session, the path forward here is to integrate the SlicerDicer with the query API, to make sure what data we need for QC and exploratory visualizations of NWB files are provided by the query API. Further, we will push on the idea of providing a higher level API on top of the Read API, that speaks to neuroscience domain concepts but hides some of the software complexity of the lower level PyNWB implementation details.
