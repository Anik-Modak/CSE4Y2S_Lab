from tensorflow.keras.layers import Input, Dense, Flatten
from tensorflow.keras.models import Model 
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
import numpy as np

IMG_H = IMG_W = 32

def prepare_data():
    (trainX, trainY), (testX, testY) = mnist.load_data();
    
    index = np.argwhere(trainY < 3)
    index = np.squeeze(index)
    trainX = trainX[index]
    trainY = trainY[index]
    
    index = np.argwhere(testY < 3)
    index = np.squeeze(index)
    testX = testX[index]
    testY = testY[index]
    
    classN = 3
    trainY = to_categorical(trainY, classN)
    testY = to_categorical(testY, classN)
    
    print(trainX.shape, testX.shape)
    trainX = np.pad(trainX, ((0,0),(2,2),(2,2)), 'constant')
    testX = np.pad(testX, ((0,0),(2,2),(2,2)), 'constant')
    
    trainX = np.stack((trainX,)*3, axis = -1)
    testX = np.stack((testX,)*3, axis=-1)
    print(trainX.shape, testX.shape)
    
    trainX = trainX.astype(np.float32)
    testX = testX.astype(np.float32)
    
    trainX /= 255
    testX /= 255
    
    # Preprocess image data to be fit with VGG16
    trainX = preprocess_input(trainX)
    testX = preprocess_input(testX)
    
    return trainX, trainY, testX, testY

def build_model():
    
    basemodel = VGG16(input_shape=(32, 32, 3), include_top = False)
    basemodel.summary()
    
    for layer in basemodel.layers:
        layer.trainable = False
     
    inputs = basemodel.input   
    x = basemodel.output
    x = Flatten()(x)
    x = Dense(8, activation='sigmoid')(x)
    outputs = Dense(3, activation='softmax')(x)
    
    model = Model(inputs, outputs)
    model.summary()
    
    return model
     
def main():
    trainX, trainY, testX, testY = prepare_data()
    model = build_model()

    model.compile(loss = 'mse', optimizer='rmsprop')
    model.fit(trainX, trainY, epochs = 10, batch_size = 32, validation_split = 0.2)
    model.compile(metrics = 'accuracy')
    model.evaluate(testX, testY)  
    
if __name__=="__main__":
    main()
        
    
    
    