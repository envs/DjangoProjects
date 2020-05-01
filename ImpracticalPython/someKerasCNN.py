from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

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
num_classes = 10
epochs = 3

X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)
print(X_train.shape)        # (60000, 784)
print(X_test.shape)

X_train = X_train.astype('float32')     # Ensure consistent datatype
X_test = X_test.astype('float32')

X_train /= 255.0                        # Normalize the data
X_test /= 255.0
print(X_train[0])

y_train = to_categorical(y_train, num_classes)   # Sets the output to 10 bin
y_test = to_categorical(y_test, num_classes)
print(y_train.shape)                    # (60000, 10)
print(y_test.shape)                     # (10000, 10)

# Build the Model with the Convolutional NN Layers
cnn = Sequential()
cnn.add(Conv2D(32, kernel_size=(5, 5), input_shape=(28,28,1), padding='same', activation='relu'))       # First Conv Layer
cnn.add(MaxPooling2D())             # Max Pooling
cnn.add(Conv2D(64, kernel_size=(5, 5), padding='same', activation='relu'))       # Second Conv Layer. No need to specify the input_shape, Keras will take care of this
cnn.add(MaxPooling2D())
cnn.add(Flatten())      # Network is flattened because a Fully Connected Layer (FCL) is coming next
cnn.add(Dense(1024, activation='relu'))
cnn.add(Dense(10, activation='softmax'))        # Outer Layer

# Compile the Model
cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
cnn.summary()

# Train the Model
history_cnn = cnn.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

# Plot accuracy of the training model
plt.plot(history_cnn.history_cnn['acc'])

# Plot accuracy of training and validation, with loss
plt.plot(history_cnn.history_cnn['acc'])
plt.plot(history_cnn.history_cnn['val_acc'])
plt.plot(history_cnn.history_cnn['loss'])

# Evaluate the Model
score = cnn.evaluate(X_test, y_test)
score


# NB:: If the model have previously been trained, you can access the model like this

#cnn.load_weights('weights/cnn-model5.h5')
score = cnn.evaluate(X_test, y_test)
score
