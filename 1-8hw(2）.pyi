# !/usr/bin/python

# -*- coding: utf-8 -*-

import numpy as np
np.random.seed(1337)
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation,Convolution2D, MaxPooling2D, Flatten,Dropout
#import matplotlib.pyplot as plt
from keras.optimizers import RMSprop
from keras.optimizers import Adam


(x_train,y_train),(x_test,y_test) = mnist.load_data()


x_train = x_train.reshape(-1,1,28,28)
x_test = x_test.reshape(-1,1,28,28)
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test,num_classes=10)


model = Sequential()


model.add(Convolution2D(
        nb_filter =32,
        nb_row=5,
        nb_col=5,
        border_mode='same',
        input_shape=(1,
                     28,28),
        ))
model.add(Activation('relu'))


model.add(MaxPooling2D(
        pool_size=(2,2),
        strides=(2,2),
        border_mode='same',
        ))


model.add(Convolution2D(64,5,5,border_mode='same'))
model.add(Activation('relu'))


model.add(MaxPooling2D(pool_size=(2,2), border_mode='same'))


model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(units=1024,activation='relu'))
model.add(Dense(10))
model.add(Activation('softmax'))


adam = Adam(lr=1e-4)


model.compile( #编译
        optimizer = adam,
        loss = 'categorical_crossentropy',
        metrics=['accuracy'],
        )

print("Training~~~~~~~~")
model.fit(x_train,y_train, epochs=1, batch_size=32)

print("\nTesting~~~~~~~~~~")
loss,accuracy = model.evaluate(x_test,y_test)

print('\ntest loss:',loss)
print('\ntest accuracy:', accuracy)