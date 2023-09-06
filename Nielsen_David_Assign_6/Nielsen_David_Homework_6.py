
#problem 1
import numpy as np
import math
import matplotlib.pyplot as plt

def topRow(deltax, arraySize):
    array = np.zeros(arraySize)
    x = 0
    for i in range(1,len(array[0])):
        if 0 <= x < 0.5:
            U = 2*x
        else:
            U = 2*(1-x)
            
        array[0,i] = U
        x += deltax
    return array
def writeToFile(f, array, i, time):
    #f.write(str('{:.3f}'. format(time)).encode()+ ', '.encode())
    np.savetxt(f, np.atleast_2d(array[i,:]), fmt='%.4f', delimiter=', ', newline = '\r\n')
def problem1():
    file = open('L06_fin_diff.txt', 'wb')
    file.write('Lesson 6: Dimensionless heat transfer - finite difference \r\n'.encode())
    time, deltaT, alpha, deltax = 0,0.001, 1, 0.1
    
    dt = alpha*deltaT
    r = dt/(deltax**2)
    u = topRow(deltax, [21,12])
    writeToFile(file, u, 0, time) 
    time += deltaT
    #===Starting Calculations and Initial Set-Up
    
    for i in range(1,len(u)):
        u[i,0] = time
     
        for j in range(2,len(u[i])-1):
            u[i,j] = r*u[i-1,j-1]+(1-2*r)*u[i-1,j]+ r*u[i-1,j+1]
        time += deltaT    
        writeToFile(file, u, i, time)  
    file.close()
def problem2():
    file2 = open('L06_exact.txt', 'wb')
    file2.write('Lesson 6: Dimensionless heat transfer - exact \r\n'.encode())
    time, deltaT, alpha, deltax = 0, 0.001, 1, 0.1
    dt = alpha*deltaT
    u = topRow(deltax, [21,12])
    #Saving initial values to top row
    writeToFile(file2, u, 0, time)
    
    #the exact solution algorithm 
    for i in range(1,21):
        time = i * dt/alpha
        u[i,0] = time
        for j in range(1,12):
            for n in range(1,101):
                u[i,j] += math.sin(.5*n*math.pi)*math.sin(n*math.pi*((j-1)/10))*math.exp(-(n**2)*((math.pi)**2)*time)/(n**2)
            u[i,j] *= (8/(math.pi**2))
        #Saving each row to a text file
        time += deltaT
        writeToFile(file2, u, i, time)
          
    file2.close()
def problem3():
    
    plt.figure(1) #open the plot 
    file3 = open('L06_problem3.txt', 'wb')
    file3.write('Lesson 6: Dimensionless heat transfer - problem 3 \r\n'.encode())
    #variables
    k, Rho, Cp = 54, 7800, 460
    alpha = k/(Rho*Cp)
    time, deltaT, alpha, deltax = 0, 1, k/(Rho*Cp), 0.1
    dt = alpha*deltaT # smallest stable time step
    r = dt/(deltax**2)
    u = np.zeros([2,12])
    
    
    # These x value will be used in the chart
    x = []  # initialize distance along the rod (to plot it)
    for i in range(int(1/deltax)+1):
        x.append(round(i*deltax,4))
    
    #setting the initial values    
    for i in range(2,len(u[0])-1): 
        u[0,i] = 100
    
    
    # While the center of the rod is greater than 20 Celsius, the problem keeps iterating
    while(u[0,6] > 20):
        time += deltaT
        
        u[1,0] = time
        for j in range(2,len(u[0])-1):
            u[1,j] = r*u[0,j-1]+(1-2*r)*u[0,j]+ r*u[0,j+1] 
        
        if time%100 == 0 :
            strng = str(round(time, 4))
            #adding each row to a chart and to the plot
            plt.plot(x[:],u[1,1:], linewidth = 1, ms = 5, label=strng)
            writeToFile(file3, u, 1, time)
        u[0] = u[1]
    file3.close
    plt.title("rod cooling")          # Plot title
    plt.xlabel("X (meters)")                   # x axis label
    plt.ylabel("T (fraction of $\\mathregular{T_{o}}$)")                   # y axis label
     
    
    print(u)
    
if __name__ == "__main__":
    problem1()
    problem2()
    problem3()




