# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:38:51 2021

@author: Caterina Brighi
"""

#%% Import functions 

import os
import glob
import pydicom
from pathlib import Path
import shutil

'''Before running the script remember to set the paths to the relevant directories in the following sections.

    '''

#%% Set Working directory
        
data_supradir = 'Insert here absolute path to the QIN dataset parent directory' #Set working directory

subjs_path = [ f.path for f in os.scandir(data_supradir) if f.is_dir() ] #Create a list of the paths to the patients directories
subjs_name = [ f.name for f in os.scandir(data_supradir) if f.is_dir() ] #Create a list of patients names

#%% Create output folder and subfolders

os.mkdir('absolute path to a the parent directory which will ultimately contain all your sorted subdirectories')
output_dir = 'absolute path to a the parent directory which will ultimately contain all your sorted subdirectories'

sequence_list = ['T1_Axial_post', 'MPRAGE', 'FLAIR', 'T2', 'ADC', 'DSC', 'DCE', 'DWI'] #list of all sequences you are going to group
for seq in sequence_list:
    os.mkdir(output_dir+'/'+seq) #generate an output subdirectory for each imaging sequence
    globals()[seq]=output_dir+'/'+seq #create a variable for each sequence containing the path to each output subdirectory
    

#%%Create a for loop to perform image analysis on each subject sequentially

for current in subjs_name:
    subj_dir = data_supradir+current
    subj_name = current
    
    #here you need to write a few lines to read the name of the subdirectories and figure out which one is assigned to timepoint 1 and which one to timepoint 2.
    #then set a path to timepoint 1 directory, which I will call tp1_dir

    tp1_dir = 'path to tp1 dir'

    for folder in glob.glob(tp1_dir+'/'+'*T1 Axial Post*'):
        shutil.copytree(folder, T1_Axial_post+'/T1 Axial Post_'+subj_name) #This copies the T1 Axial Post folder containing the dicoms files into a new subdirectory in the T1 Axial Post output directory

    #do the same for the other sequences you would like to sort


 