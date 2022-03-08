from calendar import EPOCH
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import Model 
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy as np

def prepare_data():
    (trainX, trainY), (testX, testY) = mnist.load_data()
    print(trainX.shape, trainY.shape, testX.shape, testY.shape)
    
    index = np.argwhere((trainY == 1) | (trainY == 2))
    trainX = trainX[index]
    trainY = trainY[index]
    trainX = trainX[:,0,:,:]
    trainY = trainY[:,0]
    
    index = np.argwhere((testY == 1) | (testY == 2))
    testX = testX[index]
    testY = testY[index]
    testX = testX[:,0,:,:]
    testY = testY[:,0]
    
    classN = 2
    trainY = to_categorical(trainY==2)
    testY = to_categorical(testY==2)
    
    trainX = trainX.astype(np.float32)
    testX = testX.astype(np.float32)
    
    trainX /= 255
    testX /= 255
    return trainX, trainY, testX, testY

def build_model():
    inputs=Input((28, 28, 1))
    x = Conv2D(32, (3,3), activation="sigmoid")(inputs)
    x = MaxPooling2D(2,2)(x);
    x = Conv2D(16, (3,3), activation="sigmoid")(x)
    x = MaxPooling2D(2,2)(x);
    x = Conv2D(4, (2,2), activation="sigmoid")(x)
    x = MaxPooling2D(2,2)(x);
    x = Flatten()(x)
    x = Dense(8, activation="sigmoid")(x)
    outputs = Dense(2, activation="softmax")(x)
    
    model = Model(inputs, outputs)
    model.summary()
    return model
     
def main():
    trainX, trainY, testX, testY = prepare_data()
    model = build_model()
    model.compile(loss='mse', optimizer='rmsprop')
    model.fit(trainX, trainY, epochs = 5, batch_size = 16, validation_split = 0.2)
    model.compile(metrics = 'accuracy')
    model.evaluate(testX, testY)
    
if __name__=="__main__":
    main()