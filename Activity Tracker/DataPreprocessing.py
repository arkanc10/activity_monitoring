# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:13:31 2021

@author: arkan
"""

import pandas as pd
import re
import glob
path = 'C:\\Users\\arkan\\Desktop\\Activity Tracker\\activitydataApr20\\activitydataApr20\\*.csv'
fname = glob.glob(path)

df = pd.DataFrame()
for f in fname:
    data = pd.read_csv(f,delimiter=';', skiprows=None)
    data = data.replace(',','', regex=True)
    data['Sensor1'] = pd.to_numeric(data['Sensor1'])
    data['Sensor2'] = pd.to_numeric(data['Sensor2'])
    data['Sensor3'] = pd.to_numeric(data['Sensor3'])
    MeanValue = data.mean()
    MaxValue = data.max()[0:4,]
    MinValue = data.min()[0:4,]
    MedianValue = data.median()
    StdDeviation = data.std()
    Variance = data.var()
    #data.quantile()
    kurtosis = data.kurtosis()
    Skew = data.skew()
    MeanValue = pd.DataFrame(MeanValue).transpose()
    MaxValue = pd.DataFrame(MaxValue).transpose()
    MinValue = pd.DataFrame(MinValue).transpose()
    MedianValue = pd.DataFrame(MedianValue).transpose()
    StdDeviation = pd.DataFrame(StdDeviation).transpose()
    Variance = pd.DataFrame(Variance).transpose()
    Skew = pd.DataFrame(Skew).transpose()
    kurtosis = pd.DataFrame(kurtosis).transpose()
    MeanValue= MeanValue.rename(columns= lambda col: col+'_Mean')
    MaxValue= MaxValue.rename(columns= lambda col: col+'_Max')
    MinValue= MinValue.rename(columns= lambda col: col+'_Min')
    MedianValue= MedianValue.rename(columns= lambda col: col+'_Median')
    StdDeviation= StdDeviation.rename(columns= lambda col: col+'_Std')
    Variance= Variance.rename(columns= lambda col: col+'_Var')
    Skew = Skew.rename(columns= lambda col: col+'_Skew')
    kurtosis = kurtosis.rename(columns= lambda col: col+'_Kurt')
    FinalData =  pd.concat([Variance,MeanValue,kurtosis,Skew,MaxValue,MinValue,MedianValue,StdDeviation], axis=1)
    x = f.split("\\")[-1][:-3]
    Activity_Value = re.findall(r"(\w+?)(\d+)",x)[0][0]
    FinalData['Activity'] = Activity_Value
    df = df.append(FinalData)
    
df.to_csv(r'C:\\Users\\arkan\\Desktop\\Activity Tracker\\ActTrackerProcessedFile.csv',index=None)
