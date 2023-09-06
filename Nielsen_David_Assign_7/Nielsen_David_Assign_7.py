# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct 26 14:17:19 2022

# @author: a02271494
# """

import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib import cm 

file = open('2-D.txt', 'wb')
file.write('2_D.txt - finite difference \r\n'.encode())

box = np.zeros([2,11,21]) # t, y, x
data = np.zeros([7,11,21])

for x in range(10):
    box[:,:,0] = 30 # rows down, y, j
    box[:,:,-1] = 30
    box[:,0,:] = 30 # columns across, x, i
    box[:,-1,:] = 30

np.set_printoptions(linewidth=1000, precision = 2)
 

alpha = 0.252*10**(-4) # square meters per day (thermal diffusivity)
dx = 0.001 # meters, 1,2,3-D distance step, i variable, columns
dy = 0.001 # meters, 2,3-D distance step, j variable, rows
dt = (dx**2)/(2*alpha)/2 # smallest stable time step for 1-D rod
dT = round(alpha * dt/(x*x),6)
x = 0.02 # meters, 1,2,3-D distance step (discretized into x/dx steps of dx m each), i variable, columns
y = 0.01 # meters, 2,3-D distance step (discretized into y/dy steps of dy m each), j variable, rows
t = 0
n = 0

temperatureCheckpoints = [5,10,15]
checkpoint = 0
while box[0,int(int(y/dy+1)/2),int(int(x/dx+1)/2)] < 20:
    t += 1
    for j in range(1,int(y/dy)):
        for i in range(1,int(x/dx)):
            box[1,j,i] = box[0,j,i] + alpha * ( (box[0,j+1,i] - 2*box[0,j,i] + box[0,j-1,i]) / dx**2 
                                                +   (box[0,j,i+1] - 2*box[0,j,i] + box[0,j,i-1]) / dy**2 ) * dt
    box[0] = box[1]
    
    if checkpoint < 3 and box[0,int(int(y/dy+1)/2),int(int(x/dx+1)/2)] > temperatureCheckpoints[checkpoint]:
        file.write(str('{:.4f}'.format(t * dt)).encode() + ','.encode()) # formats write to output file
        np.savetxt(file, np.atleast_2d(box[0,:,:]), fmt='%.4f', delimiter=', ', newline = '\r\n') # writes to output file
        print(data[n,int(y/dy/2),int(x/dx/2)]) # progress of diffusion
        checkpoint += 1
        n += 1
        data[n] = box[0] # saves data for surface plots
file.write(str('{:.4f}'.format(t * dt)).encode() + ','.encode()) # formats write to output file
np.savetxt(file, np.atleast_2d(box[0,:,:]), fmt='%.4f', delimiter=', ', newline = '\r\n') # writes to output file
print(data[n,int(y/dy/2),int(x/dx/2)]) # progress of diffusion
checkpoint += 1
n += 1
data[n] = box[0] 
print('Time: ' + str(t) + ' days')

for k in range(0,n):
# https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html
    fig = plt.figure()
    xaxis = ([])# initialize distance along the x axis (columns, i) to plot it
    yaxis = ([])# initialize distance along the y axis (rows, j) to plot it
    for i in range(int(x/dx+1)): #initialize x-axis (j,columns) for plot
        xaxis.append(round(i*dx,4))
    for j in range(int(y/dy+1)): #initialize y-axis (i,rows) for plot
        yaxis.append(round(j*dy,4))
    #print('cols',xaxis,'rows', yaxis)
    ax = plt.axes(projection = '3d')
    ax.set_box_aspect(aspect = (1,1,1)) #scale axes to match ranges
    # https://stackoverflow.com/questions/30223161/matplotlib-mplot3d-how-to-increase-the-size-of-an-axis-stretch-in-a-3d-plo#
    xaxis,yaxis=np.meshgrid(xaxis,yaxis)
    z=data[k,:,:]
    surf = ax.plot_surface(xaxis,yaxis,z, rstride=1, cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)
    # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    fig.colorbar(surf)   








file2 = open('2-D2.txt', 'wb')
file2.write('2_D2.txt - finite difference \r\n'.encode())

