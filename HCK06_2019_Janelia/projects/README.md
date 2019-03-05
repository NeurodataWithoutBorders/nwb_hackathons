[:rewind: Back to main page](../README.md)

## What should my hackathon project look like?

Projects may span a broad range of topics, e.g., integrating new data with NWB:N, developing new features for PyNWB, exploring new problems, or creating documentation. Design your project in a way that:
  1. You can make significant progress during the hackathon (i.e., in ~1 day). This also means that you should come prepared for the hackathon. For example, if your project is about integrating data with NWB:N then you should **a)** know the data, **b)** ideally have scripts for reading the data in Python already preparted, and **c)** bring the data with you to the hackathon.
  1. The project is **a)** relevant to NWB:N and **b)** useful either as is or be something that you or someone else can build on after the hackathon 
  
### Does everyone need to have their own project?

Everyone should be part of a project, but not everyone must have their own project. Hacking in teams is fun!

## Project Suggestions
You are free to come to this event with your own ideas for a project, but if you want some inspiration, here are some areas we have identified where we could use some help:

### pynwb

* **aad default `ProcessingModule`s**: see [nwb-schema issue](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/249)

* **Schema validator**: We need a way to ensure that the schema yaml files follow the schema language of HDMF. This will be particularly useful as part of an extension sharing infrastructure, where users will be creating these yaml files and we would like to validate them before sharing them with the community. We think JSON-schema might be an appropriate tool for this.

* **[Neo](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3930095/) support**: Neo is a community standard for representing neural data in memory that several analysis and visualization tools use. We would like to have methods that convert from `pynwb` objects to `neo` objects:

| `pynwb`|  `neo`|
| --- | --- |
| `TimeSeries`| `AnalogSignal`, `AnalogSignalArray`, or `IrregularlySampledSignal`|
| `SpikeEventSeries`| `Spike`|
| `Units.spike_times`| `SpikeTrain`|
| `AnnotationSeries`| `EventArray`|
| `trials`, `epochs`| `EpochArray`|

* **Nix support**: Nix is another neural data standard, and it would be useful to convert back and forth between NWB:N and Nix.

* **Exdir backend**: While NWB:N and `pynwb` were designed to support multiple backends, the only one currently implemented is HDF5. Exdir is a specification for using files and folders in a structure similar to HDF5, and would be an ideal candidate for an alternative backend for NWB:N. See issue [here](https://github.com/NeurodataWithoutBorders/pynwb/issues/629).

* **Data visualization in Jupyter notebook widgets**: This would be a fun little project where you could take specific neurodata_types and create data visualizations. Bonus points if they are interactive Jupyter widgets. Ideal candidates: `pynwb.misc.Units` table, `pynwb.misc.AnnotationSeries`

* **Support for regular ontology**: See previous work [here](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/1)

* **Add [ONE](https://ibllib.readthedocs.io/en/latest/04_reference.html#open-neurophysiology-environment) API**

* **DataJoint support**

* **Add support for other analysis/visualization packages**

### matnwb

* **Continuous Integration (CI)**: CI is a tool for running tests automatically every time you merge a pull request, which makes sure the tests and up-to-date and prevents the addition of bugs. We have this working in pynwb, and it would be great to also have this working in matnwb.

* **Data compression**: HDF5 has robust data compression capabilities, but matnwb cannot currently take advantage of them. We need a way to tell the neurodata_type constructors whether/how a dataset should be chunked and compressed. Issue [here](https://github.com/NeurodataWithoutBorders/matnwb/issues/50). See [the pynwb implementation of this](https://pynwb.readthedocs.io/en/stable/tutorials/general/advanced_hdf5_io.html#sphx-glr-tutorials-general-advanced-hdf5-io-py) for inspiration.

* **Data append**: see issue [here](https://github.com/NeurodataWithoutBorders/matnwb/issues/109)

* **Support MATLAB table**: see issues for [in](https://github.com/NeurodataWithoutBorders/matnwb/issues/98) and [out](https://github.com/NeurodataWithoutBorders/matnwb/issues/111)

* **DataJoint support**

* **Support for other analysis/visualization packages**


### Data acquisition

**ScanImage**, **TDT**, **Plexon**, **OpenNeurophys**, etc.


## How to create a new project

When you are ready, create a new project by creating a new `README.md` file in a new subfolder of the [projects](.) folder using the provided [project description template][project-description-template] and add your project to the project list in the [PROJECTS.md](PROJECTS.md) file. Step-by-step instructions for creating a new project using GitHub are:

1. Open [project description template][project-description-template] and copy its full content to the clipboard
1. Go back to the [projects](https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK06_2018_Janelia/projects) folder on GitHub
1. Click on "Create new file" button
1. Type `YourProjectName/README.md`
1. Paste the previously copied content of project template page into your new `README.md`
1. Update at least your project's **title**, **key investigators**, and **project description** sections
1. Add a link to your project to the [project list](PROJECTS.md)

Note: some steps above may require creating a [pull request](https://help.github.com/articles/creating-a-pull-request/) until your account is given write access.

[project-description-template]: https://raw.githubusercontent.com/NeurodataWithoutBorders/nwb_hackathons/master/HCK06_2018_Janelia/projects/template/README.md
