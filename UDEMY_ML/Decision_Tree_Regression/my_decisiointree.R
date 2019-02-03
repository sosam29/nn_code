dataset <- read.csv('Position_Salaries.csv')
# create varible to get the columns of interest
dataset<- dataset[2:3]
X<- dataset[1]
y <- dataset[2]

# create regressor

library(rpart)

regressor <- rpart(formula=Salary~.,data= dataset, control = rpart.control(minsplit = 1L) )

#dataset$Level2 <- dataset$Level^2
#dataset$Level3 <- dataset$Level^3
#poly_reg <- lm(formula = Salary~.,
#               data = dataset)
ggplot()+
  geom_point(aes(x = dataset$Level, y=dataset$Salary), color='red') +
  geom_line(aes(x= dataset$Level, y = predict(regressor, newdata = dataset)), color='blue')+
  ggtitle("Truth about salary DecisionTree") +
  xlab("Level")+ 
  ylab('Salary')

# high resolution Display 
X_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot()+
  geom_point(aes(x = dataset$Level, y=dataset$Salary), color='red') +
  geom_line(aes(x= X_grid, y = predict(regressor, newdata = data.frame(Level=X_grid))), color='blue')+
  ggtitle("Truth about High resolution DecisionTree") +
  xlab("Level")+ 
  ylab('Salary')


y_pred <- predict(regressor, data.frame(Level=6.5))
