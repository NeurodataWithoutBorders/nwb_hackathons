[:rewind: Back to main page](../README.md)

## What should my workshop project look like?

Projects may span a broad range of topics, e.g., converting data to NWB, integrating a software tool with NWB, working through the NWB online tutorials, developing new features for PyNWB/MatNWB, and creating documentation.

Design your project in a way that you can make significant progress during the workshop (i.e., in ~2 days). This also means that you should come prepared for the workshop. For example, if your project is about converting data to NWB, then you should know the data and ideally have scripts for reading the data in Python or MATLAB already working.

Suggestions for projects:
* convert some of your or a collaborator’s data to NWB
* convert data from a public archive to NWB
* integrate a software tool with NWB
* work through NWB online tutorials
* practice using NWB-compatible tools on publicly available NWB data, e.g., on [DANDI](https://dandiarchive.org/)

We ask that you create a project page with a description of the goals of your project. We will use these pages to connect people who are working on similar projects (e.g. converting data from the same acquisition system) and follow your progress.

## Create a new project page

Create a new project page by creating a new `README.md` file in a new subfolder of the [projects](https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK09_2020_Remote/projects) folder using the provided [project description template][project-description-template] and add your project to the project list in the [PROJECTS.md](PROJECTS.md) file. Step-by-step instructions for creating a new project using GitHub are:

1. Open [project description template][project-description-template] and copy its full content to the clipboard.
1. Go to the [projects](https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK09_2020_Remote/projects) folder on GitHub.
1. Click the "Add file" > "Create new file" button (at the top-right of the page).
1. Type `YourProjectName/README.md` as the new file name. Your project name should not have any spaces.
1. Paste the previously copied content from the project template page into your new `README.md` Markdown file.
1. Update at least your project's **title**, **key investigators**, and **project description** sections. Note that the syntax \<-- text --> denotes comments in Markdown format.
1. Click the "Propose new file" button at the bottom of the page.
1. On the right side of the next page, click the green "Create pull request" button to open a pull request.
1. On the next page, click the "Create pull request" button. After an administrator reviews and merges your pull request, the workshop website will be updated.

If you have any questions, please ask us on the NWB Slack workspace: https://bit.ly/nwb-slack

[project-description-template]: https://raw.githubusercontent.com/NeurodataWithoutBorders/nwb_hackathons/master/HCK09_2020_Remote/projects/template/README.md

## Prepare for your workshop project

Before the workshop, please install the Python or MATLAB software for NWB: 
  * PyNWB (Python): https://pynwb.readthedocs.io/en/stable/getting_started.html
  * MatNWB (MATLAB): https://neurodatawithoutborders.github.io/matnwb/
