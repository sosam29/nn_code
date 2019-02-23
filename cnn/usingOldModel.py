from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from shallownn import ShallowNN
from keras.optimizers import SGD
from keras.datasets import cifar10
import matplotlib.pyplot as plt 
import numpy as np 
from imutils import paths
from keras.models import load_model

# print()

imagePath = np.array(list(paths.list_images()))
((trainX, trainY),(testX, testY)) = cifar10.load_data()
trainX = trainX.astype('float')/255.0
testX = testX.astype('float')/255.0

lb= LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY= lb.transform(testY)

labelNames = ["Airplane","Automobile","bird","cat","deer","dog", "frog","horse","ship","duck"]

model =load_model('../cifar10.model.hdf5')

print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1),
	target_names=labelNames))

# plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 40), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 40), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 40), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, 40), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()
