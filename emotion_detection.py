import sys
import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, AveragePooling2D
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.utils import np_utils


# Data processing

    # Normalizing data


# CNN Model Architecture
model = Sequential()
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape = ()))
