from tensorflow.keras.layers import Dense, Input, Flatten, Conv2D, MaxPool2D
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing.image import img_to_array, array_to_img
import numpy as np

IMG_W = 32
IMG_H = 32

def build_model():
	baseModel = VGG16(input_shape = (IMG_W, IMG_H, 3), include_top = False)
	baseModel.summary()
	
	for layer in baseModel.layers:
		layer.trainable = False
	baseModel.summary()
	
	inputs = baseModel.input
	x = baseModel.output
	x = Flatten()(x)
	x = Dense(8, activation = 'sigmoid')(x)
	outputs = Dense(2)(x)
	
	model = Model(inputs, outputs)
	model.summary()

	return model

def prepare_data():

	# Load image data
	(trainX, trainY), (testX, testY) = mnist.load_data()
	print(trainX.shape, trainY.shape, testX.shape, testY.shape)

	index = np.argwhere(trainY < 2)
	trainX = trainX[index]
	trainY = trainY[index]

	index = np.argwhere(testY < 2)
	testX = testX[index]
	testY = testY[index]

	trainX = np.dstack([trainX] * 3)
	testX = np.dstack([testX] * 3)

	trainX = trainX.reshape(-1, 28,28,3)
	testX = testX.reshape (-1,28,28,3)


	trainX = np.asarray([img_to_array(array_to_img(im, scale=False).resize((IMG_W,IMG_H))) for im in trainX])
	testX = np.asarray([img_to_array(array_to_img(im, scale=False).resize((IMG_W,IMG_H))) for im in testX])
	
	classN = 2
	trainY = to_categorical(trainY, classN)
	testY = to_categorical(testY, classN)
	
	# To convert pixel values from 0-255 into 0-1.    
	trainX = trainX.astype(np.float32)
	testX = testX.astype(np.float32)
	trainX /= 255
	testX /= 255    

	# Preprocess image data to be fit with VGG16
	testX = preprocess_input(testX)
	trainX = preprocess_input(trainX)
	
	return trainX, trainY, testX, testY
		
def main():
	trainX, trainY, testX, testY = prepare_data()
	model = build_model()

	model.compile(loss = 'mse', optimizer='rmsprop')
	model.fit(trainX, trainY, epochs = 10, batch_size = 16, validation_split = 0.2)
	model.compile(metrics = 'accuracy')
	model.evaluate(testX, testY)  

if __name__ == "__main__":
	main()
