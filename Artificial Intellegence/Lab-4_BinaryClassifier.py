# To prepare a transfer learning based binary classifier using the pre-trained VGG16.

from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import numpy as np
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.callbacks import EarlyStopping, History
import random
import os
import cv2
import matplotlib.pyplot as plt

TRAIN_SPLIT = 0.80

DIR = ''

def main():
	#original_model_prediction()
	
	# Prepare data sets
	imgH = 128; imgW = 128 
	trainX, trainY, testX, testY = preprocess_data(imgH, imgW)
	
	# Train and save model.
	modelPath = DIR + 'VGG_BinaryClassifier.hdf5'
	training(trainX, trainY, modelPath, imgH, imgW)
	
	# Load and test the model
	testing(testX, testY, modelPath)

def testing(testX, testY, modelPath):
	# Preprocess image data to be fit with VGG16
	testXX = preprocess_input(testX) 
	
	# Load the trained model'
	model = load_model(modelPath)
	
	# Predict Class
	predictions = model.predict(testX)
	predictedClass = ['SmartPhone' if a < 0.5 else 'ButtonPhone' for a in predictions] 
	actualClass = ['SmartPhone' if a < 0.5 else 'ButtonPhone' for a in testY]	
	print('Actual Class: {}'.format(actualClass))
	print('Predicted Class: {}'.format(predictedClass))
	display_images_with_predictions(testX, predictedClass)
	
	# Evaluate model performance
	model.compile(metrics = 'accuracy')
	loss, accuracy = model.evaluate(testXX, testY)
	print('Accuracy: {}'.format(accuracy))

def training(trainX, trainY, modelPath, imgH, imgW):
	# Preprocess image data to be fit with VGG16
	print(trainX.max(), trainX.min())
	trainX = preprocess_input(trainX)
	print(trainX.max(), trainX.min())
		
	# Build model architecture. 
	model = build_model(imgH, imgW)
	
	# Train model
	model.compile(loss = 'mse', optimizer = 'rmsprop')
	callbackList = [EarlyStopping(monitor = 'val_loss', patience = 10), History()]
	history = model.fit(trainX, trainY, epochs = 100, batch_size = 32, validation_split = 0.2, callbacks = callbackList)
		
	# Save trained model and figure of training and validation loss.
	model.save(modelPath)
	figPath = DIR + 'Training_Vs_Val_Loss.png'
	plot_loss(history, figPath)
	
def plot_loss(history, figPath):
	loss = history.history['loss']
	valLoss = history.history['val_loss']
	epochs = range(1, len(loss) + 1)

	plt.figure(figsize = (20, 20))
	plt.rcParams['font.size'] = '14'
	plt.plot(epochs, loss, 'bo-', label = 'Training loss')
	plt.plot(epochs, valLoss, 'k*-', label = 'Validation loss')
	plt.title('Training and validation loss')
	plt.legend()
	
	plt.savefig(figPath)
	plt.close()

def display_images_with_predictions(imgSet, labelSet):
	plt.figure(figsize = (20, 20))
	for i in range(9):
		plt.subplot(3, 3, i + 1)
		plt.title(labelSet[i])
		plt.imshow(imgSet[i])
		plt.axis('off')
	plt.show()
	
def preprocess_data(imgW, imgH):
	# Load image data
	imgDir = DIR + 'SmartPhone/'
	imgSet1 = prepare_image_array(imgDir, imgW, imgH)
	print(imgSet1.shape)
	m = imgSet1.shape[0]
	
	imgDir = DIR + 'ButtonPhone/'
	imgSet2 = prepare_image_array(imgDir, imgW, imgH)
	print(imgSet2.shape)
	n = imgSet2.shape[0]
	
	# Put all image data into one array.
	imgSet = np.concatenate((imgSet1, imgSet2), axis = 0)
	print(imgSet.shape)
	
	# Prepare labels.
	labelSet1 = np.zeros(m, dtype = np.uint8)
	labelSet2 = np.ones(n, dtype = np.uint8)
	labelSet = np.concatenate((labelSet1, labelSet2), axis = 0)
	print(labelSet)
	
	# Shuffle image data and labels
	p = imgSet.shape[0] # p = n + m
	indices = np.arange(p)
	print(indices)
	random.shuffle(indices)
	print(indices)	
	imgSet = imgSet[indices]
	labelSet = labelSet[indices]
	
	# Split data into training and test sets
	r = int(p * TRAIN_SPLIT)
	trainX = imgSet[:r]
	trainY = labelSet[:r]
	testX = imgSet[r:]
	testY = labelSet[r:]
	
	return trainX, trainY, testX, testY

def prepare_image_array(imgDir, imgW, imgH):
	imgList = os.listdir(imgDir)
	#print(imgList)
	n = len(imgList)
	
	imgSet = []
	for i in range(n):
		imgPath = imgDir + imgList[i]
		if (os.path.exists(imgPath)):
			print(imgPath)
			
			# Load image.
			img = cv2.imread(imgPath)
			print(img.shape)
			
			# Resize image.
			resizedImg = cv2.resize(img, (imgW, imgH))
			print(resizedImg.shape)
			
			# Convert BGR image into RGB image.
			rgbImg = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2RGB)
			
			# Put image into a list
			imgSet.append(rgbImg)
		else:
			print("It is not a valid image path.")
		
	print(len(imgSet))
	imgSet = np.array(imgSet, dtype = np.uint8)
	print(imgSet.shape)
	
	return imgSet

def build_model(imgH, imgW):
	baseModel = VGG16(input_shape = (imgH, imgW, 3), include_top = False) 
	baseModel.summary()
	
	for layer in baseModel.layers:
		layer.trainable = False
	baseModel.summary()
	
	inputs = baseModel.input
	x = baseModel.output
	x = Flatten()(x)
	x = Dense(32, activation = 'sigmoid')(x)
	x = Dense(8, activation = 'sigmoid')(x)
	outputs = Dense(1, activation = 'sigmoid')(x)
	
	model = Model(inputs, outputs)
	model.summary()
	
	return model

if __name__ == '__main__':
	main()

