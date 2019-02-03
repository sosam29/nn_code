from keras.layers.core import Dense
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.optimizers import SGD
from sklearn.metrics import classification_report
from sklearn import datasets
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt 
import numpy as np 
from mnist import MNIST
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

print("[INFO]  loading full nmnsit dataset...")

mndata = MNIST('/Users/samuelsonawane/Downloads/ML_TensorFlow/mnist_data_full/samples')
trainX, trainY = mndata.load_training()
testX, testY = mndata.load_testing()

X = trainX +  testX
y=  trainY+ testY
#dataset = datasets.fetch_mldata("MNIST Original")

# X, y = input_data.read_data_sets('MNIST_data', one_hot=True)
# X, y = datasets.fetch_openml('mnist_784', version=1, return_X_y=True)

# print('hi there')
# data = dataset.data.astype('float')/255.0
(trainX, testX, trainY, testY)= train_test_split(X, y, test_size=0.25, random_state=42)

lb = LabelBinarizer()
enc = OneHotEncoder(handle_unknown='ignore')

trainY= enc.fit_transform(trainY)
testY = enc.fit(testY)
# print(type(trainY)) array.array
# trainY = lb.fit_transform(trainY)
# testY = lb.transform(testY)


model = Sequential()
model.add(Dense(256, inout_shape=(786,), activation='sigmoid'))
model.add(Dense(128, activation='sigmoid'))
model.add(Dense(10, activation='softmax'))

sgd = SGD(0.01)
model.compile(loss='categorical_crossentroy', optimizer=sgd, metrics=['accuracy'])
H = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=100, batch_size=128)

print("[INFO] evaluating network.....")

predictions = model.predict(testX,batch_size=128 )

print(classification_report(testY.argmax(axis=1), predictions.argmax(axis=1), target_names=[str(x) for x in lb.classes_]))
plt.style.use('ggplot')
plt.figure()
plt.plot(np.arange(0, 100), H.histogram['loss'], label= 'train_loss')
plt.plot(np.arange(0, 100), H.histogram['val_loss'], label= 'val_loss')
plt.plot(np.arange(0, 100), H.histogram['acc'], label= 'train_acc')
plt.plot(np.arange(0, 100), H.histogram['val_acc'], label= 'val_acc')
plt.title('Training Loss and Accuracy')
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
print('[INFO]  THIS IS FOR HOLDING LINE')



