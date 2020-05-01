import numpy as np
from keras.applications import vgg16
from keras.preprocessing import image

model = vgg16.VGG16(weights="imagenet")

img = image.load_img('images/spoon.jpeg', target_size=(224,224))
img

# Convert image to Numpy array
arr = image.img_to_array(img)
arr.shape       # (224, 224, 3)

# Expand dimension
arr = np.expand_dims(arr, axis=0)
arr.shape       # (1, 224, 224, 3)

# Preprocessing
arr = vgg16.preprocess_input(arr)
arr

# Predict
preds = model.predict(arr)
preds

# Prediction for Top 5
vgg16.decode_predictions(preds, top=5)


#### Test using another image
img2 = image.load_img('images/fly.jpeg', target_size=(224,224))
img2

arr2 = image.img_to_array(img2)
arr2 = np.expand_dims(arr2, axis=0)
arr2 = vgg16.preprocess_input(arr2)
preds2 = model.predict(arr2)
vgg16.decode_predictions(preds2, top=5)