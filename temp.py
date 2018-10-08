# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import time
from dateutil import parser
import csv
import sys


#f = open(sys.argv[1], 'rb')

with open('datafile.csv') as datafile:
#    writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    reader = csv.reader(datafile)
    for row in reader:
        print(row[1])
        
        
       
    #employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    #employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

'''
f = open('datafile.csv', 'rb')
reader = csv.reader(f)
lineCount = 0

for row in reader:
    if lineCount==0:
        print(f'Column names are {", ".join(row)}')
        lineCount += 1
    else:
         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
         line_count += 1
         
print(f'Processed {line_count} lines.')
'''         





dt = parser.parse("1/6/2012")

print(dt)

#makes UK format instead of yank format
dt = parser.parse("1/6/2012", dayfirst=True)

print(dt)


print('Hello World!')



'''
arr=np.zeros((20,9))

arr[0][4]=1
arr[19][4]=1

"""
arr = { (3, 5, 10, 12, 20), (2, 2 , 2 , 3, 4) }
"""


for i in arr:
  print(i)
'''

  
  
  
