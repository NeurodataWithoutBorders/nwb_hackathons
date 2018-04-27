#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 08:39:36 2018

@author: Nic
"""

# GCAMP
from pynwb.image import ImageSeries
from pynwb import NWBFile, NWBHDF5IO
import os, warnings, datetime
import scipy.io as spio
os.chdir('/Volumes/Nic/revault/revault2/cmdata_CCD_analysis/cm62_2')
mat = spio.loadmat('cm62_2_runE_stim1.mat',variable_names=['data_out'])
mat = mat['data_out']
gcamp = mat['gcamp'][0][0]
chbo = mat['chbo'][0][0]
chbr = mat['chbr'][0][0]


def acquisition_rate(txt_file_name):
    warnings.warn('This is hard coded. Make sure to implement txt file loading.')
    return 31.2207

gcamp_nwb = ImageSeries(
        name='gcamp',
        source='NA',
        data=gcamp,
        unit='NA',
        format='raw',
        starting_time = 0.,
        rate = acquisition_rate(None)
        )

chbo_nwb = ImageSeries(
        name='chbo',
        source='NA',
        data=chbo,
        unit='NA',
        format='raw',
        starting_time = 0.,
        rate = acquisition_rate(None)
        )

chbr_nwb = ImageSeries(
        name='chbr',
        source='NA',
        data=chbr,
        unit='NA',
        format='raw',
        starting_time = 0.,
        rate = acquisition_rate(None)
        )

# WEBCAM
import os, glob, time, numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
i = 0
os.chdir('/Volumes/Nic/revault/revault2/cmdata/cm62_2/CCD/runE/runE_webcam1/')
img_full = np.zeros((480,640,len(glob.glob('*.jpg'))),dtype=np.uint8)
for filename in glob.iglob('*.jpg'):
     img = mpimg.imread('runE'+str(i)+'.jpg')
     img_full[:,:,i] = img[:,:,0]
     i += 1
     #imgplot = plt.imshow(img)
     #plt.show()
     #time.sleep(.1)
     #print(i)
     
webcam_nwb = ImageSeries(
        name='webcam_CCD',
        source='NA',
        data=img_full,
        unit='NA',
        format='raw',
        starting_time = 0.,
        rate = acquisition_rate(None)
        )

# Construct NWB File
nwbfile = NWBFile(
        source = 'NA',
        session_description = 'cm62_2_runE_stim1',
        identifier = 'cm62',
        session_start_time = datetime.datetime(2018,1,1,1,0,0),
        file_create_time = datetime.datetime.now()
        ) 

nwbfile.add_acquisition(gcamp_nwb)
nwbfile.add_acquisition(chbo_nwb)
nwbfile.add_acquisition(chbr_nwb)
nwbfile.add_acquisition(webcam_nwb)


with NWBHDF5IO('test_output.nwb', mode = 'w') as io:
    io.write(nwbfile,cache_spec = False)
