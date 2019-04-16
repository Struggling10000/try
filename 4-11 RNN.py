# coding:utf-8
__author__ = 'jmh081701'
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib import rnn
##过程会先在当前目录下的data寻找mnist的数据文件，如果没有数据文件就会去网上download下来.
mnist = input_data.read_data_sets("./data", one_hot=True)

train_rate = 0.001 #学习速率，
train_step = 10000  #
batch_size = 1280# 每批样本数
display_step = 100 #

frame_size = 28 # 序列里面每一个分量的大小，每一行像素是一个分量，
sequence_length = 28
hidden_num = 100 # 隐层神经元的个数
n_classes = 10   #分类的类别数

# 定义输入,输出
x = tf.placeholder(dtype=tf.float32, shape=[None, sequence_length * frame_size], name="inputx")

y = tf.placeholder(dtype=tf.float32, shape=[None, n_classes], name="expected_y")
# 定义权值
weights = tf.Variable(tf.truncated_normal(shape=[hidden_num, n_classes]))
bias = tf.Variable(tf.zeros(shape=[n_classes]))


# 定义RNN网络
def RNN(x, weights, bias):
    x = tf.reshape(x, shape=[-1, sequence_length, frame_size])
    # 先把输入转换为dynamic_rnn接受的形状：batch_size,sequence_length,frame_size这样子的
    #tf.nn.rnn_cell.BasicLSTMCell()
    rnn_cell = tf.nn.rnn_cell.BasicLSTMCell(hidden_num,forget_bias=1.0,state_is_tuple=True)
    # 生成hidden_num个隐层的RNN网络,rnn_cell.output_size等于隐层个数，state_size也是等于隐层个数，但是对于LSTM单元来说这两个size又是不一样的。
    # 这是一个深度RNN网络,对于每一个长度为sequence_length的序列[x1,x2,x3,...,]的每一个xi,都会在深度方向跑一遍RNN,每一个都会被这hidden_num个隐层单元处理。
    output, states = tf.nn.dynamic_rnn(rnn_cell, x, dtype=tf.float32)
    # 此时output就是一个[batch_size,sequence_length,rnn_cell.output_size]形状的tensor

    return tf.nn.softmax(tf.matmul(output[:, -1, :], weights) + bias, 1)


predy = RNN(x, weights, bias)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predy, labels=y))
train = tf.train.AdamOptimizer(train_rate).minimize(cost)

correct_pred = tf.equal(tf.argmax(predy, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.to_float(correct_pred))

sess = tf.Session()
sess.run(tf.initialize_all_variables())
step = 1
testx, testy = mnist.test.next_batch(batch_size)
while step <= train_step:
    batch_x, batch_y = mnist.train.next_batch(batch_size)
    #    batch_x=tf.reshape(batch_x,shape=[batch_size,sequence_length,frame_size])
    _loss, __ = sess.run([cost, train], feed_dict={x: batch_x, y: batch_y})
    if step % display_step == 0:
        acc, loss = sess.run([accuracy, cost], feed_dict={x: testx, y: testy})
        print(step, acc, loss)
    step += 1

