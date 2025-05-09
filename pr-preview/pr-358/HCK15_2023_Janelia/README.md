<img alt="NWB 2023 User/Developer Days Banner" src="images/event_banner.png">

# NWB User Days and Developer Days 2023

  * [Report](#report)
  * [Dates and Location](#dates-and-location)
  * [Registration](#registration)
  * [Logistics](#logistics)
  * [Organizing Committee](#organizing-committee)
    * [Additional Organizational Support](#additional-organizational-support)
  * [Resources](#resources)
  * [What to bring?](#what-to-bring)
  * [Objective](#objective)
  * [Agenda](#agenda)
  * [Projects](#projects)
  * [Code of Conduct](#code-of-conduct)
  * [Disclaimer](#disclaimer)
  
## Report

The final report for the 2023 NWB User Days and Developer Days is now available on GitHub ([PDF](report/Report___15th_NWB_and_User_and_16th_Developer_Days_2023.pdf)) ([LaTeX (on Overleaf)](https://www.overleaf.com/read/qsdtmzjnhwxn).

## Dates and Location

- **Dates:** July 24-29, 2023
  - **User Days:** July 24-26, 2023
  - **Developer Days:** July 27-29, 2023
- **Location:** [HHMI Janelia Research Campus](https://www.janelia.org/), 19700 Helix Dr, Ashburn, VA 20147,
  [Openstreetmap](https://www.openstreetmap.org/?mlat=39.0708&mlon=-77.4655#map=14/39.0708/-77.4655)
  [Directions](https://www.janelia.org/directions)
- **Meeting Rooms:** For the meeting we have two rooms. The main room is *Axon-Dendrite* and the breakout room is *Spectrum*.
  For details about the room locations see the [building map.](../HCK06_2019_Janelia/travel/janelia_room_plan_for_6th_nwbn_hackathon.pdf)

## Registration

Registration is now closed. If you would like to be added, please contact the organizers and we may be able to accommodate your request.

## Logistics

**Housing:** Housing will be provided onsite on the Janelia research campus. For details about transportation and logistics please see [here](https://www.dropbox.com/s/i2540enmapap05o/Janelia%20travel%20logistics.pdf?dl=0)

**Travel:** Travel support is not provided. Limited funds may be available to support attendee travel. Once attendance has been confirmed, we will contact you to collect additional information regarding your travel details.

* **User Days:** Attendees should plan to arrive Sunday afternoon and depart on Wednesday evening after the social or Thursday (depending on availability of flights). 
* **Developer Days:** Attendees should plan to arrive Wednesday evening to attend the joint social with User Days participants and depart Saturday afternoon after conclusion of the meeting. 

**Directions:** The Janelia Research Campus is located in Loudoun County, Virginia – just 30 miles from Washington, DC, and about eight miles north of Dulles International Airport (IAD). For directions see [https://www.janelia.org/directions](https://www.janelia.org/directions)


## Organizing Committee

**Site chair:** [Jakob Voigt](https://www.voigtslab.org/people)

**Program chair (User Days):**  [Oliver Rübel](https://crd.lbl.gov/divisions/scidata/mla/staff/oliver-ruebel/) and [Ben Dichter](http://bendichter.com/)

**Program chair (Developer Days):** [Oliver Rübel](https://crd.lbl.gov/divisions/scidata/mla/staff/oliver-ruebel/) and [Ryan Ly](https://crd.lbl.gov/divisions/scidata/mla/staff/ryan-ly/)

**Administrative Support:** [Janine Stevens](https://www.janelia.org/people/janine-stevens)

### Additional Organizational Support

- The Kavli Foundation
- Janelia HHMI

## What to bring?

* Bring any example data sets needed for your project with you to the hackathon. For any lab-specific data (i.e., 
  data not in NWB), you should know how to read the data using Python or MATLAB and ideally have scripts ready for 
  reading the data.
* Bring your laptop with appropriate software installed. For installation instructions see:
  * [**PyNWB (Python)**](https://pynwb.readthedocs.io/en/stable/install_users.html). If you are a developer and want to contribute to PyNWB see the [**Installing PyNWB for Developers**](https://pynwb.readthedocs.io/en/stable/install_developers.html) instructions. 
  * [**MatNWB (Matlab)**](https://neurodatawithoutborders.github.io/matnwb/)
* For an overview of NWB software, see also: 
  * [**Glossary of Core NWB Tools**](https://nwb-overview.readthedocs.io/en/latest/core_tools/core_tools_home.html) 
  * [**Glossary of Analysis and Visualization Tools**](https://nwb-overview.readthedocs.io/en/latest/tools/tools_home.html)
* For an overview of NWB see the [**NWB Overview Docs**](https://nwb-overview.readthedocs.io)

## Objective

The [Neurodata Without Borders](nwb.org) project is an effort to standardize the description and storage of neurophysiology
data and metadata. NWB enables data sharing and reuse and reduces the energy barrier to applying data analytics both within
and across labs. NWB has seen wide adoption in the neurophysiology community, and there are now over 100 datasets on the
DANDI Archive in NWB, including data from the Allen Institute and the International Brain Laboratory.

The **User Days** will train users how to convert their data to NWB and publish it on the DANDI Archive. 
We will work with members of the neuroscience community that want to apply NWB to their datasets. We will train 
attendees, starting from the basics and proceeding to advanced data engineering techniques to maximally utilize the
features of the HDF5 and Zarr backends. Attendees will also be trained in the creation of NWB extensions.

The **Developer Days** will bring  neuroscientists, tool builders, and research software engineers together to further the
development of the NWB software ecosystem, including the data standard, core software packages, official tools, and community tools. 
Members of the community will exchange ideas and best practices for using NWB and the libraries, share NWB based tools, surface 
common needs, solve bugs, make feature requests, brainstorm about future funding and collaboration, and make progress 
on current blockages.

**Note:** This event is meant to foster community and collaboration around NWB, not competition. As such, this is really
more of a "workshop" or "tutorial" than a "hackathon." There will be no judges nor prizes. Participants will be expected
to bring data from their own lab, bring their own tool, or other relevant project and/or collaborate with others to 
build integration with NWB.

## Agenda

<!-- ORGANIZERS: please edit AGENDA.md -->

{% include_relative agenda/AGENDA.md %}

## Projects

To ease collaborative editing of projects we are managing projects in the following Google Docs:

* [**User Days Projects**](https://docs.google.com/document/d/1SJOu-ze7L8QS-xJMLBwB42FrurA2Sbf2x8vy9TFMOx0/edit?usp=share_link)
* [**Developer Days Projects**](https://docs.google.com/document/d/1wXELFWmKnJu30_PsZdGw1F3TE9WNyBOvGEFLa-9uMP4/edit?usp=share_link)

To create a new project, simply:

* Open the project Google Doc. If you are participating and do not have edit access, then please contact the workshop organizers via email or Slack to request access.
* Make a copy of the project template section and add it to the end of the document
* Update at least your project’s title, key investigators, and project description sections


## Code of Conduct

Please see the [Code of Conduct](https://neurodatawithoutborders.github.io/nwb_hackathons/code_of_conduct) for all NWB events.


## Disclaimer

This website and related content were prepared as an account of or to expedite work sponsored at least in part by 
the United States Government. While we strive to provide correct information, neither the United States Government 
nor any agency thereof, nor The Regents of the University of California, nor any of their employees, makes any 
warranty, express or implied  or assumes any legal responsibility for the accuracy, completeness, or usefulness of 
any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately 
owned rights. Reference herein to any specific commercial product, process, or service by its trade name, trademark, 
manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by 
the United States Government or any agency thereof, or The Regents of the University of California.  Use of the 
Laboratory or University’s name for endorsements is prohibited. The views and opinions of authors expressed herein 
do not necessarily state or reflect those of the United States Government or any agency thereof or The Regents of 
the University of California.  Neither Berkeley Lab nor its employees are agents of the US Government. Berkeley Lab 
web pages link to many other websites.  Such links do not constitute an endorsement of the content or company and we 
are not responsible for the content of such links.


