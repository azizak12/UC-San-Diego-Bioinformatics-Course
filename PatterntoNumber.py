# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:44:05 2017

@author: kurby
"""

def PatternToNumber(Pattern):
  num = ""
  bases = {'A':'0','C':'1','G':'2','T':'3'}
  for char in Pattern:
    num += bases[char]
  return int(num,4)

print(PatternToNumber("ATGCAA"))