box = np.zeros([2,11,41]) # t, y, x
data = np.zeros([7,11,41])

for x in range(10):
    box[:,:,0] = 30 # rows down, y, j
    box[:,:,-1] = 30
    box[:,0,:] = 30 # columns across, x, i
    box[:,-1,:] = 30

np.set_printoptions(linewidth=1000, precision = 2)
 

alpha = 0.252*10**(-4) # square meters per day (thermal diffusivity)
dx = 0.01 # meters, 1,2,3-D distance step, i variable, columns
dy = 0.01 # meters, 2,3-D distance step, j variable, rows
dt = (dx**2)/(2*alpha)/2 # smallest stable time step for 1-D rod
dT = round(alpha * dt/(x*x),6)
x = 0.4 # meters, 1,2,3-D distance step (discretized into x/dx steps of dx m each), i variable, columns
y = 0.1 # meters, 2,3-D distance step (discretized into y/dy steps of dy m each), j variable, rows
t = 0
n = 0


temperatureCheckpoints = [5,10,15]
checkpoint = 0

while box[0,int(int(y/dy+1)/2),int(int(x/dx+1)/2)] < 20:
    t += 1
    for j in range(1,int(y/dy)):
        for i in range(1,int(x/dx)):
            box[1,j,i] = box[0,j,i] + alpha * ( (box[0,j+1,i] - 2*box[0,j,i] + box[0,j-1,i]) / dx**2 
                                                +   (box[0,j,i+1] - 2*box[0,j,i] + box[0,j,i-1]) / dy**2 ) * dt
    box[0] = box[1]
    if checkpoint < 3 and box[0,int(int(y/dy+1)/2),int(int(x/dx+1)/2)] > temperatureCheckpoints[checkpoint]:
        file2.write(str('{:.4f}'.format(t * dt)).encode() + ','.encode()) # formats write to output file
        np.savetxt(file, np.atleast_2d(box[0,:,:]), fmt='%.4f', delimiter=', ', newline = '\r\n') # writes to output file
        print(data[n,int(y/dy/2),int(x/dx/2)]) # progress of diffusion
        checkpoint += 1
        n += 1
        data[n] = box[0] # saves data for surface plots
        
file.write(str('{:.4f}'.format(t * dt)).encode() + ','.encode()) # formats write to output file
np.savetxt(file, np.atleast_2d(box[0,:,:]), fmt='%.4f', delimiter=', ', newline = '\r\n') # writes to output file
print(data[n,int(y/dy/2),int(x/dx/2)]) # progress of diffusion
checkpoint += 1
n += 1
data[n] = box[0] 


print('Time: ' + str(t) + ' Days')
for k in range(0,n):
# https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html
    fig = plt.figure()
    xaxis = ([])# initialize distance along the x axis (columns, i) to plot it
    yaxis = ([])# initialize distance along the y axis (rows, j) to plot it
    for i in range(int(x/dx+1)): #initialize x-axis (j,columns) for plot
        xaxis.append(round(i*dx,4))
    for j in range(int(y/dy+1)): #initialize y-axis (i,rows) for plot
        yaxis.append(round(j*dy,4))
    #print('cols',xaxis,'rows', yaxis)
    ax = plt.axes(projection = '3d')
    ax.set_box_aspect(aspect = (1,1,1)) #scale axes to match ranges
    # https://stackoverflow.com/questions/30223161/matplotlib-mplot3d-how-to-increase-the-size-of-an-axis-stretch-in-a-3d-plo#
    xaxis,yaxis=np.meshgrid(xaxis,yaxis)
    z=data[k,:,:]
    surf = ax.plot_surface(xaxis,yaxis,z, rstride=1, cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)
    # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    fig.colorbar(surf)  








file3 = open('3-D cuboid.txt', 'wb')
file3.write('3-D cuboid - finite difference \r\n'.encode())

k = 386  # watts per meter per degree C at 20 deg C(thermal conductivity)
rho = 896 # kilograms per cubic meter at 20 deg C (density)
Cp = 380 # Joules per kilogram per degree Kelvin at 20 deg C (heat capacity) 

