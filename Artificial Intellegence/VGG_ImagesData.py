from tensorflow.keras.layers import Input, Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
import numpy as np
import os
import cv2
import random

TRAIN_SPLIT = 0.8
IMG_H = IMG_W = 32

def prepare_data():
    imgDir = 'SmartPhone/'
    imgSet1 = prepare_image_array(imgDir)
    m = imgSet1.shape[0]
    
    imgDir = 'ButtonPhone/'
    imgSet2 = prepare_image_array(imgDir)
    n = imgSet2.shape[0]
    
    imgSet = np.concatenate((imgSet1, imgSet2), axis = 0)
    print(imgSet.shape)
 
    #prepare labels
    levelSet1 = np.zeros(m, dtype = np.uint8)
    levelSet2 = np.ones(n, dtype = np.uint8)
    labelSet = np.concatenate((levelSet1, levelSet2), axis = 0)
    
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
 
    # Preprocess image data to be fit with VGG16
    testX = preprocess_input(testX)
    trainX = preprocess_input(trainX)
    print(trainX.shape, testX.shape)
 
    return trainX, trainY, testX, testY

def prepare_image_array(imgDir):
    imgList = os.listdir(imgDir)
    n = len(imgList)
    
    imgSet = []
    for i in range(n):
        imgPath = imgDir + imgList[i]
        
        if(os.path.exists(imgPath)):
            img = cv2.imread(imgPath)
            resImg = cv2.resize(img, (IMG_H, IMG_W))
            rgbImg = cv2.cvtColor(resImg, cv2.COLOR_BGR2RGB)
            imgSet.append(rgbImg)
        else:
            print("This is not valid path")
    
    imgSet = np.array(imgSet, dtype = np.uint8)
    return imgSet
    
def build_model():
    basemodel = VGG16(input_shape=(IMG_H, IMG_W, 3), include_top = False)
    basemodel.summary()
    
    for layer in basemodel.layers:
        layer.trainable = False
     
    inputs = basemodel.input   
    x = basemodel.output
    x = Flatten()(x)
    x = Dense(32, activation = 'sigmoid')(x)
    x = Dense(8, activation='sigmoid')(x)
    outputs = Dense(2, activation='sigmoid')(x)
    
    model = Model(inputs, outputs)
    model.summary()
    
    return model
     
def main():
    from tensorflow.keras.callbacks import EarlyStopping, History
    trainX, trainY, testX, testY = prepare_data()
    model = build_model()

    model.compile(loss = 'mse', optimizer = 'rmsprop')
    callbackList = [EarlyStopping(monitor = 'val_loss', patience = 10), History()]
    history = model.fit(trainX, trainY, epochs = 300, batch_size = 16, callbacks = callbackList, validation_split = 0.2)
    
    # Check what the model predicts.
    predictY = model.predict(testX)
    for i in range(10):
	    y = np.argmax(testY[i])
	    pY = np.argmax(predictY[i])
	    print('Original Y: {}, Predicted Y: {}'.format(y, pY))
    

    # Evaluate model performance
    model.compile(metrics = 'accuracy')
    loss, accuracy = model.evaluate(testX, testY)
    print('Accuracy: {}'.format(accuracy))  
    
if __name__=="__main__":
    main()