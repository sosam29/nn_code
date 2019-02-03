import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split

# import data to create the dataset.
dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1].values


#since dataset is small we are skipping split the operation
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#create the regressor

y_pred = regressor.predict(6.5)
# fit regression Mode



#Visualize  regression model 

plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X)), color='blue')
plt.title("plot Regression)")
plt.xlabel("Position Level")
plt.ylabel('Salary')

#Visualize  regression model with higher resolutions
X_grid = np.arange(min(X),max(X), 0.1)
#print(X_grid)
X_grid = X_grid.reshape((len(X_grid),1))
#print(X_grid)
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid)), color='blue')
plt.title("plot Regression with higher resolutions")
plt.xlabel("Position Level")
plt.ylabel('Salary')