alpha = k/(rho*Cp) # square meters per second (thermal diffusivity)

dx = 0.01 # meters, 1,2,3-D distance step, i variable, columns
dy = 0.01 # meters, 2,3-D distance step, j variable, rows
dz = 0.01 # ,metersm 3-D distance step, k variable, planes
x = 0.2 # meters, 1,2,3-D distance step (discretized into x/dx steps of dx m each), i variable, columns
y = 0.2 # meters, 2,3-D distance step (discretized into y/dy steps of dy m each), j variable, rows
z = 0.2 # meters, 3-D distance step (discretized into z/dz steps of dz m each), k variable, planes

dt = 0.01

box = np.zeros([2,21,21,21])  # box, slice, column, row
data = np.zeros([7,21,21,21])
for p in range(4):
   box[:,0,0:-1,:] = 25 
   box[:,-1,0:-1,:] = 25 
   box[:,1:-1,1:-1,1:-1] = 4
   box[:,:,0,:] = 25 
   box[:,:,0,0] = 5 
   box[:,:,:-1,0] = 25 
   box[:,:,:-1,-1] = 25 
   box[:,:,-1,:] = 51 


t = 0
n = 0
checkpoint = 0
checkpointlist = [5,10,15]


while box[0,int(z/dz/2),int(y/dy/2),int(x/dx/2)]<20:
    
    t += 1
    for i in range(1,int(x/dx)):
        for j in range(1,int(y/dy)):
            for k in range(1,int(z/dz)):
                box[1,k,i,j] = box[0,k,i,j] + alpha * ((box[0,k-1,i,j] - 2 * box[0,k,i,j] + box[0,k+1,i,j])/ dz**2 +
                                                         (box[0,k,i-1,j] - 2 * box[0,k,i,j] + box[0,k,i+1,j])/ dy**2 +
                                                         (box[0,k,i,j-1] - 2 * box[0,k,i,j] + box[0,k,i,j+1])/ dx**2) * dt
    box[0] = box[1]
    if checkpoint < 3 and np.min(box) > checkpointlist[checkpoint]:
        checkpoint += 1
        file3.write(str('{:.4f}'.format(t * dt)).encode() + ','.encode()) # formats write to output file3_var
        np.savetxt(file3, np.atleast_2d(box[0,10,:,10]), fmt='%.4f', delimiter=', ', newline = '\r\n') # writes to output file3_var
        data[n,:,:,:] = box[0,:,:,:] # saves data for surface plots
        file3.write('\r\n'.encode()) 
        n+=1
        print(np.min(box))  
     
file3.write(str('{:.4f}'.format(t * dt)).encode() + ','.encode()) # formats write to output file3_var
np.savetxt(file3, np.atleast_2d(box[0,10,:,10]), fmt='%.4f', delimiter=', ', newline = '\r\n') # writes to output file3_var
data[n,:,:,:] = box[0,:,:,:] # saves data for surface plots
file3.write('\r\n'.encode()) 
n+=1
 
np.set_printoptions(precision = 0, linewidth=(1000), suppress = True)                
print(box[0][int(z/dz/2)])
print('time (s) =',t*dt)


print(n)

plt.figure(1) #open the plot   
# initialize the plot axes

for m in range(0,n):
# https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d') # set up axes for the plot
    xaxis = ([])# initialize distance along the x axis (columns, j) to plot it
    yaxis = ([])# initialize distance along the y axis (rows, i) to plot it
    for i in range(int(x/dx)+1): #initialize x-axis (i,columns) for plot
        xaxis.append(round(i*dx,4))
    for j in range(int(y/dy)+1): #initialize y-axis (j,rows) for plot
        yaxis.append(round(j*dy,4))
    #print('cols',xaxis,'rows', yaxis)
    xaxis,yaxis=np.meshgrid(xaxis,yaxis)
    zaxis=data[m,int(z/dz/2),:,:]
    surf = ax.plot_surface(xaxis,yaxis,zaxis, rstride=1, cstride=1, cmap=cm.YlGn,
                       linewidth=0, antialiased=False)
    fig.colorbar(surf)    