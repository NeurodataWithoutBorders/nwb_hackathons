Back to [Projects List](../../README.md#ProjectsList)

# Write full project title here

## Key Investigators

- Andrew Tritt (Berkeley Lab)
- Oliver Ruebel (Berkeley Lab)
- Jean-Christophe Fillion-Robin (Kitware)

# Project Description

Define template and methods for sharing extensions.

## Objective

1. Document best practice for creating pynwb extensions
1. Document guidelines and core principles for creating extensions
1. Create a template of extension (e.g using cookiecutter)
1. Update existing extension to comply with the template

## Current Process/Tools
* **Existing tooling for documenting extensions**
    * [generate_format_docs.py](https://github.com/NeurodataWithoutBorders/nwb-schema/blob/dev/docs/utils/generate_format_docs.py) Python tool for creating Sphinx RST docs from the YAML/JSON sources of a format specification. This script is also used to generate the docs for the NWB core format but supports extensions as well.
    * [init_sphinx_extension_doc.py](https://github.com/NeurodataWithoutBorders/nwb-schema/blob/dev/docs/utils/init_sphinx_extension_doc.py) This is a helper script to setup a new Sphinx documentation for an extension
    * [render.py](https://github.com/NeurodataWithoutBorders/nwb-schema/blob/dev/docs/utils/render.py) This script is used to 1) extact object hierarchies from a specification YAML/JSON source (also supports HDF5 files) and 2) to plot the hierarchy using NetworkX. This module is used by `generate_format_docs.py` to create all the plots in the format documentation.
* **Template for extensions** * There is initial documentation for how to use the above scripts and a rough template for how to organize extensions in the PyNWB docs [here](http://pynwb.readthedocs.io/en/latest/example.html#documenting-extensions). This needs to be updated once we have decided on the actual template, moved and updated docuemtnation tooling etc. 
* **Existing tooling for writing extensions:** PyNWB implements and API for reading, writing, and creating format specifications in the NWB schema language. Existing documents describing how to write and use extensions in PyNWB are part of the `Examples` as well as `Tutorials` sections of the PyNWB docs:
  * http://pynwb.readthedocs.io/en/latest/example.html#extending-nwb
  * http://pynwb.readthedocs.io/en/latest/tutorials.html#extensions

## Approach and Plan

1. Discuss with teams having experience creating extensions
1. Consolidate documentation and tools supporting extension creation
    * **Known ToDo items**
        * Move the existing tooling out of the nwb-schema repo to an approbriate place in the PyNWB repo. This is to 1) make the tools more accessible, 2) add ability to do testing, 3) avoid copying of the scripts (currently `init_sphinx_extensions_doc.py` will copy the scripts because we don't have a good mechanism for installing the nwb-schema repo, which is for collecting documents and not sources)
        * Update render.py to use the PyNWB schema classes when constructing the hierarchy rather than custom dicts. This is mainly for consistency to make the code also easier to reuse in other places. 
        * Clean up the scripts and add more documentation. 
1. Create a template
1. Create document with guidelines for extensions (e.g., reuse types, avoid data denormatlization/dublication, names should be clear and consistent with the format etc.) and possibly a descision-tree to help folks navigate the process and make decisions in the design process.
1. Depending on progress on this project we may also want to create a Git-repo for sharing extensions (to be determined as part of the project)
1. Understand work required to support easy install of extensions (similar to `pip install nameOfExtension`). 
    * Define requirements and create list of options for how the installation of extensions should work (e.g., custom install tool as part of PyNWB, pip, etc.). Ultimately, install of extensions needs to be possible not just for PyNWB but also APIs for other languages (e.g. MatNWB). Ideally we'd have a consistent tooling for this but at least the extensions should live in a single location to avoid divergence of extensions.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Forum: https://github.com/orgs/NeurodataWithoutBorders/teams/YourSubTeam
- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data

