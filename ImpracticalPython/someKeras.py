from keras.datasets import mnist
from keras.preprocessing.image import load_img, array_to_img
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense

import numpy as np
import matplotlib.pyplot as plt

# Load the Data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)        # (60000, 28, 28)
print(X_test.shape)
print(y_train.shape)        # (60000,)
print(y_test.shape)         # (10000,)

# Understanding the Image Data Format
X_train[0].shape
plt.imshow(X_train, cmap='gray')

# Preprocessing the Image Data
image_height, image_width = 28, 28
X_train = X_train.reshape(60000, image_height*image_width)
X_test = X_test.reshape(10000, image_height*image_width)
print(X_train.shape)        # (60000, 784)
print(X_test.shape)

X_train = X_train.astype('float32')     # Ensure consistent datatype
X_test = X_test.astype('float32')

X_train /= 255.0                        # Normalize the data
X_test /= 255.0
print(X_train[0])

y_train = to_categorical(y_train, 10)   # Sets the output to 10 bin
y_test = to_categorical(y_test, 10)
print(y_train.shape)                    # (60000, 10)
print(y_test.shape)                     # (10000, 10)

# Build the Model
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))    # Outer Layer
model.add(Dense(512, activation='relu'))        # Hidden Layer. No need to specify the input_shape, Keras will take care of this
model.add(Dense(10, activation='softmax'))

# Compile the Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train the Model
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

# Plot accuracy of the training model
plt.plot(history.history['acc'])

# Plot accuracy of training and validation, with loss
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.plot(history.history['loss'])

# Evaluate the Model
score = model.evaluate(X_test, y_test)
score

