[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Hierarchical folder structure for HDFView 

## Key Investigators

- Liviu S. (Laboratory of Neural Microcircuitry & Blue Brain Project, EPFL)
- Andrew Tritt (Lawrence Berkeley National Laboratory)

## Project Description

Create an extension that generates a folder structure that mirrors the hierarchical tables from the [ndx-icephys-meta](https://github.com/oruebel/ndx-icephys-meta) extension.  
At the deepest level, add soft links to data in `/acquisition` and `/stimulus`.

This folder structure will look like this in HDFView:

```
/root  
  /view  
    /Electrode_01  
      /APWaveform  
      /Delta  
        /repetition_1  
          /stimulus  
            /VoltageClampStimulusSeries_01_soft_link  
            /VoltageClampStimulusSeries_02_soft_link  
          /response  
            /VoltageClampSeries_01_soft_link  
            /VoltageClampSeries_02_soft_link  
        /repetition_2  
        /repetition_3  
        /etc...  
      /FirePattern  
      /etc...
    /Electrode_02  
```      


## Progress and Next Steps

Main code written by the end of the hackathon. Testing and debugging needed.

