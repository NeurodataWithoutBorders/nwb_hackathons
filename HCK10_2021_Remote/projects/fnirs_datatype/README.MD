[:rewind: Back to the projects list](../../README.md#ProjectsList)
<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# fNIRS neurodata type 

## Key Investigators
<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->
* Darin Erat Sleiter ([AE Studio](ae.studio))
* Sumner Lee Norman ([AE Studio](ae.studio))
* José Ribeiro ([AE Studio](ae.studio))

## Project Description
<!-- Add a short paragraph describing the project. -->
In this project, we will convert at least one candidate fNIRS dataset into NWB format. Our stretch goals include writing an automated conversion tool and some preliminary fNIRS data visualization tools (e.g. that could integrate with nwbwidgets) 

## Objectives
<!-- Briefly describe the objectives of your project. What would you like to achive?-->
We will:
<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->
1. Objective A. Create a new fNIRS neurodata type using [the ndx-template](https://github.com/nwb-extensions/ndx-template) 
2. Objective B. Submit the new neurodata type to the [NDX Catalog](https://github.com/nwb-extensions/).
3. Objective C. (stretch) Create an automated SNIRF --> fNIRS conversion tool.
4. Objective D. (stretch) Create preliminary fNIRS data visualization tools.
​
## Approach and Plan
<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->
1. Explore the datasets listed here and determine the best one for prototyping first.
1. Make a list of all fNIRS relevant neurodata structures and what lower level structures would be best to build on (e.g. time series vs. imaging time series). 
1. Submit the fNIRS neurodata type to the NWB repository.
1. Formalize the conversion between SNIRF sample data and the new NWB_fNIRS neurodata type.
1. Build a set of preliminary fNIRS data visualization tools.
​
## Progress and Next Steps
<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->
WIP
​
## Materials
<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->
1. Jaeyoung et al. [data is available at this link](http://doc.ml.tu-berlin.de/hBCI/contactthanks.php) or `wget http://doc.ml.tu-berlin.de/hBCI/NIRS/NIRS_01-29.zip` for fNIRS data only
1. Bak et al. [data is available on figshare](https://figshare.com/articles/dataset/Open_access_fNIRS_dataset_for_classification_of_the_unilateral_finger-_and_foot-tapping/9783755/1)
and [analysis is available on github](https://github.com/JaeyoungShin/fNIRS-dataset)
1. [SNIRF sample data can be found here](https://github.com/fNIRS/snirf-samples/tree/253e533fe9118a0fea0fac0e6fc5506d737e647d)
​
## Background and References
<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->
### Publications related to data
1. [[Jaeyoung Shin, Alexander von Lühmann, Benjamin Blankertz, Do-Won Kim, Han-Jeong Hwang and Klaus-Robert Müller, "Open Access Dataset for EEG+NIRS Single-Trial Classification," IEEE Trans. Neural Syst. Rehabil. Eng., online published.](http://doc.ml.tu-berlin.de/hBCI/contactthanks.php)](http://doc.ml.tu-berlin.de/hBCI/contactthanks.php)
1. [Bak, SuJin, Jinwoo Park, Jaeyoung Shin, and Jichai Jeong. "Open-access fNIRS dataset for classification of unilateral finger-and foot-tapping." Electronics 8, no. 12 (2019): 1486.](https://www.semanticscholar.org/paper/Open-Access-fNIRS-Dataset-for-Classification-of-and-Bak-Park/48a0537fbb487454c53bd0d893a43402d7b75b88)
