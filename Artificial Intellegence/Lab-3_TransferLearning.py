from tensorflow.keras.applications.vgg16 import VGG16, decode_predictions, preprocess_input
import cv2
import matplotlib.pyplot as plt
import numpy as np

DIR = '/home/cse/AI_Lab_2021/'

def main():
	# Load a pre-trained model.
	model = VGG16()
	model.summary()
	
	# Load image
	imgPath = DIR + 'Baby.jpeg' #'Rose.jpeg' #'Boat.jpeg' #'Elephant.jpeg'	
	bgrImg = cv2.imread(imgPath)
	print(bgrImg.shape)
	
	# Convert image from BGR into RGB format
	rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
	
	# Reshape image so that it can fit into the model.
	display_img(rgbImg)
	rgbImg = cv2.resize(rgbImg, (224, 224))
	display_img(rgbImg)
	
	# Expand dimension since the model accepts 4D data.
	print(rgbImg.shape)
	rgbImg = np.expand_dims(rgbImg, axis = 0)
	print(rgbImg.shape)
	
	# Preprocess image
	rgbImg = preprocess_input(rgbImg)
	
	# Predict which class the loaded image belongs to
	# List of 1000 classes: http://image-net.org/challenges/LSVRC/2014/browse-synsets
	prediction = model.predict(rgbImg)
	prediction = decode_predictions(prediction, top = 1000)
	print(prediction)
	
def display_img(img):
	plt.imshow(img)
	plt.show()
	plt.close()

if __name__ == '__main__':
	main()