# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:19:22 2024

@author: thehe
"""

import sys
import os.path
filename = "skeleascii.txt"
file_exists = os.path.isfile(filename)

if file_exists: 
    print("\n* ",filename,"opened\n")
    f = open(filename,"r")
else:
    print ("\n file name not found\n")
    sys.exit(0)
record=f.readline()
sys.clear()