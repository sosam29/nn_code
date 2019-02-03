#template for R 
# read file and create csv
dataset <- read.csv('Position_Salaries.csv')
# create varible to get the columns of interest
dataset<- dataset[2:3]
X<- dataset[1]
y <- dataset[2]

library(randomForest)

regressor <- randomForest(formula = Salary~.,
               data = dataset, ntree=1000)
#X_grid <- seq(min(dataset$Level), max(dataset$Level), 0.001)
# 
ggplot()+
  geom_point(aes(x = dataset$Level, y=dataset$Salary), color='red') +
  geom_line(aes(x= dataset$Level, y = predict(regressor, newdata = dataset)), color='blue')+
  ggtitle("Truth about salary (Random Forest)") +
  xlab("Level")+ 
  ylab('Salary')


X_grid <- seq(min(dataset$Level), max(dataset$Level), 0.001)

ggplot()+
  geom_point(aes(x = dataset$Level, y=dataset$Salary), color='red') +
  geom_line(aes(x= X_grid, y = predict(regressor, newdata = data.frame(Level=X_grid))), color='blue')+
  ggtitle("Truth about salary (Random Forest)") +
  xlab("Level")+ 
  ylab('Salary')


y_pred <- predict(regressor, data.frame(Level=6.5))