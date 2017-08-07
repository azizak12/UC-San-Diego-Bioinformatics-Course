# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:21:25 2017

@author: kurby
"""

#Challenge
#Reverse Complement Problem: Find the reverse complement of a DNA string.
#     Input: A DNA string Pattern.
#     Output: Patternrc , the reverse complement of Pattern.

def RevComp(Pattern):
    Patternrc = []
    bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for char in reversed(Pattern):
        Patternrc.append(bases[char])
    return "".join(Patternrc)
    
print(RevComp("AAAACCCGGT"))