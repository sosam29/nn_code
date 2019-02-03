# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#from sklearn.model_selection import train_test_split

# import data to create the dataset.
dataset =pd.read_csv("~/Downloads/UDEMY_ML/SVR/Position_Salaries.csv")

X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2:3].values # have to do it like that way [[*]] as there was error related to Dimention in predict function.

#yß= y.reshape(1,-1)
#since dataset is small we are skipping split the operation
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#from sklearn.tree import DecisionTree
#sc_X = StandardScaler()
#sc_y = StandardScaler()
#X= sc_X.fit_transform(X)
#y= sc_y.fit_transform(y)

#create the regressor
from sklearn.tree  import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state=0)

s#ummary(regressor)
# fit regression Mode
regressor.fit(X, y)

y_pred = regressor.predict(6.5)

#Visualize  regression model 

plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title("plot SVR Regression")
plt.xlabel("Position Level")
plt.ylabel('Salary')

#Visualize  regression model with higher resolutions

X_grid = np.arange(min(X), max(X), 0.001)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title("plot SVR High Definition Regression")
plt.xlabel("Position Level")
plt.ylabel('Salary')



