import sys
import pandas as pd

if __name__ == "__main__":
    VehicleConvergeTime = {}
    ScenarioList = []
    fp = open("list.txt","r")
    line = fp.readline()
    line = line.strip('\n')
    while line:
        ScenarioList.append(line)
        line = fp.readline()
        line = line.strip('\n')
    fp.close()

    for i in range(len(ScenarioList)):
        if ScenarioList[i] == 'vid':
            VehicleConvergeTime[ScenarioList[i]] = ['','0','1','2','3','4','5','6','7','','0','1','2','3','4','5','6','7','','0','1','2','3','4','5','6','7']
            continue
        
        VehicleConvergeTime[ScenarioList[i]] = []
        fp = open(ScenarioList[i]+"/settlingTime","r")
        VehicleData = []
        line = fp.readline()
        line = line.strip('\n')
        while line:
            if line == '179.91':
                VehicleData.append('Never')
            else:
                VehicleData.append(line)
            line = fp.readline()
            line = line.strip('\n')
        fp.close()
        VehicleConvergeTime[ScenarioList[i]] = VehicleData

    df = pd.DataFrame(data=VehicleConvergeTime)
    
    df.to_csv('settlingTime.csv',index=False)
