# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:42:28 2022

@author: Keith Roper
"""

import numpy as np
import random as rm

# generates pcr data cycle by cycle for given number of cycles and samples iteratively
# nested for loops to initialize variables piecewise (one at a time) and to iterate
def pcr1(cycles, samples):
    pcr_data = np.zeros([cycles+1,samples+1])
    print(pcr_data) # check data array size and initialization
    for i in range(cycles+1):
        for j in range(samples+1):
            if i == 0 and j==0:
                pcr_data[i,j] = 0   #initial value of cycles (0) corresponding to sample template at cycle = 0
            elif i==0 and j>0:
                pcr_data[i,j] = j  #defined value of sample  at cycle = 0       
 #               pcr_data[i,j] = rm.randint(0,4)   #initial value of sample  at cycle = 0
            elif i>0:
                if j == 0:
                    pcr_data[i,j] = pcr_data[i-1,j]+1  # increment cycle by 1             
                else:
                    pcr_data[i,j] = pcr_data[i-1,j]*2
 #                   print(i,pcr_data[i,j])  #confirm iterative calculation
 #                   NT=pcr_data[i-1,j]  # another way to caculate new template value                
 #                   pcr_data[i,j] = NT*2
    print('cycle ',end='')
    for i in range(1,samples+1):
        print('s'+str(i)+'  ',end='')
    print()
    print(pcr_data)

# generates pcr data cycle by cycle for given number of cycles and samples via calculation
# list comprehension to initialize row/column of variables; for loop to calculate concentrations piecewise
def pcr1_0(cycles, samples):
    pcr_data = np.zeros([cycles+1,samples+1])
#    print(pcr_data) # check data array size and initialization
    pcr_data[0,0:]= [j for j in range(samples+1)]
#   print(pcr_data)  # confirm sample initial value initialization   
    pcr_data[0:,0]=[i for i in range(cycles+1)]
#    pcr_data[0,0:]=np.arange(samples+1)   #np alternative
#    pcr_data[0:,0]=np.arange(cycles+1)  #np alternative
#   print(pcr_data)  # confirm cycle number initialization
    for i in range(1,cycles+1):
        pcr_data[i,1:]=[pcr_data[0,j]*2**i for j in range(1,samples+1)]
#    print(pcr_data)  # confirm sample change per cycle calculation    
    print('cycle ',end='')
    for i in range(1,samples+1):
        print('s'+str(i)+'  ',end='')
    print()
    print(pcr_data)
    
# generates pcr data cycle by cycle for given number of cycles and samples via calculation
# list comprehension to initialize row/column of variables and calculate array
def pcr1_1(cycles, samples):
    pcr_data = np.zeros([cycles+1,samples+1])
#    print(pcr_data) # check data array size and initialization
    pcr_data[0,0:]= [j for j in range(samples+1)]
#   print(pcr_data)  # confirm sample initial value initialization   
    pcr_data[0:,0]=[i for i in range(cycles+1)]
#   print(pcr_data)  # confirm cycle number initialization
    pcr_data[1:,1:]=[[pcr_data[0,j]*2**pcr_data[i,0] for j in range(1,samples+1)] for i in range(1,cycles+1)] 
#    print(pcr_data)  # confirm sample change per cycle calculation   
    print('cycle ',end='')
    for i in range(1,samples+1):
        print('s'+str(i)+'  ',end='')
    print()
    print(pcr_data)

# returns number of cycles needed to reach target amplicon concentration from initial concentration
# for loop nested in while loop to calculate concentrations piecewise from initial concentration
def pcr2_0(initial,target):
    pcr_data = np.zeros([51,2])
#    print(pcr_data) # check data array size and initialization
    current_value = 0
    i=0
    print('cycle '+'copies')
    while current_value<target:
        for j in range(2):
            if i == 0 and j==0:
                pcr_data[i,j] = 0   #initial value of cycles (0)
 #               print('initial cycles ',pcr_data[i,j])
            elif i==0 and j>0:
                pcr_data[i,j] = initial    
 #               print('initial copies ',pcr_data[i,j])
                i+=1                 
            elif i>0:
                if j == 0:
                    pcr_data[i,j] = pcr_data[i-1,j]+1  # increment cycle by 1        
                else:
                    pcr_data[i,j] = pcr_data[i-1,j]*2
                    print(i,pcr_data[i,1]) 
                    current_value = pcr_data[i,j]
                    i+=1 
 #       print(i,current_value)
    print('template reached target '+str(target)+' copies at '+str(i-1)+' cycles' ) 
    print('cycle '+'s1')
    print(pcr_data[0:i,0:])               

# returns number of cycles needed to reach target amplicon concentration from initial concentration
# while loop frames calculation of successive concentrations from initial concentration
def pcr2_1(initial,target):
    pcr_data = np.zeros([51,2])
#    print(pcr_data) # check data array size and initialization
    current_value = 0
    i=1
    pcr_data[0,1]= initial
    print('cycle '+'copies')
    while current_value<target:
        pcr_data[i,0] = i
        pcr_data[i,1] = pcr_data[i-1,1]*2
        current_value = pcr_data[i,1]
        i+=1 
        print(i,current_value)
    print('template reached target '+str(target)+' copies at '+str(i-1)+' cycles' )   
    print('cycle '+'s1')
    print(pcr_data[0:i,0:])               

# returns number of cycles needed to reach target amplicon concentration from initial concentration
# while loop frames calculation of successive concentrations from initial concentration
# while loop uses array value
def pcr2_2(initial,target):
    pcr_data = np.zeros([51,2])
#    print(pcr_data) # check data array size and initialization
    i=1
    pcr_data[0,1]= initial
    print('cycle '+'copies')
    while pcr_data[i-1,1]<target:
        pcr_data[i,0] = i
        pcr_data[i,1] = pcr_data[i-1,1]*2
        i+=1 
#        print(i-1,pcr_data[i-1,1])  #confirm iteration of while loop
    print('template reached target '+str(target)+' copies at '+str(i-1)+' cycles' )   
    print('cycle '+'s1')
    print(pcr_data[0:i,0:])    
    
'''    numpy.append
numpy.append(arr, values, axis=None)[source]
Append values to the end of an array.

Parameters
arr: array_like
Values are appended to a copy of this array.

values: array_like
These values are appended to a copy of arr. It must be of the correct shape (the same shape as arr, excluding axis). If axis is not specified, values can be any shape and will be flattened before use.

axisint, optional
The axis along which values are appended. If axis is not given, both arr and values are flattened before use.

Reference: https://numpy.org/doc/stable/reference/generated/numpy.append.html
''' 

# returns number of cycles needed to reach target amplicon concentration from initial concentration
# while loop frames calculation of successive concentrations from initial concentration
# small initial array appended in while loop
def pcr2_3(initial,target):
    pcr_data = np.zeros([2,2])
#    print(pcr_data) # check data array size and initialization
    i=1
    pcr_data[0,1]= initial
    print('cycle '+'copies')
    while pcr_data[i-1,1]<target:
        pcr_data[i,0] = i
        pcr_data[i,1] = pcr_data[i-1,1]*2
        i+=1 
        pcr_data = np.append(pcr_data, np.zeros([1,2]), axis=0)
        print(i-1,pcr_data[i-1,1])  #confirm iteration of while loop
    print('template reached target '+str(target)+' copies at '+str(i-1)+' cycles' )   
    print('cycle '+'s1')
    print(pcr_data)  

# returns number of cycles needed to reach target amplicon concentration from initial concentration
# list comprehension calculates 1-D array of concentrations
# np to insert cycle number and transpose    
def pcr2_4(initial,target):
    data=[initial*2**i for i in range(1,50) if initial*2**i <= target]
    print('template reached target '+str(target)+' copies at '+str(len(data))+' cycles' )   
    dat = np.array([np.arange(1,len(data)+1),data])
    pcr_data=np.transpose(dat)
    print('cycle '+'s1')
    print(pcr_data) 
