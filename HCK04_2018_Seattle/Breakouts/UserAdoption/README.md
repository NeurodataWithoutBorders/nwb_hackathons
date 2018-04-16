Back to [Breakout Sessions](../../README.md#breakout-sessions)

* Andrew Tritt (LBNL)
* Jean-Christophe Fillion-Robin (Kitware)
* Nick Cain (AIBS)
* Oliver Ruebel (LBNL)
* Will Schroeder (Kitware)
* Justin Kiggins (AIBS)
* *Thanks [@bendichter](https://github.com/bendichter) for taking notes*

# Improving NWB user adoption and removing pain points

1. Discussion of current pain points. [Slides](https://docs.google.com/presentation/d/1WGkEtX7yAXMHUC6nhRmvyM7yoimmM_A_uPUI_s2kdak/edit#slide=id.p)

# Notes

## Action items

The following is a list of high-level action items as a result of the user adoption hangout:

* Update https://neurodatawithoutborders.github.io/ to organize all online docs under one umbrella (Done)

* Creating "good first issue" andd "help wanted" labels on the PyNWB repo to help guide new developers to issues they can address (Done)

* Talk to Kavli and propose changes to nwb.org (in progress)

* Update ReadTheDocs documentation pages to add a menu bar for cross-linking between the various pages 

* Setup monthly developer/user "hangout" call that is open for everyone to join. The goal is to allow a) developers to sync up and b) to allow users to come in ask questions. 

Completed action items from the breakout:


## Online Documentation / Websites
 
### nwb.org

 * Proposed changes to nwb.org:
 
    * Update entry points below the banner
   
		* For users/developers --> Point to https://neurodatawithoutborders.github.io/
		* History --> Point to history http://www.nwb.org/nwb-neurophysiology/
		* Questions About NWB:N --> Point to Google Group https://groups.google.com/forum/#!forum/neurodatawithoutborders
		* Join Our Mailing List --> Point to KAVLI mailing list. 
    
    *  Some of the information on nwb.org needs to be updated to reflect the current state of the project. Some specific items:
		* Our sponsors should be updated and moved out of the top banner to a seprate location
		* http://www.nwb.org/founding-institutions/ : Needs to be updated to reflect the current project teams and funders. Previous funders and members should then be listed in an Alumni section of the page. 
		* http://www.nwb.org/nwb-neurophysiology/ : The text on this page currently mainly describes the original pilot and should be updated to describe also the development of NWB 2. Alternatively, we could also remove the page and instead have the main menu "NWB: Neurophysiology --> Introduction --Detailed" point directly to https://neurodatawithoutborders.github.io/ . In either case, https://neurodatawithoutborders.github.io/ should be somehow available from the main menu.
		* http://www.nwb.org/resources/ : All links on the page currently point to NWB 1. This page should be updated to point to the current format specification (http://nwb-schema.readthedocs.io/en/latest/) and  APIs (http://pynwb.readthedocs.io/en/latest/ and https://github.com/NeurodataWithoutBorders/matnwb). Material for NWB:N 1 should be either moved to a different page or appear in a seprate section specific to NWB:N 1.
		* http://www.nwb.org/contact-us/ : Since the mailing list is accesible by Kavli only, we should direct people to the google group list first for questions to allow developers and users to respond to questions.
		* Make banner height smaller 
    
    * Create page with “NWB is used by these labs”
    
### User/Developer Website for NWB:N

We need a landing page for NWB:N (separate from the NWB nwb.org landing page) that is focused on end users and developers rather than funders and NWB at large. While there is a lot of documentation available, we need better cross-linking between the documents as well as a central place for users to go to for information about the NWB:N data standard and software.

* Proposed process 

    * The developer team will create this at: https://neurodatawithoutborders.github.io/
    
    * The site should also be easily accesible from nwb.org

    * indicate that NWB:N is under active development and not yet guaranteed to be backwards compatible since we are in Beta and not final release yet. Will Schroeder, will help us with language here please?

    * Look at CMake landing page for an example
    
    * A lot of the initial content will likely come from http://nwb-overview.readthedocs.io/en/latest/ , which once ported to the new site, will be deprectated. 
    
    * Parts that should be included on the new user/developer page:

	    * Value proposition - pitch to use NWB

	    * Resources : Link to all available online docs

	    * Mailing list

	    * GitHub : Link to the main repositories

	    * Describe various tools in ecosystem (matnwb, pynwb, nwb-schema, etc.)

	    * Google group

	    * Want to get involved? link to the url to the pre-defined “good first issue” tag

###  ReadTheDocs

* Proposed changed: 
	
	* Need cross-linking between the various documentations


## Outreach

  * Hackathons now, then transition into giving talks at conferences

    * Events:

      * Cosyne
      * Neurohack week
      * SfN
      * CNS


  * Blogging

    * open source guide a good resource for community engagement



## Internal Processes

* Pain points: 
  * recruiting developers
    * on-ramp issues: tag for “good first issue”
      * we should all go through the steps of solving a “good first issue”
      
* User expectations: New users currently often expect that NWB 2 is stable rather than being under active development. 
  We need to be clearly communicate this. This may be harder on nwb.org but should be clearly spelled out on https://neurodatawithoutborders.github.io/

* Someone needs to be the person who holds the community together
* Public hangout every two weeks or monthly
  * agenda
  * establish culture
	* aim for 2-5 new users
	* find time, ideally good for europeans
	* Nick to make sure AI is involved in development meetings






