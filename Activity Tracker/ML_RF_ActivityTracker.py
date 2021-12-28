# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:52:19 2021

@author: arkan
"""


import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\arkan\\OneDrive\\Desktop\\Activity Tracker\\ActTrackerProcessedFile.csv')

x = df.drop('Activity',axis = 1) ##df.iloc[:,:-1]

y = df['Activity'] ## df.iloc[:,-1]

# scaler = StandardScaler()
 #data scaled and centered

X_train,X_test, y_train, y_test = train_test_split(x,y,test_size=0.20, random_state=42,stratify=y)

# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

accuracies = []
n = range(10,50,2)
for i in n:
    clf = RandomForestClassifier(n_estimators= i , random_state=0 )
    fit = clf.fit(X_train, y_train)
    Test_Pred = fit.predict(X_test)
    a_test = (accuracy_score(y_test, Test_Pred))
    accuracies.append(a_test)
    
plt.plot(n,accuracies)
plt.ylabel('Accuracy')
plt.xlabel('No. of Trees')
plt.show()

# Lets say we pick n_estimators = 20 
clf = RandomForestClassifier(n_estimators= 35 , random_state=0 )
fit = clf.fit(X_train, y_train)
Test_Pred = fit.predict(X_test)

print(classification_report(y_test,Test_Pred))
print(confusion_matrix(y_test,Test_Pred))

#Train_Pred = fit.predict(X_train)

#a_train = metrics.accuracy_score(y_train, Train_Pred)




