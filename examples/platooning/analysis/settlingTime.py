import pandas as pd
import sys

if __name__=='__main__':
    VehicleDynamic = pd.read_csv(sys.argv[1]+"/output.csv");
    
    time = VehicleDynamic['time'].values.tolist()
    distance = VehicleDynamic['distance'].values.tolist()
    nodeId = VehicleDynamic['nodeId'].values.tolist()
    speed = VehicleDynamic['speed'].values.tolist()

    distanceConverge = [0]*8
    speedConverge = [0]*8
    ess = [0]*8

    targetSpeed = 100/3.6
    targetDistance = 80/3.6+15

    for i in range(len(time)):
        if time[i] == 179.91:
        	ess[nodeId[i]] = distance[i]

    for i in range(len(time)):

        if speed[i] >= targetSpeed*1.05 or speed[i] <= targetSpeed*0.95 :
            if time[i] > speedConverge[nodeId[i]]:
                speedConverge[nodeId[i]] = time[i]

        if nodeId[i]==0:
            continue

        if distance[i] >= ess[nodeId[i]]*1.05 or distance[i] <= ess[nodeId[i]]*0.95:
            if time[i] > distanceConverge[nodeId[i]]:
                distanceConverge[nodeId[i]] = time[i]

    fp = open(sys.argv[1]+"/settlingTime","w")

    print >> fp,'speed'
    for i in range(len(speedConverge)):
        print >> fp,str(speedConverge[i])

    print >> fp,'distance'
    for i in range(len(distanceConverge)):
        print >> fp,str(distanceConverge[i])
    
    print >> fp,'ess'
    for i in range(len(ess)):
#        if i==0 or ess[i]-targetDistance<0.001:
#        ess[i]=targetDistance
        print >> fp,str((ess[i]-targetDistance))
    
    fp.close()

