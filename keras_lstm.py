import keras
from keras.layers import LSTM
from keras.layers import Dense, Activation
from keras.datasets import mnist
from keras.models import Sequential
from keras.optimizers import Adam

import matplotlib.pyplot as plt

learning_rate = 0.001
training_iters = 10
batch_size = 128
display_step = 10

n_input = 28
n_step = 28
n_hidden = 128
n_classes = 10
# mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, n_step, n_input)
x_test = x_test.reshape(-1, n_step, n_input)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

y_train = keras.utils.to_categorical(y_train, n_classes)
y_test = keras.utils.to_categorical(y_test, n_classes)

model = Sequential()
model.add(LSTM(n_hidden,batch_input_shape=(None, n_step, n_input), unroll=True))

model.add(Dense(n_classes))
model.add(Activation('softmax'))

adam = Adam(lr=learning_rate)
model.summary()
model.compile(optimizer=adam,loss='categorical_crossentropy',metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=batch_size,epochs=training_iters,verbose=1, validation_data=(x_test, y_test))

scores = model.evaluate(x_test, y_test, verbose=0)
print('LSTM test score:', scores[0])
print('LSTM test accuracy:', scores[1])

resultdata = history.history
val_acc = resultdata['val_acc']
val_loss = resultdata['val_loss']
acc = resultdata['acc']
loss = resultdata['loss']

# #plt.title("Keras_LSTM_validation")
# plt.xlabel("epoch")
# plt.ylabel("acc")
# plt.plot(range(1, len(acc)+1), acc, 'r.-', label="Training acc")
# plt.plot(range(1, len(val_acc)+1), val_acc, 'b。-', label="Validation acc")
# plt.xlim(0, len(val_loss)+2)
# plt.ylim(0, 1.2)
# plt.legend()
# plt.show()

#plt.title("Keras_LSTM_testing")
plt.xlabel("epoch")
plt.ylabel("acc")
plt.plot(range(1, len(loss)+1), loss, 'ro-', label="Training loss")
plt.plot(range(1, len(val_loss)+1), val_loss, 'bo-', label="Validation loss")
plt.plot(range(1, len(acc)+1), acc, 'r.-', label="Training acc")
plt.plot(range(1, len(val_acc)+1), val_acc, 'b.-', label="Validation acc")
plt.xlim(0, len(val_loss)+2)
plt.ylim(0, 1.2)
plt.legend()
plt.show()
