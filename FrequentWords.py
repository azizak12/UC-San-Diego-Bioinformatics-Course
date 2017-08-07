# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:29:16 2017

@author: kurby
"""
"""
#Pseudocode

FrequentWords(Text, k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← the k-mer Text(i, k)
            Count(i) ← PatternCount(Text, Pattern)
        maxCount ← maximum value in array Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                add Text(i, k) to FrequentPatterns
        remove duplicates from FrequentPatterns
        return FrequentPatterns
"""
       
def PatternCount(Text,Pattern):
  count = 0
  for i in range(0,len(Text)-len(Pattern)+1):
    if Text[i:i+len(Pattern)] == Pattern:
      count += 1
  return count

def FrequentWords(Text,k):
    FrequentPatterns = []
    Count = []
    for i in range(0,len(Text)-k+1): #iterating through Text
        Pattern = Text[i:i+k]
        Count.insert(i,PatternCount(Text,Pattern))
    maxCount = max(Count)
    for i in range(len(Count)): #iterating through Count
        if Count[i] == maxCount:
            FrequentPatterns.append(Text[i:i+k])
    return(list(set(FrequentPatterns)))
    
print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT",4)) 
