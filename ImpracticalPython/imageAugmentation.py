import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, load_img
from keras.applications.inception_v3 import preprocess_input

# ** Check that sample-confirm folder is empty **

# Generate
train_datagen = ImageDataGenerator (
    preprocessing_function=preprocess_input,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator (
    preprocessing_function=preprocess_input,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

jf_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    horizontal_flip=True
)

# Check on a sample to confirm the image generators work as expected
train_generator = train_datagen.flow_from_directory('images/sample-train/', target_size=(150,150), save_to_dir='images/sample-confirm/')

i = 0
for batch in train_datagen.flow_from_directory('images/sample-train/', target_size=(150,150), save_to_dir='images/sample-confirm/'):
    i += 1
    if (i > 10):
        break

j = 0
for batch in jf_datagen.flow_from_directory('images/sample-train/', target_size=(150,150), save_to_dir='images/sample-confirm/'):
    j += 1
    if (j > 10):
        break