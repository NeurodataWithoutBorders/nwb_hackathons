[:rewind: Back to the projects list](../../README.md#ProjectsList)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Integrate NWB:N with RAVE

![RAVE visualizations via data imported from NWB format](https://raw.githubusercontent.com/dipterix/instrave/master/img/mainapp/ravedemo.gif)

* Check this video 
https://youtu.be/h_W9FyHKokA

* File to convert NWB to RAVE (Alpha version)

[https://raw.githubusercontent.com/beauchamplab/rave/dev-0.1.6.1/inst/third_party/NWB/nwb_import.R](https://raw.githubusercontent.com/beauchamplab/rave/dev-0.1.6.1/inst/third_party/NWB/nwb_import.R)

## Key Investigators

- Zhengjia Wang (Baylor College of Medicine/Rice University)
- Michael S. Beauchamp 

## Project Description

The goal of this project is to create “R” code that will allow our ECOG package, RAVE,
to read in (as a start) voltage traces from NWB files.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->
Support importing NWB format and load `Subject`, `epoch`, and `LFP` into `RAVE` preprocess pipeline.
<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->

## Approach and Plan


Create scripts to import `subject`, `analogtraces`, `cortical surface`, `electrode`, and `trial`


## Progress and Next Steps

1. [Done] Make clear about NWB basic structure
2. [May 15] Import NWB to RAVE


## Materials

### NWB to RAVE Converter

[NWB Converter to RAVE (Test script)](https://raw.githubusercontent.com/beauchamplab/rave/dev-0.1.6.1/inst/third_party/NWB/nwb_import.R)


### NWB ECoG extension

[https://github.com/bendichter/nwbext_ecog](https://github.com/bendichter/nwbext_ecog)

### Installations

#### Install `nwbext_ecog`

In terminal, 
```
pip install git+https://github.com/bendichter/nwbext_ecog
```

#### Install R and Rstudio

Open links below and install them according to your platform.

* [R](https://cran.r-project.org/) 
* [RStudio](https://www.rstudio.com/products/rstudio/download/)

#### HDF5 library in R

In R, [hdf5r](https://github.com/hhoeflin/hdf5r) provides IO for HDF5 files. To install it,

```
install.packages('hdf5r')
```

#### Install `RAVE`:

First, install [R](https://cran.r-project.org/) and [RStudio](https://www.rstudio.com/products/rstudio/download/)

Open Rstudio, type the following command

```r
install.packages('devtools')

# Install RAVE dev version
devtools::install_github('beauchamplab/rave@dev-0.1.6')

# Install builtin modules
devtools::install_github('beauchamplab/ravebuiltins')
```


<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

-  Web page for RAVE: [https://openwetware.org/wiki/Beauchamp:RAVE](https://openwetware.org/wiki/Beauchamp:RAVE)
-  GitHub site for RAVE: [https://github.com/beauchamplab/rave/tree/master#rave](https://github.com/beauchamplab/rave/tree/master#rave)



