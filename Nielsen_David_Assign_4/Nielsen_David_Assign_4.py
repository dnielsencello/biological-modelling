import numpy as np
sensor_data=np.loadtxt('mv_Sensor.csv',delimiter=',')
sensor_data[0:,0],sensor_data[0:,1] = [1000*sensor_data[i][0] for i in range(len(sensor_data))],[sensor_data[i][1]/290 for i in range(len(sensor_data))]
np.set_printoptions(precision=3,threshold=1000,edgeitems=4,suppress=True)
print(sensor_data)

np.savetxt('pH_Sensor.csv',sensor_data,fmt=['%.f','%.3f'],delimiter=',',newline='\n',header='milliters base ,pH level')
sensor_data=np.loadtxt('Bacterial_Growth.csv',delimiter=',')
sensor_data[0:,1]= [((sensor_data[i][1]+sensor_data[i][2]+sensor_data[i][3]+sensor_data[i][4])/4) for i in range(len(sensor_data))]
for i in range(3):
    sensor_data = np.delete(sensor_data,2,1)
print(sensor_data)   
np.set_printoptions(precision=3,threshold=1000,edgeitems=4,suppress=True) 
np.savetxt('Avg_Growth.csv',sensor_data,fmt=['%.f','%.f'],delimiter=',',header='Hours,Growth Average')
r, s, k, A, h, No, Po, yearOfDrought, harePopulationAfterDrought, time, N, P = 0.9, 0.3, 10000, 5, 10, 1000, 100, 101, 2000, 0, 1000, 100 
growthArray = np.zeros([400,3], float)
for i in range(400):
   time,
   N,
   P,
   growthArray[i] = time + 0.25,
   N+ N*(r*(1-N/k)-(A*N*P)/(N**2+No**2))*0.25,
   P +P*(s*(1-h*P/N))*0.25,
   ([time,N,P]) 
   
   
np.savetxt('PredatorPrey.csv',growthArray,fmt=['%.2f','%.f','%.f'],delimiter=',',header='Years,Prey,Predators')
print(growthArray)