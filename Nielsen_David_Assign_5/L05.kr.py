# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:12:33 2022

@author: Keith Roper
"""
' Data Visualization with matplotlib '

#import packages
import math as mt
import matplotlib.pyplot as plt
# pyplot tutorial: https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import numpy as np

' Scatter Plots '
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
xv=[x for x in range(1,11)]
yv=[y**3 for y in range(1,11)]
yv2 = [y**2 for y in range(1,11)]
plt.scatter(xv,yv)
# separate figures
# plt.show()

'Line plots '
plt.plot(xv,yv); plt.show()

#plot features
# Note: compile/execute these commands simultaneously with plot command to occur on same graph
plt.plot(xv,yv,color='red');plt.show()
plt.plot(xv,yv,color='red',linewidth='5'); plt.show()
plt.scatter(xv,yv,s=80,color='blue',marker="v"); plt.show()
plt.scatter(xv,yv,s=120,color='purple',marker="<",alpha=0.3); #plt.show()
# alpha: blending value between 0 (transparent) and 1 (opaque)

#labels
plt.title('plot of purple'); plt.xlabel('x'); plt.ylabel('x^3')

#ranges
plt.xlim([1,15])
plt.ylim([-100,1250])

# tick marks
plt.yticks([y for y in range(0,1250,100)])
plt.xticks([x for x in range(14)])

' Muliple data sets on same figure'
# Example 1 - exponential values of x
# simultaneous scatter plots
plt.figure(1)                                       # Create Figure 1
plt.plot(xv, yv, c="blue", marker="D", label="x^3")        # Plot (x^3 vs x)
plt.plot(xv, yv2, c="red", marker="+", label="x^2")     # Plot (x^2 vs x)
plt.title("square and cube of x")           # Plot title
plt.xlabel("x")                            # x axis label
plt.ylabel("powers of x")                   # y axis label
plt.legend(loc=0)                                   # Place legend in "best" spot
# alternatives: loc = 'upper right'; loc = 'upper left'

# Example 2 - simpler exponential values of x
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# Example 3 - subplots
# subplots
hrs=[x for x in range(13)]
v1=[mt.log(y)*2.0 for y in range(1,14)]
v2=[(mt.log10(z))**2.0 for z in range(1,14)]
ta=np.array([hrs,v1,v2])
print(ta)
print(ta[1:,2])
varray = np.transpose(np.array([hrs,v1,v2]))
print(varray)
print(varray[:,1])
print(varray[:,2])
plt.scatter(varray[:,0],varray[:,1],s=60,color='green')
fig,(sf1,sf2)=plt.subplots(1,2)
sf1.scatter(varray[:,0],varray[:,1],s=60,color='green')
sf2.scatter(varray[:,0],varray[:,2],s=40,color='orange')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.scatter(varray[:,0],varray[:,1],s=60,color='green')
ax2.scatter(varray[:,0],varray[:,2],s=40,color='orange')
ax3.scatter(varray[:,0],varray[:,1],s=60,color='red')
ax4.scatter(varray[:,0],varray[:,2],s=40,color='yellow')

' Surface plots'
#Surface Plots No. 1 - create data inline
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))

# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

#Surface Plots No. 2 - import data
surf_data=np.loadtxt('surface_plot_practice.csv',delimiter=',')
np.set_printoptions(precision=2,threshold=1000,edgeitems=4,suppress=True)
print(surf_data)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x=surf_data[0,1:]
y=surf_data[1:,0]
z=surf_data[1:,1:]
x,y=np.meshgrid(x,y)
from matplotlib import cm
surf_plot=ax.plot_surface(x,y,z,cmap=cm.YlGn)
fig.colorbar(surf_plot)

