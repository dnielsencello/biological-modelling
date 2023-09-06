import numpy as np
import matplotlib.pyplot as plt

#Problem1
#importing the PredatorPrey.csv file and loading it into an np array
PP_data=np.loadtxt('PredatorPrey.txt',delimiter=',')

#setting up to plot two sets of data onto one graph
fig, ax1 = plt.subplots(1)
#prey data is set to the color blue
prey = plt.scatter(PP_data[:,0],PP_data[:,1], c = 'blue', s = 2)
#indicating that prey and predator will have the same x value 
ax2 = ax1.twinx()
#predator data is plotted and set to the color red
predator, = ax2.plot(PP_data[:,0],PP_data[:,2], c = 'red')
# Inclusion of title, and labeling the axis
plt.title('Predator Prey Model')
ax1.set_ylabel('Prey Population',color = 'blue')
ax1.set_xlabel('Years')
ax2.set_ylabel('Predator Population', color = 'red')
#addition of a legend
ax1.legend((prey,predator),('Prey','Predator'), loc = 'lower center')


#Problem2
#Each graph will be loaded from the same set of data, but will be displayed as individual graphs

Stock_data = np.loadtxt('BDX.csv', delimiter = ',')

#Scatter plot of the Open data
#plt.figure() function calls out a new figure to plot onto
plt.figure()
plt.scatter(Stock_data[1:,0],Stock_data[1:,1], c = 'red', s = 3)
Open = plt.plot(Stock_data[1:,0],Stock_data[1:,1])
plt.title('BD Open')
plt.xlabel('Day of the Year')
plt.ylabel('Stock Price $')

#Scatter plot of the High 
plt.figure()
plt.scatter(Stock_data[1:,0],Stock_data[1:,2], c = 'red', s = 3)
high = plt.plot(Stock_data[1:,0],Stock_data[1:,2])
plt.title('BD High')
plt.xlabel('Day of the Year', color = 'blue')
plt.ylabel('Stock Price $')

#Scatter plot of the Low data
plt.figure()
plt.scatter(Stock_data[1:,0],Stock_data[1:,3], c = 'red', s = 3)
low = plt.plot(Stock_data[1:,0],Stock_data[1:,3])
plt.title('BD Low')
plt.xlabel('Day of the Year')
plt.ylabel('Stock Price $')

#Scatter plot of the Volume
plt.figure()
plt.scatter(Stock_data[1:,0],Stock_data[1:,6], c = 'red', s = 3)
Volume = plt.plot(Stock_data[1:,0],Stock_data[1:,6])
plt.title('BD Volume')
plt.xlabel('Day of the Year')
plt.ylabel('Volume')


#Problem3
#importing the 3d surface plot package
from matplotlib import cm

SWR_Data = np.loadtxt('SWR.csv', delimiter = ',')
#naming my plot
fig = plt.figure()
#making fig into a 3d Surface Plot
ax = fig.gca(projection = '3d')

#Specifying axis data
x = SWR_Data[1:,0]
y = SWR_Data[0,1:]
z = SWR_Data[1:,1:]
#specifying the axis parameters
y, x = np.meshgrid(y,x)
surf_plot = ax.plot_surface(x,y,z, cmap = cm.YlGn)
#labelling axis
plt.xlabel('Frequency (MHz)')
plt.ylabel('Length (in.)')
ax.set_zlabel('Reflected Power')
#adding color bar with label
fig.colorbar(surf_plot, pad = 0.2).ax.set_ylabel('Reflected Power Scale')


