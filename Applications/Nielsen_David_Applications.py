# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:07:57 2022

@author: DAVID
"""

import numpy as np
import matplotlib.pyplot as plt

#importing data from the literature. Below is the column index for relevant data for modeling and comparison
# [:, 0] = Dilution Rate
# [:, 1] = Effective Glucose in Feed
# [:, 2] = Glucose in Effluent
# [:, 3] = SA in Effluent   
# [:,-2] = Yield of Biomass from Substrate
# [:,-3] = Yield of Product from Substrate

PP_data = [[ 0.146, 19.4,  12.4,    5.,     1.4,    0.6,    0.38,   1.9,    0.71,   0.125,  0.73 ],
 [ 0.146, 19.4,   12.7,    4.7,    1.4,    0.5,    0.,     1.7,    0.7 ,   0.13 ,  0.68 ],
 [ 0.093, 19. ,    6.6,    9.2,    2.5,    0.6,    0.34,   1.9,    0.74,   0.159,  0.85 ],
 [ 0.093, 19. ,    6.4,    9.3,    2.5,    0.6,    0.  ,   1.9,    0.74,   0.128,  0.87 ],
 [ 0.187, 19.8,   15.8,    2.5,    0.8,    0.3,    0.51,   1.5,    0.62,   0.171,  0.46 ],
 [ 0.06 , 49.4,   33.9,   11.9,    3. ,    0.5,    0.44,   2. ,    0.77,   0.078,  0.71 ],
 [ 0.06 , 49.2,   33.9,   11.5,    3. ,    0.3,    0.  ,   2. ,    0.75,   0.079,  0.69 ],
 [ 0.093, 48.9,   39. ,    7. ,    1.8,    0.3,    0.37,   2. ,    0.7 ,   0.077,  0.65 ],
 [ 0.093, 49. ,   39.6,    6.3,    1.7,    0.4,    0.37,   1.9,    0.67,   0.107,  0.59 ],
 [ 0.043, 47.9,   30.3,   13.4,    3.5,    0.3,    0.  ,   2. ,    0.76,   0.08 ,  0.58 ],
 [ 0.043, 48.3,   30.7,   13.3,    3.6,    0.3,    0.54,   1.9,    0.76,   0.081,  0.57 ],
 [ 0.021, 47.3,   23.5,   18. ,    4.7,    0.8,    0.49,   2. ,    0.76,   0.061,  0.38 ],
 [ 0.021, 47.3,   22.8,   17.3,    4.4,    0.3,    0.6 ,   2. ,    0.71,   0.063,  0.36 ]]

comparisonArray = []
for e in range(2,len(PP_data)):

    D = PP_data[e][0] #Dilution
    So = PP_data[e][1] #Influent Concentration
    S = So #
    Xo = 0.5 #this is the initial concentration of biomass in the reactor (g/L)
    X = 0.5 # this is the initial concentration of the effluent and will be adjust (g/L)
    P = 0 #this is the initial amount of product within effluent (g/L)
    ug = 0.22 #growth rate
    kd = 0 #cell death rate
    dt = 0.05 #hrs
    Ysx = PP_data[e][-2] # the yield of biomass from substrate
    Ysp = PP_data[e][-3] # the yield of product from substrate
    
    GlucoseInEffluentActual = int(PP_data[e][2]) #literature value of effluent glucose (g/L)
    SAInEffluentActual = int(PP_data[e][3]) #literature value for effluent product (g/L)
    
    umax = 1.5 # the maximum growth rate of the cells, I guessed this value
    Ks = 0.7 # concentration that is 1/2 umaxg/L
    time = 0
    
    
    hoursOfOperation = 250 #hrs the reactor was run in the literature
    
    #X = Xo*exp(ug*t)1.2*S/(Ks+S)v1.2*S/(Ks+S)
    growthArray = []
    #This loop goes through each differential and calculates ug with is the net 
    #growth rate for the cells, kd is the death rate of cells and is an important
    #term in calculating ug. ug is also calculated with the substrate concentration
    #as the availability of Substrate increases the growth rate approaches umax
    #Product formation, biomass growth, and substrate concentration rely on ug
    #which contributes to biomass accumulation in the reactor. Eventually Dilution (D)
    #Which is the inverse of hydrolic retention time drives the reaction to steady
    #state which means eventually dS/dt, dX/dt, and dP/dt approach 0
    for i in range(int(hoursOfOperation/dt)):
    
        growthArray.append([time,X,S,P])#,biomassInEffluent,substrateInEffluent])
        time += dt
        kd = np.log(X/Xo) #coefffeint of cell death
        ug = 1.5*S/(Ks+S) - kd
        S += (D*So - D*S - ug*X)*dt # substrate concentration
        X += (-X*D + X*ug*Ysx)*dt # Biomass concentration
        P += (-P*D + X*ug*Ysp)*dt # Product concentration
      
        
    print('Dilution: ' + str(D) + '/hr')
    print('Influent Glucose Concentration: ' + str(So) + 'g/L')
    print('Theoretical effluent salicilic acid concentration ' + str(P) + 'g/L')
    print('Actual effluent salicilic acid concentration: '+ str(SAInEffluentActual) )
    print('Theoretical effluent glucose concentration ' + str(S))
    print('Actual effluent glucose concentration: '+ str(GlucoseInEffluentActual))
    print()
    comparisonArray.append([D,So,P,SAInEffluentActual,S,GlucoseInEffluentActual])
    growthArray = np.array(growthArray)


    #the creation of the charts for each of the parameters determined by literature
    #NAMELY So, or influent glucose concentration, and D, dilution. 
    fig, ax1 = plt.subplots(1)
    substrate, = plt.plot(growthArray[:,0],growthArray[:,2], c = 'blue')
    ax2 = ax1.twinx()
    biomass, = ax2.plot(growthArray[:,0],growthArray[:,1], c = 'red')
    product, = ax1.plot(growthArray[:,0],growthArray[:,3], c = 'purple')
    plt.title('CSTFR with ' + str(D) + "/hr Dilution")
    ax1.set_ylabel('Glucose/Salicilic Acid (g/L)', color = 'blue')
    ax1.set_xlabel('Hours')
    ax2.set_ylabel('Biomass (g/L)', color = 'red')
    ax1.legend((biomass,substrate, product),('Effluent Biomass','Effluent Substrate', 'Effluent Product'), loc = 'lower center')
        # print('Time = ' + str(time))
        # print('X = ' + str(X))
        # print('S =' +  str(S))
comparisonArray = np.array(comparisonArray)       


#A chart that compares dilution with the literature for effluent substrate/glucose concentration
fig, ax1 = plt.subplots(1)
SAactual = ax1.scatter(comparisonArray[:,0],comparisonArray[:,2], c = 'red')
SAmodel = ax1.scatter(comparisonArray[:,0], comparisonArray[:,3], c = 'orange')
ax1.legend((SAactual,SAmodel),('Literature Values','Model Values'), loc = 'upper right')
ax1.set_xlabel('Dilution (1/hr)')
ax1.set_ylabel('Glucose Effluent (g/L)')
plt.title('Literature vs. Model Comparison of Effluent Substrate concentration')
texts = []
for i, txt in enumerate(comparisonArray[:,1]):
    if txt not in texts:
        ax1.annotate('So= ' + str(txt), (comparisonArray[i,0], comparisonArray[i,2]))
        texts.append(txt)
  
    
#A chart that compares dilution with the literature for effluent product/salicilic concentration @ Steady State
        ax1.annotate('So = ' + str(txt), (comparisonArray[i,0], comparisonArray[i,2]))
        #ax1.annotate('So = ' + str(txt), (comparisonArray[i,0], comparisonArray[i,3]))
fig, ax1 = plt.subplots(1)
SAactual = ax1.scatter(comparisonArray[:,0],comparisonArray[:,4], c = 'red')
SAmodel = ax1.scatter(comparisonArray[:,0], comparisonArray[:,5], c = 'orange')
ax1.legend((SAactual,SAmodel),('Literature Values','Model Values'), loc = 'upper right')
ax1.set_xlabel('Dilution (g/L)')
ax1.set_ylabel('Salicilic Acid Effluent (g/L)')
plt.title('Literature vs. Model Comparison of Effluent Product concentration')
texts = []
for i, txt in enumerate(comparisonArray[:,1]):
    if txt not in texts:
        ax1.annotate('So= ' + str(txt), (comparisonArray[i,0], comparisonArray[i,4]))
        texts.append(txt)
        
        
#A chart that compares literature values with modeled values for effluent glucose at Steady State            
fig, ax1 = plt.subplots(1)
SA = ax1.scatter(comparisonArray[:,2],comparisonArray[:,3], c = 'red')
ax1.set_xlabel('Literature Effluent Glucose (g/L)')
ax1.set_ylabel('Model Effluent Glucose (g/L)')
plt.title('Literature vs. Model Comparison of Effluent Glucose concentration')

#A chart that compares literature values with modeled values for effluent Salicilic Acid at Steady State            
fig, ax1 = plt.subplots(1)
SA = ax1.scatter(comparisonArray[:,4],comparisonArray[:,5], c = 'red')
ax1.set_xlabel('Literature Effluent SA (g/L)')
ax1.set_ylabel('Model Effluent SA (g/L)')
plt.title('Literature vs. Model Comparison of Effluent Product concentration')