import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.optimizers import SGD, Adam
from keras.utils import np_utils
from keras.datasets import mnist


# categorical_crossentropy


def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    number = 10000
    x_train = x_train[0:number]
    y_train = y_train[0:number]
    x_train = x_train.reshape(number, 28 * 28)
    x_test = x_test.reshape(x_test.shape[0], 28 * 28)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    # convert class vectors to binary class matrices
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
    x_train = x_train
    x_test = x_test
    # 加上x_test=np.random.normal(x_test)
    x_test = np.random.normal(x_test)
    x_train = x_train / 255
    x_test = x_test / 255
    return (x_train, y_train), (x_test, y_test)



(x_train, y_train), (x_test, y_test) = load_data()
model = Sequential()
model.add(Dense(input_dim=28 * 28, units=689, activation='relu'))

# 添加droput,正常设为0.5,这里trian的精度很高，故而设的高一些，为0.7；

# droput削弱trian的overfitting；

model.add(Dropout(0.7))
model.add(Dense(units=689, activation='relu'))
model.add(Dropout(0.7))
model.add(Dense(units=689, activation='relu'))
model.add(Dropout(0.7))
# for i in range(10):
#          model.add(Dense(units=689, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) # case 3
#model.compile(loss='mse', optimizer='adam', metrics=['accuracy']) # case 4
#model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.1), metrics=['accuracy']) #case 2
#model.compile(loss='mse', optimizer=SGD(lr=0.1), metrics=['accuracy']) # case 1
model.fit(x_train, y_train, batch_size=10, epochs=20)
result = model.evaluate(x_train, y_train, batch_size=10000)
print('\nTrain Acc', result[1])
result = model.evaluate(x_test, y_test, batch_size=10000)
print('\nTest Acc', result[1])
result = model.predict(x_test)

# 结果 10层网络，train acc = 96%；test acc = 92%
#     3层网络，train acc = 99%；test acc = 96%
# 增加了droput，3层网络，train acc = 98%； test acc = 95%
