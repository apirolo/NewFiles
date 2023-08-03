# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:12:36 2023

@author: Alex
"""

import os

def NewFiles(OldFolder, NewFolder):
    
    for file in os.listdir(NewFolder):
        if os.path.isfile(OldFolder + "\\" + file):
            os.remove(NewFolder + "\\" + file)
            
    return
