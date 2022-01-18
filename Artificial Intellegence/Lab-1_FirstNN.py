import numpy as np
from tensorflow.keras.layers import Dense,Input
from tensorflow.keras.models import Model
 
def build_model():
    inputs = Input(1,)
    outputs = Dense(1)(inputs)
    model = Model(inputs,outputs)
    model.compile(loss = 'mse')
    model.summary()
    return model
 
def prepare_data():
    testX = np.arange(100)
    testY = hidden_function(testX)
    trainX = np.arange(100,65000)
    trainY = hidden_function(trainX)
    return testX,testY, trainX, trainY

def hidden_function(x):
    a=5; b=3;
    y =a*x +b;
    return y

def main():
    model = build_model()
    testX,testY,trainX,trainY = prepare_data()
    model.fit(trainX,trainY, epochs = 200)
    weight = model.layers[1].get_weights()[0][0][0]
    bias = model.layers[1].get_weights()[1][0]
    print('a:{}, b: {}'.format(weight,bias))
    
if __name__ == "__main__":
	main()
