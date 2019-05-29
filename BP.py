# -*- coding: utf-8 -*-
import numpy as np # 用来做矩阵运算
import pandas as pd # 用来做数据分析
from keras.models import Sequential # 模型&序列串行的类
from keras.layers import Dense # 隐含层的节点与前后都有连接，密度很高
from keras.wrappers.scikit_learn import KerasClassifier # 一个包裹的API
from keras.utils import np_utils # 待会解释
from sklearn.model_selection import cross_val_score # 交叉验证，准确度与得分
from sklearn.model_selection import KFold # KFold 将数据集中n-1个作为训练集，1个作为测试集，进行n次
from sklearn.preprocessing import LabelEncoder # 预处理，用于将标签的字符串转换为数字
from keras.models import model_from_json # 训练好模型，最后存起来，下次用完就无需再次训练，用的时候读就可以
from sklearn import metrics
import time

# reproducibility
seed = 13
np.random.seed(seed) # 种子数，随机的值是一样的


# define a network
def baseline_model():
    """
    三层结构
    输入层纬度为4：与特征数目有关
    隐含层纬度为7：自定义，一般为纺锤形
    输出层纬度为3：三个类别
    """
    model = Sequential()
    # 按顺序构建网络
    model.add(Dense(4,input_dim=4,activation='tanh'))
    # 第一层，输入层到隐含层，有7个节点，输入数据纬度4维，双曲正切函数
    model.add(Dense(3,activation='softmax'))
    # 隐含层到输出层的结构，输出层与类别的个数一样，隐藏层的节点自己定
    model.compile(loss='mean_squared_error', optimizer='sgd',metrics=['accuracy'])
    # 编译模型：用均方差来衡量网络输出的差，训练优化网络-随机梯度下降法，metrics解释如何衡量模型的好坏
    return model


def test_iris():
    # load data
    start_time=time.time()
    df = pd.read_csv('Irisdata.csv')  # 0-3是特征，4是类别，存了一个表格
    X = df.values[1:, 0:4].astype(float)  # numpyarray所有行的0-3列，浮点型float差不多了，不用double，以节约内存
    Y = df.values[1:, 4]  # 第4列

    # encode
    encoder = LabelEncoder()  # 实例
    Y_encoded = encoder.fit_transform(Y)  # 编码，字符串变为数字
    Y_onehot = np_utils.to_categorical(Y_encoded)  # onehot编码

    estimator = KerasClassifier(build_fn=baseline_model, epochs=20, batch_size=1, verbose=1)
    # 用于交叉验证，epochs为训练次数20次，batch_size批次处理为1个训练数据，输入信息的浓缩程度verbose为1

    # evalute 评估系统
    kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
    # kfold这个定义的交叉验证的方法
    # 150个数据分为10份，挑9份训练数据，1份测试数据
    # shuffle随机打乱
    # 使得重复结果一致
    result = cross_val_score(estimator, X, Y_onehot, cv=kfold)
    # 调用estimator的训练结构对象
    print("Accuracy of cross validation, mean %.2f, std %.2f" % (result.mean(), result.std()))
    # 打印结果

    # save model 将模型存起来
    estimator.fit(X, Y_onehot)  # 做训练数据
    model_json = estimator.model.to_json()  # 将其模型转换为json
    # 保存输入、隐藏、输出层结构，激活函数
    with open("./model.json", "w")as json_file:
        json_file.write(model_json)
        # 权重不在json中,只保存网络结构

    # 储存权重
    estimator.model.save_weights("model.h5")
    print("saved model to disk")

    # load model and use it for prediction
    json_file = open("./model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)  # 读入网络结构
    loaded_model.load_weights("model.h5")  # 读入权重
    print("loaded model from disk")

    predicted = loaded_model.predict(X)  # 做预测
    # print("predicted probability: " + str(predicted))

    predicted_label = loaded_model.predict_classes(X)  # 直接说明类别是什么
    print("predicted label: " + str(predicted_label))
    #print(metrics.accuracy_score(y_true=Y_onehot, y_pred=predicted_label),
     #     (metrics.f1_score(y_true=Y_onehot, y_pred=predicted_label,average='macro')))
    end_time=time.time()
    print("耗时为："+str(end_time-start_time))
    return 0
def test_nonnamedata():
    start_time=time.time()
    df = pd.read_csv('ELM-data.csv')  # 0-3是特征，4是类别，存了一个表格
    X = df.values[1:, 1:].astype(float)  # numpyarray所有行的0-3列，浮点型float差不多了，不用double，以节约内存
    Y = df.values[1:, 0]  # 第4列

    # encode
    encoder = LabelEncoder()  # 实例
    Y_encoded = encoder.fit_transform(Y)  # 编码，字符串变为数字
    Y_onehot = np_utils.to_categorical(Y_encoded)  # onehot编码

    estimator = KerasClassifier(build_fn=baseline_model, epochs=20, batch_size=1, verbose=1)
    # 用于交叉验证，epochs为训练次数20次，batch_size批次处理为1个训练数据，输入信息的浓缩程度verbose为1

    # evalute 评估系统
    kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
    # kfold这个定义的交叉验证的方法
    # 150个数据分为10份，挑9份训练数据，1份测试数据
    # shuffle随机打乱
    # 使得重复结果一致
    result = cross_val_score(estimator, X, Y_onehot, cv=kfold)
    # 调用estimator的训练结构对象
    print("Accuracy of cross validation, mean %.2f, std %.2f" % (result.mean(), result.std()))
    # 打印结果

    # save model 将模型存起来
    estimator.fit(X, Y_onehot)  # 做训练数据
    model_json = estimator.model.to_json()  # 将其模型转换为json
    # 保存输入、隐藏、输出层结构，激活函数
    with open("./model.json", "w")as json_file:
        json_file.write(model_json)
        # 权重不在json中,只保存网络结构

    # 储存权重
    estimator.model.save_weights("model.h5")
    print("saved model to disk")

    # load model and use it for prediction
    json_file = open("./model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)  # 读入网络结构
    loaded_model.load_weights("model.h5")  # 读入权重
    print("loaded model from disk")

    predicted = loaded_model.predict(X)  # 做预测
    print("predicted probability: " + str(predicted))

    predicted_label = loaded_model.predict_classes(X)  # 直接说明类别是什么
    print("predicted label: " +str(predicted_label))
    # print(metrics.accuracy_score(y_true=Y_onehot, y_pred=predicted_label),
    #       (metrics.f1_score(y_true=Y_onehot, y_pred=predicted_label)))
    end_time=time.time()
    print("耗时为："+str(end_time-start_time))
    return 0
if __name__=='__main__':
    test_iris()
    # test_nonnamedata()