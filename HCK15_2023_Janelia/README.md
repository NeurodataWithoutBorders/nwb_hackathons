# NWB User Days and Developer Hackathon 2023

  * [Report](#report)
  * [Dates and Location](#dates-and-location)
  * [Attendees](#attendees)
  * [Registration](#registration)
  * [Logistics](#logistics)
  * [Organizing Committee](#organizing-committee)
    * [Additional Organizational Support](#additional-organizational-support)
  * [Resources](#resources)
  * [What to bring?](#what-to-bring)
  * [Objective](#objective)
  * [Agenda](#agenda)
    * [User Days](#agenda-user-days)
    * [Developer Days](#agenda-developer-days)
    * [Calendar](#agenda-calendar)
  * [Projects](#projects)
     * [Creating a New Project](projects/README.md)
  * [Registrants](#registrants)
  * [Attending Remotely](#attending-remotely)
  * [Resources](#resources)
  * [Disclaimer](#disclaimer)

[//]: # (## Report)

[//]: # ()
[//]: # (The final report for the 15th NWB Developer Hackathon and User Days is now available:)

## Dates and Location

- **Dates:** July 24-29, 2023
  - **User Days:** July 24-26, 2023
  - **Developer Days:** July 27-29, 2023
- **Location:** [HHMI Janelia Research Campus](https://www.janelia.org/), 19700 Helix Dr, Ashburn, VA 20147,
  [Openstreetmap](https://www.openstreetmap.org/?mlat=39.0708&mlon=-77.4655#map=14/39.0708/-77.4655)
  [Directions](https://www.janelia.org/directions)
- **Meeting Rooms:** For the meeting we have two rooms. The main room is *Synapse* and the breakout room is *Spectrum*.
  For details about the room locations see the [building map.](travel/janelia_room_plan_for_6th_nwbn_hackathon.pdf)

## Registration

If you would like to attend the NWB User and Developer Workshop, please register 
[here](https://forms.gle/ZqgUKDCfcX9XT8AbA). Registration for this event is free. Space at the event is limited and 
registration is on a first-come basis.

## Logistics

**Housing:** Housing will be provided onsite on the Janelia Research Campus. For details about transportation and 
logistics please see [here](https://www.dropbox.com/s/i2540enmapap05o/Janelia%20travel%20logistics.pdf?dl=0)

[//]: # (**Travel:** Travel support is being provided by The Kavli Foundation. As housing will be onsite on the Janelia )

[//]: # (research campus, travel support is intended for flights &#40;not housing&#41;. Funds available to support attendee travel are limited! Travel arrangements must be pre-approved by the Foundation’s Executive Assistant. If you use the Kavli travel services &#40;recommended&#41; then please CC Stephanie Albin &#40;salbin@kavlifoundation.org&#41; to get approval for the travel cost. Also, if you are planing to book your own flights then please make sure to get PRE-APPROVAL from Stephanie Albin &#40;salbin at kavlifoundation.org&#41;. Please see the [Kavli reimbursement guidelines]&#40;travel/Kavli_Reimbursement_Guidelines.pdf&#41; for details. The traveler profile form is available [here]&#40;travel/CT_Traveler_Profile.docx&#41;.)

**Directions:** The Janelia Research Campus is located in Loudoun County, Virginia – just 30 miles from Washington, DC,
and about eight miles north of Dulles International Airport (IAD). For directions see
[https://www.janelia.org/directions](https://www.janelia.org/directions).


## Organizing Committee

**Site chair:** Jakob Voigt
**Program chair (User Days):**  Oliver Rübel and Ben Dichter
**Program chair (Developer Days):** Oliver Rübel and Ryan Ly
**Administrative Support:** Janine Stevens

### Additional Organizational Support

- The Kavli Foundation
- Janelia HHMI

[//]: # ()
[//]: # (## Resources)

[//]: # ()
[//]: # (### Talks)

[//]: # (The slides for the talks presented during the User Days are available [here.]&#40;https://drive.google.com/drive/folders/18oG1rRJpluXQJJQaH4xbz6u58LXPiZbI?usp=sharing&#41;)

[//]: # ()
[//]: # (### Code)

[//]: # ()
[//]: # (Ben Dichter's electrophysiology tutorial &#40;Day 1&#41;:)

[//]: # ()
[//]: # (* [python jupyter notebook]&#40;http://htmlpreview.github.io/?https://github.com/NeurodataWithoutBorders/nwb_hackathons/blob/master/HCK06_2019_Janelia/NWB_tutorial_2019_python.html&#41;)

[//]: # (* [matlab code]&#40;http://htmlpreview.github.io/?https://github.com/NeurodataWithoutBorders/nwb_hackathons/blob/master/HCK06_2019_Janelia/NWB_tutorial_2019_matlab.html&#41;)

[//]: # ()
[//]: # (Tom Davidson's 'early adopter experiences' talk &#40;Day 1&#41;:)

[//]: # ()
[//]: # (* [Repo containing notebooks in talk]&#40;https://github.com/LorenFrankLab/franklab-nwb-hack/tree/master/hackathon-6&#41;)

## What to bring?

* Create the outline for your project at the hackathon. For further details and instructions on how to create a project see [here](projects/README.md)
* Bring any example data sets needed for your project with you to the hackathon. For any lab-specific data (i.e., data not in NWB) you should know how to read the data using Python and ideally have scripts ready for reading the data.
* Bring your laptop with appropriate software installed. For instructions on how to install PyNWB see [http://pynwb.readthedocs.io/en/latest/getting_started.html#installation](http://pynwb.readthedocs.io/en/latest/getting_started.html#installation)
* For an overview of NWB see also: [The NWB Overview Docs](https://nwb-overview.readthedocs.io/en/latest/)

## Objective

The [Neurodata Without Borders](nwb.org) project is an effort to standardize the description and storage of neurophysiology
data and metadata. NWB enables data sharing and reuse and reduces the energy-barrier to applying data analytics both within
and across labs. NWB has seen wide adoption in the neurophysiology community, and there are now over 100 datasets on the
DANDI Archive in NWB, including data from the Allen Institute and the International Brain Laboratory.

The User Days will train users how to convert their data to NWB and publish it on the DANDI Archive. 
We will work with members of the neuroscience community that want to apply NWB to their datasets. We will train 
attendees, starting from the basics and proceeding to advanced data engineering techniques to maximally utilize the
features of the HDF5 and Zarr backends. Attendees will also be trained in the creation of NWB extensions.

The Developer days will bring the experimental neurophysiology community together to further adoption and the
development of NWB, the NWB software libraries, and the progress of the scientific workflows that rely on NWB. Members of
the community will exchange ideas and best practices for using NWB and the libraries, share NWB based tools, surface 
common needs, solve bugs, make feature requests, brainstorm about future funding and collaboration, and make progress 
on current blockages.

Note: This event is meant to foster community and collaboration around NWB, not competition. As such, this is really
more of a "workshop" or "tutorial" than a "hackathon." There will be no judges nor prizes. Participants will be expected
to bring data from their own lab and/or collaborate with others to build integration with NWB.

## Agenda

<!-- ORGANIZERS: please edit AGENDA.md -->

{% include_relative agenda/AGENDA.md %}

## Projects

We will provide a Google Doc for attendees to share their progress on projects with each other.

[//]: # ()
[//]: # (## Attending Remotely)

[//]: # ()
[//]: # (We are using Zoom for remote participation.There are multiple ways to join this meeting.)

[//]: # ()
[//]: # (1. Use the following link to Join the meeting from your desktop or cell: [https://hhmi.zoom.us/j/122156921]&#40;https://hhmi.zoom.us/j/122156921&#41; &#40;This will load the Zoom client and is recommended for the best audio quality!&#41;)

[//]: # ()
[//]: # (2. From a cell phone if you are not able to use the first link :)

[//]: # (US: **+19294362866,,122156921#** or **+16699006833,,122156921#**)

[//]: # ()
[//]: # (3. From a standard telephone : Dial&#40;for higher quality, dial a number based on your current location&#41;:)

[//]: # (US: +1 929 436 2866 or +1 669 900 6833 or 877 853 5257 &#40;Toll Free&#41; or 855 880 1246 &#40;Toll Free&#41;)

[//]: # (Meeting ID: 122 156 921  &#40;Find your local number: [https://zoom.us/u/acHwiXLxGC]&#40;https://zoom.us/u/acHwiXLxGC&#41;&#41;)

[//]: # ()
[//]: # (4. If you are in an HHMI conference room, use the touch panel to dial 2800. When prompted, type #122 156 921#)

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


