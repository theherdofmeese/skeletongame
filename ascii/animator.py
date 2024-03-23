# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:37:20 2024

@author: thehe
"""
# Open the file in read mode

import time as t
i=0
while i< 20:
    i+=1
    with open('skeleascii2.txt', 'r') as file:
        # Read each line from the file and print it
        for line in file:
            print(line, end='')  # Use end='' to avoid extra newlines
    print("\n")
    t.sleep(.1)
    with open('skeleascii2.2.txt', 'r') as file:
        # Read each line from the file and print it
        for line in file:
            print(line, end='')  # Use end='' to avoid extra newlines
    t.sleep(.1)
    print("\n")