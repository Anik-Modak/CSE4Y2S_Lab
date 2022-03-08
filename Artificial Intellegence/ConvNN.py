from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import Model

def build_model(m, n, h, c):
    
    inputs = Input((m, n, 1))
    x = Conv2D(filters=2*h, kernel_size=(3,3), strides=(1,1), padding='same')(inputs)
    
    for i in range(h-1):
        x = Conv2D(filters=2*(h-i-1), kernel_size=(2,2), strides=(1,1), padding='same')(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)
    
    x = Flatten()(x)
    outputs = Dense(c, activation="sigmoid")(x)
    model = Model(inputs, outputs)
    model.summary()
    
    model.compile(loss='mse', optimizer="rmsprop")
    return model

def main():
    build_model(28, 28, 4, 3)
    
if __name__ == "__main__":
    main()    
    
    