from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from shallownn import ShallowNN
from keras.optimizers import SGD
from keras.datasets import cifar10
import matplotlib.pyplot as plt 
import numpy as np 

((trainX, trainY),(testX, testY)) = cifar10.load_data()
trainX = trainX.astype('float')/255.0
testX = testX.astype('float')/255.0

lb= LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY= lb.transform(testY)

labelNames = ["Airplane","Automobile","bird","cat","deer","dog", "frog","horse","ship","duck"]
opt =SGD(lr=0.005)
model = ShallowNN.build(width=32, height=32, depth=3, classes=10)
model.compile(opt, loss="categorical_crossentropy", metrics=["accuracy"])

H = model.fit(trainX, trainY, validation_data=(testX, testY), batch_size=50, epochs=40, verbose=-1)

print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1),
	target_names=labelNames))

# plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 100), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 100), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 100), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, 100), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()



