import sys
import pandas as pd
import numpy as np
import csv
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, AveragePooling2D, ZeroPadding2D
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.utils import np_utils




# reading csv file
def read_csv(filename):
  train_images = []
  train_labels = []
  test_images = []
  test_labels = []
  df = pd.read_csv(filename)

  for index, row in df.iterrows():  
    image = row['pixels'].split(" ")  
    try:  
        if 'Training' in row['Usage']:  
           train_images.append(np.array(image,'float32'))  
           train_labels.append(row['emotion'])  
        elif 'PublicTest' in row['Usage']:  
           test_images.append(np.array(image, 'float32'))  
           test_labels.append(row['emotion'])  
    except:  
        print(f"Error at index :{index}, row:{row}")  
  return np.array(train_images), np.array(train_labels), np.array(test_images), np.array(test_labels)


# Defining paths
dataset_path = "./Dataset/fer2013.csv"

# Model parameters
n_labels = 8
batch_size = 64
epochs = 30
width, height = (48, 48)

# Reading images and labels
train_images, train_labels, test_images, test_labels = read_csv(dataset_path)

# Data processing
train_images = train_images / 255.0
train_images = train_images.reshape(train_images.shape[0], 48, 48, 1)
train_labels = np_utils.to_categorical(train_labels, num_classes = n_labels)  


test_images = test_images / 255.0
test_images = test_images.reshape(test_images.shape[0], 48, 48, 1)
test_labels = np_utils.to_categorical(test_labels, num_classes = n_labels) 


# CNN Model Architecture
model = Sequential()

# 1. Adding convolutions
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(train_images.shape[1:])))  
model.add(BatchNormalization())
model.add(Conv2D(64,kernel_size= (3, 3), activation='relu'))  
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2)))  
model.add(Dropout(0.5))  
  
#2nd convolution layer  
model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3), activation='relu'))  
model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3), activation='relu'))  
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2)))  
model.add(Dropout(0.5))  
  
#3rd convolution layer  
model.add(Conv2D(128, (3, 3), activation='relu'))  
model.add(BatchNormalization())
model.add(Conv2D(128, (3, 3), activation='relu'))  
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2))) 

# 2. Fully connected Neural Network
model.add(Flatten())
model.add(Dense(4096, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(4096, activation='tanh'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.1))
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(n_labels, activation='softmax'))

#Compliling the model  
model.compile(loss=categorical_crossentropy,  
              optimizer=Adam(),  
              metrics=['accuracy'])  


# Training the model  
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