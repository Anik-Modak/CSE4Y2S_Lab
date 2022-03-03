from tensorflow.keras.layers import Dense, Input, Flatten, Conv2D, MaxPool2D
from tensorflow.keras.models import Model
 
def build_model():
	
	inputs = Input((28, 28, 1))
	x = Conv2D(10, (3,3), strides=(2,2), padding = 'valid')(inputs)
	x = Conv2D(4, (2,2), strides=(2,2), padding = 'valid')(x)
	x = Flatten()(x)
	x = Dense(100, activation = 'relu')(x)
	outputs = Dense(10, activation='softmax')(x)
    
	model = Model(inputs, outputs)
	model.summary()
    
	model.compile(loss = 'mse', optimizer='rmsprop')
    
	return model

def main():
	model = build_model()
    
if __name__ == "__main__":
	main()
