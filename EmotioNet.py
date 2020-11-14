import sys
import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, AveragePooling2D, ZeroPadding2D
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.utils import np_utils


# Data processing

# Normalizing data
train_images = []
train_labels = []
test_images = []
test_labels = []


# Model parameters
n_labels = 5
batch_size = 64
epochs = 30
width, height = (48, 48)

# CNN Model Architecture
model = Sequential()

# 1. Adding convolutions
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(train_images.shape[1:])))  
model.add(Conv2D(64,kernel_size= (3, 3), activation='relu'))  
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2)))  
model.add(Dropout(0.5))  
  
#2nd convolution layer  
model.add(Conv2D(64, (3, 3), activation='relu'))  
model.add(Conv2D(64, (3, 3), activation='relu'))  
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2)))  
model.add(Dropout(0.5))  
  
#3rd convolution layer  
model.add(Conv2D(128, (3, 3), activation='relu'))  
model.add(Conv2D(128, (3, 3), activation='relu'))  
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2))) 

# 2. Fully connected Neural Network
model.add(Flatten())
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(n_labels, activation='softmax'))

#Compliling the model  
model.compile(loss=categorical_crossentropy,  
              optimizer=Adam(),  
              metrics=['accuracy'])  
  
#Training the model  
model.fit(train_images, train_labels,  
          batch_size=batch_size,  
          epochs=epochs,  
          verbose=1,  
          validation_data=(test_images, test_labels),  
          shuffle=True)  
  
  
#Saving the  model to  use it later on  
EmotioNet_json = model.to_json()  
with open("EmotioNet.json", "w") as json_file:  
    json_file.write(EmotioNet_json)  
model.save_weights("EmotioNet_weights.h5")  