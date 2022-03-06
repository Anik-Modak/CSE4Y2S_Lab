from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
import numpy as np
import os
import cv2
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
import random

TRAIN_SPLIT = 0.80
DIR = ''
IMG_W = 32
IMG_H = 32

def prepare_data():
	# Load image data
	imgDir = DIR + 'SmartPhone/'
	imgSet1 = prepare_image_array(imgDir)
	m = imgSet1.shape[0]
	
	imgDir = DIR + 'ButtonPhone/'
	imgSet2 = prepare_image_array(imgDir)
	n = imgSet2.shape[0]
	
	# Put all image data into one array.
	imgSet = np.concatenate((imgSet1, imgSet2), axis = 0)
	print(imgSet.shape)
	
	# Prepare labels.
	labelSet1 = np.zeros(m, dtype = np.uint8)
	labelSet2 = np.ones(n, dtype = np.uint8)
	labelSet = np.concatenate((labelSet1, labelSet2), axis = 0)
	
	# Shuffle image data and labels
	p = n + m
	indices = np.arange(p)
	random.shuffle(indices)	
	imgSet = imgSet[indices]
	labelSet = labelSet[indices]
	
	# Split data into training and test sets
	r = int(p * TRAIN_SPLIT)
	trainX = imgSet[:r]
	trainY = labelSet[:r]
	testX = imgSet[r:]
	testY = labelSet[r:]
	
	return trainX, trainY, testX, testY

def prepare_image_array(imgDir):
	imgList = os.listdir(imgDir)
	n = len(imgList)
	
	imgSet = []
	for i in range(n):
		imgPath = imgDir + imgList[i]
		if (os.path.exists(imgPath)):
			# Load image.
			img = cv2.imread(imgPath)
			#print(img.shape)
			
			# Resize image.
			resizedImg = cv2.resize(img, (IMG_W, IMG_H))
			#print(resizedImg.shape)

			# Convert BGR image into RGB image.
			rgbImg = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2RGB)
			
			# Put image into a list
			imgSet.append(rgbImg)
		else:
			print("It is not a valid image path.")
		
	imgSet = np.array(imgSet, dtype = np.uint8)
	print(imgSet.shape)
	return imgSet

def build_model():
	baseModel = VGG16(input_shape = (IMG_H, IMG_W, 3), include_top = False) 
	baseModel.summary()
	
	for layer in baseModel.layers:
		layer.trainable = False
	#baseModel.summary()
	
	inputs = baseModel.input
	x = baseModel.output
	x = Flatten()(x)
	x = Dense(32, activation = 'sigmoid')(x)
	x = Dense(8, activation = 'sigmoid')(x)
	outputs = Dense(1, activation = 'sigmoid')(x)
	
	model = Model(inputs, outputs)
	model.summary()
	
	return model

def main():
	trainX, trainY, testX, testY = prepare_data()
	model = build_model()

	model.compile(loss = 'mse', optimizer='rmsprop')
	model.fit(trainX, trainY, epochs = 50, batch_size = 32, validation_split = 0.2)
	model.compile(metrics = 'accuracy')
	model.evaluate(testX, testY)
	
if __name__ == '__main__':
	main()
