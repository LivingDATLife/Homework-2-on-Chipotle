# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 07:51:05 2015

import csv
with open ("chipotle.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile)
    for line in tsvreader:
        print line [1:]
        
        
#was able to import the data to the spyder console but not do fully what the assignment asked

with open ("chipotle.tsv") as f:
    lines = f.read().split('\n') [:-1]
    for i, line in enumerate (lines):
      if i == 0:
          column_names = line.split()
      else:
          data = line.split();
          
#this just gave an output of what I put in. I didn't expect it to do anything 
#I was researching different methods of doing the assignment 
#Will definitely play around with it this week 
#definitely be in office hours on the weekend       
    
