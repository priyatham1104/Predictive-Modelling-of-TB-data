# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv, os
import shutil
import numpy as np
import glob
import pandas as pd
from builtins import object
import tensorflow as tf




dir00 = os.getcwd()
dir0 = dir00 + "/pritam_test_2/"
print(dir00)
dir1 = dir0 + "/files/"
dir2 = dir0 + "/folders/"
dir4 = dir0 + "/average samples 180/"
dir5 = dir0 + "/average samples 600/"
time_sample = 600
os.chdir(dir1)
files1 = os.listdir(".")

for fil1 in files1:
    if(fil1.split(".")[1] == "txt"):
        print(fil1)
        os.chdir(dir2)
        h = fil1.split(".")[0]
        if not os.path.exists(h):
            os.mkdir(h)
            os.chdir(dir1)
        dir3 = dir2  + fil1.split(".")[0] + "/"
    # print(os.getcwd())
    # break
        os.chdir(dir1)

        file1 = open(fil1,"r")
        file1_lines = file1.readlines()
        file1.close()
        x = 1
        for x in range(1,2):
            x = x+1
            i = 0
            j = 0
            k = 0
            l = 0
            p = 0
            a = 0
            g = 0
            sampling_rate = 10
            sensorID = []
            

            for line in file1_lines:
                p = p+1
                temp = line.split()
                if len(line.strip().split()) == 0:
                    continue
                if temp[0] == "State" and temp[2] == str(x):
                    k = k+1
            print("number of samples of state " + str(x) + ": " +str(k))
            data = np.zeros((k,343))
            data_2 = np.zeros((int(k/sampling_rate),343))
            data_time = np.zeros((k,7))

            for line in file1_lines:
                a = a+1
                temp = line.split()
                if len(line.strip().split()) == 0:
                    continue
                if temp[0] == "Date":
                    continue
                if temp[0] == "Time":
                    continue
                if temp[0] == "No":
                    continue
                if temp[0] == "Sec":
                    continue
                if temp[0] == "State" and temp[2] == str(x):
                    for line in file1_lines[a+1:a+344]:
                        temp2 = line.split()
                        data[i,j] = temp2[2]
                        j = j+1
                        #print("temp2" + temp2[2])
                    j = 0
                    i = i+1
                    
                    if(x==2): 
                        line_time2 = file1_lines[a-4]
                        line_time = file1_lines[a-3]
                        temp3 = line_time.split(":")
                        temp4 = line_time2.split(":") 
                        line_time3 = temp4[1]
                        temp5 = line_time3.split(".")
                        data_time[g,0] = temp3[1]
                        data_time[g,1] = temp3[2]
                        data_time[g,2] = temp3[3] 
                        data_time[g,3] = temp5[0]
                        data_time[g,4] = temp5[1]
                        data_time[g,5] = temp5[2]
                        data
                        g = g+1
               

            data_time[0,6] = (data_time[g-1,5]-data_time[0,5])*3600*24*30*12 + (data_time[g-1,4]-data_time[0,4])*3600*24*30 + (data_time[g-1,3]-data_time[0,3])*3600*24 + (data_time[g-1,0]-data_time[0,0])*3600 + (data_time[g-1,1]-data_time[0,1])*60 +(data_time[g-1,2]-data_time[0,2])
            data_time[1,6] = k
            if(data_time[0,6]!=0 and k != 0):
                data_time[2,6] = int(data_time[0,6]/time_sample) 
                data_time[3,6] = int(k/data_time[2,6])+1
                data_time[4,6] = (data_time[g-1,5]-data_time[0,5])*3600*24*30*12
                data_time[5,6] = (data_time[g-1,4]-data_time[0,4])*3600*24*30
                data_time[6,6] = (data_time[g-1,3]-data_time[0,3])*3600*24
                data_time[7,6] = (data_time[g-1,0]-data_time[0,0])*3600
                data_time[8,6] = (data_time[g-1,1]-data_time[0,1])*60
                
                
                
            
            if(x==2 and (data_time[2,6]!= 0) and data_time[0,6]!=0 and data_time[3,6]>1):  
                m = k
                print("number of samples:" + " "  + str(k))
                p = int(data_time[2,6]) + 1
                print("number of average samples:" + " " + str(p))
                n = 343
                e = int(m/p)
                print("number of samples per avergae"+ " " + str(e) )
                print()
                data_average = np.zeros((int(data_time[2,6])+1,n))
                a = 0
                b = 0
                for a in range(0,p):
                    data_average[a,:] = np.average(data[b:b+e-1,:], axis=0)
                    a = 1+a
                    b = e*a
                        
            if(x == 2 and data_time[3,6] == 1):
                n = 343
                data_average = np.zeros((k,n))
                data_average = data     
            
            
            
            #print(data)
            os.chdir(dir3)
            #if os.path.exists("state" + str(x) +".csv"):
             #   os.remove("state" + str(x) +".csv")
            np.savetxt("state" + str(x) +".csv", data, delimiter=",")
            
            if(x==2):
                #if os.path.exists("time" + str(x) +".csv"):
                 #   os.remove("time" + str(x) +".csv")
                np.savetxt("time" + str(x) +".csv", data_time, delimiter=",")
                
                #if os.path.exists("state_average" + str(x) + str(time_sample) +".csv"):
                  #  os.remove("state_average" + str(x) + str(time_sample) +".csv")
                np.savetxt("state_average" + str(x) + str(time_sample) +".csv", data_average, delimiter=",")     
                
                os.chdir(dir5) 
                #if os.path.exists("state_average" + fil1.split(".")[0] + str(time_sample) + ".csv"):
                 #   os.remove("state_average" + fil1.split(".")[0] + str(time_sample) + ".csv")
                np.savetxt("state_average" + fil1.split(".")[0] + str(time_sample) + ".csv", data_average, delimiter=",")  
                
     
os.chdir(dir5)
dfList = []
fileList = glob.glob("*.csv")
#print(fileList)
for filename in fileList:
    df = pd.read_csv(filename, header = None)
    dfList.append(df)
concatDf = pd.concat(dfList, axis = 0)  
concatDf.to_csv('final_file.csv', index = None)

