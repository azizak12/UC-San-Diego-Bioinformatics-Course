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

def ComputingFrequencies(Text,k):
  FrequencyArray = []
  for i in range(0,4**k): #initializing to zero
    FrequencyArray.append(i)
    FrequencyArray[i] = 0
  for i in range (0,len(Text)-k+1): #iterating through sequence only once
    Pattern = Text[i:i+k] #grabs a k-mer pattern in sequence
    j = PatternToNumber(Pattern) #finds the location of pattern in array
    FrequencyArray[j] += 1
  return ' '.join(map(str,FrequencyArray))
  
print(ComputingFrequencies("ACGCGGCTCTGAAA",2))