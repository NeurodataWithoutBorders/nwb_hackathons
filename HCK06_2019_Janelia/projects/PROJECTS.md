## Assigned Projects

The lists below provide an overview of specific projects for which at least one or more attendees have signed up for to contribute to. Projects are collaborative in nature. If you are attending the hackathon and are interested in participating in any of the existing projets then please contact the team listed on the project page.

### User Days

* [Neuron model optimization](projects/neuronmodel)
* [Abf and Dat to NWB:N](projects/x_to_nwb)
* [Integrate neuron model optimization and simulation data with NWB:N](projects/neuronmodel)
* [Chang lab to NWB:N](projects/changlab_to_nwb)
* [Neuromodulation Research Center to NWB:N](projects/NMRC)
* [Integrate Thorlabs 2p calcium data into NWB](projects/kanoldLabNWB)
* [Tandon lab to NWB:N](projects/tandonlab2nwb)
* [Rutishauser lab to NWB:N](projects/RutishauserLab2NWB)
* [Lazy cross-file links](projects/lazy_cross_file_links)

### Developer Days

* [Integrate NWB:N with RAVE](projects/RAVE)
* [Integrarte ZARR with PyNWB/HDMF](projects/ZARR)
* [Evaluate avenues for NIX + NWB:N](projects/NIX)
* [NWB:N Jupyter notebook widgets](projects/JupyterWidgets)
* [NWB:N Explorer and Open Source Brain](projects/OSB_NWB_Explore)
* [Import data from acquisition systems](projects/AcquisitionSystemImporters)
* [Extension sharing](projects/ExtensionSharing)
* [Lazy cross-file links](projects/lazy_cross_file_links)

## Project Suggestions
You are free to come to this event with your own ideas for a project, but if you want some inspiration, here are some areas we have identified where we could use some help:

* **Python/PyNWB**

    * **Add default `ProcessingModules`**: see [nwb-schema issue](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/249)
    * **Schema validator**: We need a way to ensure that the schema yaml files follow the schema language. This will be particularly useful as part of an extension sharing infrastructure, where users will be creating these yaml files and we would like to validate them before sharing them with the community. This could be done using the HDMF data structures or JSON-schema.
    * **Alternate storage backends:** While NWB:N and `pynwb` were designed to support multiple backends, the only one currently implemented is HDF5. Possible options may be:
        * **Exdir:** See issue [629](https://github.com/NeurodataWithoutBorders/pynwb/issues/629)
        * **Zarr:** See issue [230](https://github.com/NeurodataWithoutBorders/pynwb/issues/230)
        * **Nix**: Nix is another neural data standard, and it would be useful to be able convert back and forth between NWB:N and Nix.
   * **Parallel I/O** Test and improve support for MPI parallel HDF5 I/O and create parallel I/O tutorial (see, e.g., https://github.com/NeurodataWithoutBorders/pynwb/pull/847)
   * **Visualization and documentation tools:**
       * **Documentation Utils**: Improve organization and visualizations of the documentation utils used to generate Sphinx docs and figures from the YAML schema files. See also https://github.com/NeurodataWithoutBorders/nwb-docutils
    * **Support for regular ontology**: See previous work [here](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/1). There is also ongoing work in this space by LBNL and AIBS. If you are interested in this please contact <oruebel@lbl.gov> .
    * **Add support for other data analysis/visualization/management packages**
        * **Add [ONE](https://ibllib.readthedocs.io/en/latest/04_reference.html#open-neurophysiology-environment) API**
        * **DataJoint support**
        * **[Neo](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3930095/) support**: Neo is a community standard for representing neural data in memory that several analysis and visualization tools use. We would like to have methods that convert from `pynwb` objects to `neo` objects:

| `pynwb`|  `neo`|
| --- | --- |
| `TimeSeries`| `AnalogSignal`, `AnalogSignalArray`, or `IrregularlySampledSignal`|
| `SpikeEventSeries`| `Spike`|
| `Units.spike_times`| `SpikeTrain`|
| `AnnotationSeries`| `EventArray`|
| `trials`, `epochs`| `EpochArray`|

* **MatNWB**
    * **Continuous Integration (CI)**: CI is a tool for running tests automatically every time you merge a pull request, which makes sure the tests and up-to-date and prevents the addition of bugs. We have this working in pynwb, and it would be great to also have this working in matnwb.
    * **Data compression**: HDF5 has robust data compression capabilities, but matnwb cannot currently take advantage of them. We need a way to tell the neurodata_type constructors whether/how a dataset should be chunked and compressed. Issue [here](https://github.com/NeurodataWithoutBorders/matnwb/issues/50). See [the pynwb implementation of this](https://pynwb.readthedocs.io/en/stable/tutorials/general/advanced_hdf5_io.html#sphx-glr-tutorials-general-advanced-hdf5-io-py) for inspiration.
    * **Data append**: see issue [here](https://github.com/NeurodataWithoutBorders/matnwb/issues/109)
    * **Support MATLAB table**: see issues for [in](https://github.com/NeurodataWithoutBorders/matnwb/issues/98) and [out](https://github.com/NeurodataWithoutBorders/matnwb/issues/111)
    * **DataJoint support**
    * **Support for other analysis/visualization packages**

* **Data acquisition**

    * **ScanImage**
    * **TDT**
    * **Plexon**
    * **OpenNeurophys**
    * ...
