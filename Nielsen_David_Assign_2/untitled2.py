# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:07:57 2022

@author: DAVID
"""
import numpy as np
import matplotlib.pyplot as plt

F = 1
Xo = 1
X = 1
Vr = 1000
ug = 0.8
kd = 0
dt = 0.05
D = 0.058

S = 19
So = 19
Ks = 0.8
time = 0


hoursOfOperation = 70

#X = Xo*exp(ug*t)
growthArray = []
biomassInEffluent = D*X*dt
substrateInEffluent = D*S*dt

for i in range(int(hoursOfOperation/dt)):

    growthArray.append([time,X,S])#,biomassInEffluent,substrateInEffluent])
    time += dt
    
    # dx/dt * 1/yxs
   
    # hey = 
    S += (D*So - D*S - ug*S)*dt 
    X += (-X*D + X*ug)*dt 
    #biomassInEffluent = D*Xo*dt - X*D*dt
    
    #substrateInEffluent = D*So*dt - D*S*dt
    kd = np.log(X/Xo)
    ug = 1.6*S/(Ks+S)-kd
    # if int(time) == 50:
    #     S = 19
    
growthArray = np.array(growthArray)
print(growthArray)
#setting up to plot two sets of data onto one graph
fig, ax1 = plt.subplots(1)
#prey data is set to the color blue
biomass, = plt.plot(growthArray[:,0],growthArray[:,1], c = 'blue')
#indicating that prey and predator will have the same x value 
#ax2 = ax1.twinx()
#predator data is plotted and set to the color red
substrate, = ax1.plot(growthArray[:,0],growthArray[:,2], c = 'red')
# biomassInEf, = ax1.plot(growthArray[:,0],growthArray[:,3], c = 'purple')
# substrateInEf, = ax1.plot(growthArray[:,0],growthArray[:,4], c = 'orange')
# Inclusion of title, and labeling the axis
plt.title('Predator Prey Model')
ax1.set_ylabel('Concentration')
ax1.set_xlabel('Hours')
#ax2.set_ylabel('Predator Population', color = 'red')
#addition of a legend
#ax1.legend((biomass,substrate,biomassInEf, substrateInEf),('Biomass','Substrate', 'Biomass in effluent', 'Substrate in Effluent'), loc = 'lower center')
ax1.legend((biomass,substrate),('Biomass','Substrate'), loc = 'lower center')
    # print('Time = ' + str(time))
    # print('X = ' + str(X))
    # print('S =' +  str(S))