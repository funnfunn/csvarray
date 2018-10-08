# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 12:02:15 2018

@author: streetsr
"""




import numpy as np
import pandas as pd
import time
from dateutil import parser
import csv
import sys
import itertools # use this to count the number of columns in the CSV file
from io import StringIO



datafilename = 'csvdata.csv'
d = '\t'
f=open(datafilename,'r')
##I started this code trying to manipulating everyting in terms of CSV, but I think it is better that I just put everything into a 2D array ASAP, which I have done below using the 'list(reader)' command 
reader=csv.reader(f)#,delimiter=d) # dont need this delimiter
ncol=len(next(reader)) # Read first line and count columns
f.seek(0)              # go back to beginning of file
'''
for row in reader:

#PRINT OUT ON SCREEN ALL DATA FROM CSV FILE 
    for row in reader:
        print(row)
'''        

print(ncol)
print('break\n')


for row in reader:
    #print out each cell in each row
    i=0
    while(i < ncol):    
    #need the  ', end'\t\t' term as otherwise will only go through each character
        print(row[i], end='\t\t')
        i+=1

#use enumerate to count rows
f.seek(0) #go back to beginning of file
print('break\n')
#print(list(enumerate(reader)))
#print(list(reader))
#put csv data into a 2D array
arr=list(reader)
print(len(arr))         #number of rows
print(len(arr[0]))      #number of columns 

#tranpose list to turn columns into rows, thus access data easier
arr2=list(map(list, zip(*arr)))
unitcosts=arr2[5]
#remove list name from list
unitcosts.pop(0)
print(unitcosts)
#convert to float
unitcosts=[float(i) for i in unitcosts]
meanUC=np.mean(unitcosts)
print(meanUC)
datelist=arr2[0];
datelist.pop(0)
print(datelist)


