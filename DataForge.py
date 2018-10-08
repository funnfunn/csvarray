# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:18:48 2018

@author: streetsr
"""





class DataForge:

#    datafilename=''
#    rowNo=''
#    colNo=''
#    headingList=''

    def __init__(self):
        
        
    def loadCSV(self, csvdata):
        datafilename=csvdata
        d = '\t'
        f=open(datafilename,'r')
        reader=csv.reader(f)
        
        #make sure we are at begining of file
        f.seek(0)
        #put csv data into a 2D array
        arr=list(reader)
        headingArray=arr[0]
        rowNo = len(arr)
        colNo = len(arr[0])
        #tranpose list to turn columns into rows, thus access data easier
        arr2=list(map(list, zip(*arr)))
        