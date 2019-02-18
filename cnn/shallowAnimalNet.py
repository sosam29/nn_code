from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import image2arrpreprocessor
from shallownn import ShallowNN
from keras.optimizers import SGD
from imutils import paths
import matplotlib.pyplot as plt 
import numpy as np
from SimpleDatasetLoader import SimpleDatasetLoader
from SimplePreprocessor import SimplePreprocessor
from image2arrpreprocessor import ImageToArrayPreProcessor

imagePaths = list(paths.list_images(r'/Users/samuelsonawane/Downloads/SB_Code/datasets/animals/')) # path to load images
print(len(imagePaths))
sp = SimplePreprocessor(32, 32)
iap = ImageToArrayPreProcessor()
sdl = SimpleDatasetLoader(preprocessors=[sp, iap])
(data, labels) = sdl.load(imagePaths, verbose = 600)
# print(data)
data = data.astype("float")/255.0


(trainX, testX, trainY, testY ) = train_test_split(data, labels, test_size=0.25, random_state=42)

trainY = LabelBinarizer().fit_transform(trainY)
testY = LabelBinarizer().fit_transform(testY)


opt = SGD(lr= 0.005)
model = ShallowNN.build(width=32, height=32, depth=3, classes=3)
model.compile(loss ="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

H = model.fit(trainX, trainY, validation_data=(testX, testY), batch_size=32, epochs= 100, verbose= 1)

pred = model.predict(testX, batch_size= 32)

print(classification_report(testY.argmax(axis=1), pred.argmax(axis=1), target_names=['cat', 'dog','panda']))
