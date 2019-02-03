#read dataset from source
dataset = read.csv('Wine.csv')

# split dataset
library(caTools)
set.seed(123)
split = sample.split(dataset$Customer_Segment, SplitRatio = 0.2)
training_set = subset(dataset, split==T)
testing_set = subset(dataset, split ==F)

#feature scaling
training_set= scale(training_set[-14])
testing_set = scale(testing_set[-14])

#PCA
install.packages('caret')
library('caret')
library('e1071')