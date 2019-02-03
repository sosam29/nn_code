dataset <- read.csv('Position_Salaries.csv')
# create varible to get the columns of interest
dataset<- dataset[2:3]
X<- dataset[1]
y <- dataset[2]

# create regressor

library(e1071)

regressor <- svm(formula=Salary~.,data= dataset , type='eps-regression')

#dataset$Level2 <- dataset$Level^2
#dataset$Level3 <- dataset$Level^3
#poly_reg <- lm(formula = Salary~.,
#               data = dataset)
ggplot()+
  geom_point(aes(x = dataset$Level, y=dataset$Salary), color='red') +
  geom_line(aes(x= dataset$Level, y = predict(regressor, newdata = dataset)), color='blue')+
  ggtitle("Truth about salary") +
  xlab("Level")+ 
  ylab('Salary')


y_pred <- predict(regressor, data.frame(Level=6.5))