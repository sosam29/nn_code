#template for R 
# read file and create csv
dataset <- read.csv('Social_Network_ads.csv')
# create varible to get the columns of interest
dataset<- dataset[3:5]
X<- dataset[1:2]
y <- dataset[3]

#split into train/ test
library(caTools)
set.seed(123)

split <- sample.split(dataset$Purchased, SplitRatio = 0.75)
trainingset <- subset(dataset, split== T)
testset <- subset(dataset, split ==F)

#Feature Scaling except for last column
trainingset[,1:2] <- scale(trainingset[,1:2])
testset[,1:2] <- scale(testset[,1:2])


# Logistic regression
classifier = glm(formula = Purchased~., data = trainingset, family = binomial)
pred_response <- predict(classifier, type = 'response', newdata = testset[-3])
y_pred <- ifelse(pred_response>0.5, 1, 0)

#compare and plot the test w.r.t prediction
cm= table(testset[,3], y_pred)


# plot the result 
library(ElemStatLearn)

set = trainingset
# this sets up area of square 
X1 = seq(min(set[,1])-1, max(set[,1])+1, by=0.01)
X2 = seq(min(set[,2])-1, max(set[,2])+1, by=0.01)

grid_set=expand.grid(X1,X2)

colnames(grid_set) = c('Age', 'EstimatedSalary')

prob_set = predict(classifier,type='response', newdata = set)
y_grid = ifelse(prob_set >0.5, 1, 0)

plot(set[, -3],
     main = "Logistic Regression(training set)",
     xlab = "Age",
     ylab = "Esimated Salary",
     xlim = range(X1),
     ylim = range(X2))

contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add=T)
points(grid_set, pch='.', col=ifelse(y_grid==1, "springgreen3", "tomato"))
points(set, pch=21, bg=ifelse(set[,3]==1, "green4", "red3"))





