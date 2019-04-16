import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1337)

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import SimpleRNN, Activation, Dense
from keras.optimizers import Adam

TIME_STEPS = 28  #一张图片分多少次读入
INPUT_SIZE = 28  #每次输入的多少
BATCH_SIZE = 50
BATCH_INDEX = 0
OUTPUT_SIZE = 10
CELL_SIZE = 50   # RNN中的隐藏层的个数
LR = 0.001

# 导入数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data pre-processing
X_train = X_train.reshape(-1, 28, 28) / 255.  # normalize  归一化
X_test = X_test.reshape(-1, 28, 28) / 255.  # normalize
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

# build RNN model
model = Sequential()

# RNN cell
model.add(SimpleRNN(
    batch_input_shape=(None, TIME_STEPS, INPUT_SIZE),
    output_dim=CELL_SIZE,
    unroll=True,
))

# output layer
model.add(Dense(OUTPUT_SIZE))
model.add(Activation('softmax'))

# optimizer
adam = Adam(LR)
model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

costList = []
accuracyList = []
# training
for step in range(40001):
    X_batch = X_train[BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :, :]
    Y_batch = y_train[BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :]
    cost = model.train_on_batch(X_batch, Y_batch)
    BATCH_INDEX += BATCH_SIZE
    BATCH_INDEX = 0 if BATCH_INDEX >= X_train.shape[0] else BATCH_INDEX

    if step % 500 == 0:
        cost, accuracy = model.evaluate(X_test, y_test, batch_size=y_test.shape[0], verbose=False)
        #x_train, y_train, batch_size=batch_size,epochs=training_iters,verbose=1, validation_data=(x_test, y_test
        costList.append(cost)
        accuracyList.append(accuracy)
        print(step,'  -loss: ', cost, '-acc: ', accuracy)


index = range(0, 40001, 500)
# print(index)
# print(len(index))
# print(len(range(len(costList))))
# print(len(range(len(accuracyList))))
# print(len(costList))
# print(len(accuracyList))
#plt.title("Keras_RNN")
plt.xlabel("step")
plt.ylabel("acc")
plt.plot(index, costList, 'r.-', label="Loss")
plt.plot(index, accuracyList, 'b.-', label="Acc")
plt.legend()
plt.show()
