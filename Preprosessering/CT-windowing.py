# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 08:57:26 2022

@author: Sofie
"""
# Importere nødvendige pakker
import numpy as np
import nibabel as nib
import os

# Sette directory filene skal hentes fra, og nytt directory
directory = 'data/image_data/ous/tumor_ds/ct'
new_directory = 'data/image_data/ous/tumor_ds/ct_windowed'
 
# Definere window width og window level for CT-bildet
center = 60
width = 350


# Iterere over alle bildene i en for-løkke og lagre i ny mappe med
# preproseserte bilder.

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        img = nib. load(directory+'/'+filename)
        data = img. get_data()
        data=data-1024 # Konvertere til HU
        
        data=np.where(data >= width/2+center, width/2+center, data)
        data=np.where(data<=-width/2+center, -width/2+center, data)
        ct_windowed = data+ width/2-center
        new_image = nib.Nifti1Image(ct_windowed, affine=np.eye(4))
        nib.save(new_image, os.path.join(new_directory, filename))
