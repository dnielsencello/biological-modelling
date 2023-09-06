# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 15:01:32 2022

@author: Keith Roper
"""
  
''' #0. Before you work with files '''
import os
os.getcwd()
os.chdir('C:\\Users\\Keith Roper\\Desktop')
# Note: two backslashes are needed
os.getcwd()
print(os.getcwd())
os.chdir('C:\\Users\\Keith Roper\\Documents\\USU\\BE Dept\\Classes\\BE 5020\\Lessons\\lesson 04_Files Import Export')
os.getcwd()
print(os.getcwd())

''' #1. Importing data'''
import numpy as np
sensor_data=np.loadtxt('mv_Sensor.csv',delimiter=',')
# programnming object np.loadtxt can read in .csv or .txt files
print(sensor_data)

pcr_dat = np.loadtxt('PLJM1_SD1_std_curve_2.csv', delimiter = ',')
print(pcr_dat)
#   file of floating point variables

''' #2. Exporting data '''
# programnming object np.savetxt can print a stream in .csv or .txt files
np.savetxt('pH_Sensor.csv',sensor_data,delimiter=',')
np.savetxt('pH_Sensor.txt',sensor_data,delimiter=',')
# change the filename to not write over a previously saved file

np.savetxt('pcr_dat.csv',pcr_dat,delimiter=',')

''' #3. Format output files '''
np.savetxt('pH_Sensor.txt',sensor_data,fmt=['%i','%.4f'],delimiter=',')
#	'%.4f'        (Number fixed to four decimal places.  Typical to use)
#	'%d' or '%i'  (Numbers are output to file as in integer)
#	'%.4e'        (Numbers are fixed using scientific notation)   
#   brackets [ ] allow specifying different vectors
np.savetxt('pH_Sensora.txt',sensor_data,fmt=['%.3f','%.4f'],delimiter=',')

np.savetxt('pcr_dat_1.csv',pcr_dat,fmt=['%i','%.4f'],delimiter=',')
np.savetxt('pcr_dat_2.csv',pcr_dat,fmt=['%i','%.2f'],delimiter=',')

''' #4. Adding Headers to a File '''
Labels='mL_base,pH_buffer'
np.savetxt('pH_Sensor.txt',sensor_data,fmt=['%.3f','%.4f'],delimiter=',',newline='\r\n',header=Labels)
# In Windows, \r\n denotes carriage return (\n in Linux)
# Reference: https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
# Reference: https://docs.python.org/3/library/string.html#format-specification-mini-language

Labels='cycle,gene copies'
np.savetxt('pcr_dat_3.csv',pcr_dat,fmt=['%.3f','%.4f'],delimiter=',',newline='\r\n',header=Labels)

''' #5. Format console output '''
np.set_printoptions(precision=4,threshold=1000,edgeitems=4,suppress=True)
# precision: # of decimal places (default is 8)
# threshold: # of items in list before it is summarized, e.g., ...,
# edge:      # of items showns when summarized for each dimension
# suppress:  suppress = true prints #'s in simplest form, i.e., int or decimal vs. scientific notation
print(np.arange(25))
# similar to Python 'range'
# arguments: np.arange([start, ],stop,[step,],dtype=none)
# argument step defaults to 1
# arguments are positional: np.arange(1,10,3) == np.arange(start=1,stop=10,step=3)
# argument dtype: all elements same data type.  Use array.dtype to query
np.set_printoptions(precision=4,threshold=25,edgeitems=3,suppress=False)
print(np.arange(25))
print(sensor_data)
np.set_printoptions(precision=3,edgeitems=3,suppress=True)
print(sensor_data)

np.set_printoptions(precision=4,threshold=25,edgeitems=3,suppress=True)
print(pcr_dat)

''' #6. File object: open/use/close '''
# Reference: https://sites.pitt.edu/~naraehan/python3/reading_writing_methods.html
# Recursively write data (in for Loop) to a file (data) object
myfile = open('pH_sensor.txt','r')
# creates file object; 'r' for read (default - can be omitted); 'w' for write; 'a' for append
myfile.close()
# closes file

with open("PLJM1_SD1_std_curve_2.csv", "r") as f:
    print(f.read())
f.close()

with open("PLJM1_SD1_std_curve_2.csv", "r") as f:
    pcrdat=f.read()
f.close()
print(pcrdat)
#   file of string variables

pcr_dat_o = open("pcr_dat_o.csv", "w")
pcr_dat_o.writelines(pcr_dat)
pcr_dat_o.close


''' #7. Encoding '''
# Reference: https://www.programiz.com/python-programming/methods/string/encode
# read a particular encoding type, or write one
myfile = open('pH_sensor.txt', 'r',encoding = 'utf-8')
# Python uses utf-8 (8-bit Unicode) by default.  Common also are utf-16, utf-32 (32-bit)
myfile = open('results.txt', 'w',encoding = 'utf-8')
# Command: string.encode()  re-encodes differently
## Script:
# unicode string
string = 'pythön!'
# https://unicode-table.com/en/00FC/
# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

## Script Output
#The string is: pythön!
#The encoded version is: b'pyth\xc3\xb6n!'
