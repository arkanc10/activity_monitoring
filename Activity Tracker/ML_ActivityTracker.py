# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:36:56 2021

@author: arkan
"""
### Applying ML model for activity tracker
## KNN 


import pandas as pd 
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_csv('C:\\Users\\arkan\\OneDrive\\Desktop\\Activity Tracker\\ActTrackerProcessedFile.csv')

x = df.drop('Activity',axis = 1) ##df.iloc[:,:-1]

s = MinMaxScaler()

x_scale = s.fit_transform(x)

y = df['Activity'] ## df.iloc[:,-1]


X_train, X_test, y_train, y_test = train_test_split(x_scale,y, test_size=0.25, random_state=42)


a = []
k = []
for i in range(1,15):
    neigh = KNeighborsClassifier(n_neighbors=i)
    fit = neigh.fit(X_train, y_train)
    Test_values_pred = fit.predict(X_test)
    k.append(i)
    a.append(np.mean(Test_values_pred != y_test))
    
plt.plot(k,a)
plt.show()    

# Taking the neighbours as 1 from the above graph
neigh = KNeighborsClassifier(n_neighbors=1)
fit = neigh.fit(X_train, y_train)
Test_values_pred = fit.predict(X_test)

print(classification_report(y_test, Test_values_pred))
