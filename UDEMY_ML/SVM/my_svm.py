#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 17:17:50 2018

@author: samuelsonawane
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#get the data
dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[ :,2:3].values
y= dataset.iloc[:,4].values

#Split the data
from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test= train_test_split(X, y, test_size=0.25, random_state=0)

#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Model traning

from sklearn.neighbors import KNeighborsClassifier
neighb = KNeighborsClassifier(n_neighbors=5,  metric= "minkowski", p= 2  )
neighb.fit(X_train, y_train)

#Model Prediction
y_pred =neighb.predict(X_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

