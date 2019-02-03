#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 07:25:40 2018
Logistic regression 
@author: samuelsonawane
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data to create the dataset.
dataset =pd.read_csv("~/Downloads/UDEMY_ML/Logistic_Regression/Social_Network_Ads.csv")

X = dataset.iloc[:,2:4].values
y = dataset.iloc[:,4].values # have to do it like that way [[*]] as there was error related to Dimention in predict function.

#split the operation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


## Feature scaling is required here to standardize the data
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train= sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

#create the regressor
from sklearn.linear_model  import LogisticRegression

classifier = LogisticRegression(random_state=0)

# fit regression Mode
classifier.fit(X_train, y_train)

# predict 
y_pred = classifier.predict(X_test)

#compare with test result
from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#Visualize  regression model

from matplotlib.colors import ListedColormap
X_set, y_set =X_train, y_train
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min()-1, stop=X_set[:, 0].max()+1, step=0.01),
                    np.arange(start=X_set[:, 1].min()-1, stop=X_set[:, 1].max()+1, step=0.01))

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('red','green')))

#plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j, 0], X_set[y_set==j, 1],
                c= ListedColormap(('black','yellow'))(i), Label=j)
    
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()
    

from matplotlib.colors import ListedColormap
X_set, y_set =X_test, y_test
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min()-1, stop=X_set[:, 0].max()+1, step=0.01),
                    np.arange(start=X_set[:, 1].min()-1, stop=X_set[:, 1].max()+1, step=0.01))

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('red','green')))

#plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j, 0], X_set[y_set==j, 1],
                c= ListedColormap(('black','yellow'))(i), Label=j)
    
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()
    






