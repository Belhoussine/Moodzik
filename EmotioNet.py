import sys
import pandas as pd
import numpy as np
import csv
import tensorflow as tf
from PIL import Image

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, AveragePooling2D, ZeroPadding2D
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.utils import np_utils


mood_map = {
    0: 'surprise', 
    1: 'anger', 
    2: 'disgust', 
    3: 'sadness', 
    4: 'happiness', 
    5: 'neutral', 
    6: 'fear', 
    7: 'contempt'
}

def mood_to_num(mood):
  for key, value in mood_map.items(): 
         if mood == value: 
             return key 

def num_to_mood(num):
  return mood_map[num]

# reading csv file
def read_csv(filename):
  labels=list()
  with open(filename) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      labels.append(row)
  return labels

# Defining paths
csv_path = "./Train_Dataset/labels.csv"
image_path = "./Train_Dataset/Images/"


# Defining arrays
train_images = []
train_labels = []
test_images = []
test_labels = []

# Model parameters
n_labels = 8
batch_size = 64
epochs = 30
width, height = (48, 48)

# Data pre-processing

# Reading csv
df= read_csv(csv_path) 

# Reading images and labels
for index, row in enumerate(df):
  imagename = row[1]
  try:
    image = Image.open(image_path + imagename)
    image = np.asarray(image.resize((48,48)))
    train_images.append(image)
    train_labels.append(mood_to_num(row[2]))
  except:
    continue



train_images = np.array(train_images, 'float32') / 255.0
train_labels = np.array(train_labels)

train_images = train_images.reshape(train_images.shape[0], 48, 48, 1)
train_labels = np_utils.to_categorical(train_labels, num_classes = n_labels)  

# print(train_images.shape)
# print(train_labels.shape)

# Image processing
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

# Training the model  
model.fit(train_images, train_labels,  
          batch_size=batch_size,  
          epochs=epochs,  
          verbose=1,
          shuffle = True) 
          # validation_data=(test_images, test_labels),  
          # shuffle=True)  
  
#Saving the  model to  use it later on  
# EmotioNet_json = model.to_json()  
# with open("EmotioNet.json", "w") as json_file:  
#     json_file.write(EmotioNet_json)  
# model.save_weights("EmotioNet_weights.h5")  