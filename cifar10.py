from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.datasets import cifar10
import matplotlib.pyplot as plt 
import numpy as np 

print("[INFO] Getting data from CIFAR-10 model ---")
((trainX, trainY), (testX, testY))= cifar10.load_data()

trainX = trainX.astype("float")/255.0
testX = testX.astype("float")/255.0
trainX = trainX.reshape((trainX.shape[0], 3072))
testX = testX.reshape((testX.shape[0], 3072))

lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)

labelnames = ["Airplane", "automobile","bird","cat","deer", "dog","hourse","ship","truck"]
print("[INFO] Building model ---")
model = Sequential()
model.add(Dense(1024, input_shape=(3072,), activation="relu"))
model.add(Dense(512, activation="relu"))
model.add(Dense(10, activation='softmax'))

print("[INFO] Compiling model ---")
sgd = SGD( 0.01)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics="accuracy")
H = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=100, batch_size=32)

print("[INFO] Predicting model ---")
pred = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1), pred.argmax(axis=1), target_names=labelnames))


plt.style.use('ggplot')
plt.figure()
plt.plot(np.arange(0,100), H.history['loss'], label='train_loss')
plt.plot(np.arange(0,100), H.history['val_loss'], label='val_loss')
plt.plot(np.arange(0,100), H.history['acc'], label='train_acc')
plt.plot(np.arange(0,100), H.history['val_acc'], label='val_acc')
plt.title("Training Loss and Accracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()



 

