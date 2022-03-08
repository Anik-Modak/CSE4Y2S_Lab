from tensorflow.keras.layers import Dense, Input, Flatten
from tensorflow.keras.models import Model

def bulid_model(m, n, h, c):
    
    inputs = Input((m, n))
    x = Flatten()(inputs)
    
    for i in range(h):
        x = Dense(2**(h-i+1), activation = 'sigmoid')(x)
    
    outputs = Dense(c, activation='sigmoid')(x)
    model = Model(inputs, outputs)
    model.summary()
    model.compile(loss='mse', optimizer='rmsprop')
    return model;

def main():
    bulid_model(28, 28, 4, 3)
    
if __name__=="__main__":
    main()


    
    
