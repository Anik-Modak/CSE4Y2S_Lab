import numpy as np
from tensorflow.keras.layers import Dense,Input, Flatten
from tensorflow.keras.models import Model
 
def build_model():
    inputs = Input((28, 28))
    x = Flatten()(inputs)
    x = Dense(32, activation = 'sigmoid')(x)
    x = Dense(16, activation = 'sigmoid')(x)
    outputs = Dense(3)(x)
    
    model = Model(inputs, outputs)
    model.summary()
    
    model.compile(loss = 'mse')
    
    return model

def main():
    model = build_model()
  
    
if __name__ == "__main__":
	main()
