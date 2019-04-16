## -*- coding: utf-8 -*- !/usr/bin/python


# coding=utf-8

# -*- coding: utf-8 -*-
import numpy as np
np.random.seed(1337) #for reproducibility再现性
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential#按层
from keras.layers import Dense, Activation,Convolution2D, MaxPooling2D, Flatten,Dropout
#import matplotlib.pyplot as plt
from keras.optimizers import RMSprop
from keras.optimizers import Adam

#dowmload the mnisst the path '~/.keras/datasets/' if it is the first time to be called
#x shape (60000 28*28),y shape(10000,)
(x_train,y_train),(x_test,y_test) = mnist.load_data()#0-9的图片数据集

#data pre-processing
x_train = x_train.reshape(-1,1,28,28)#-1代表个数不限，1为高度，黑白照片高度为1
x_test = x_test.reshape(-1,1,28,28)
y_train = np_utils.to_categorical(y_train, num_classes=10) #把标签变为10个长度，若为1，则在1处为1，剩下的都标为0
y_test = np_utils.to_categorical(y_test,num_classes=10)

#Another way to build CNN
model = Sequential()

#Conv layer 1 output shape (32,28,28)
model.add(Convolution2D(
        nb_filter =32,#滤波器装了32个，每个滤波器都会扫过这个图片，会得到另外一整张图片，所以之后得到的告诉是32层
        nb_row=5,
        nb_col=5,
        border_mode='same', #padding method
        input_shape=(1,      #channels  通道数
                     28,28),  #height & width 长和宽
        ))
model.add(Activation('relu'))

#Pooling layer 1 (max pooling) output shape (32,14,14)
model.add(MaxPooling2D(
        pool_size=(2,2), #2*2
        strides=(2,2),  #长和宽都跳两个再pool一次
        border_mode='same', #paddingmethod
        ))

#Conv layers 2 output shape (64,14,14)
model.add(Convolution2D(64,5,5,border_mode='same'))
model.add(Activation('relu'))

#Pooling layers 2 (max pooling) output shape (64,7,7)
model.add(MaxPooling2D(pool_size=(2,2), border_mode='same'))

#Fully connected layer 1 input shape (64*7*7) = (3136)
#Flatten 把三维抹成一维，全连接
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(units=1024,activation='relu'))
#Fully connected layer 2 to shape (10) for 10 classes
model.add(Dense(10)) #输出10个单位
model.add(Activation('softmax')) #softmax用来分类

#Another way to define optimizer
adam = Adam(lr=1e-4)

# We add metrics to get more results you want to see
model.compile( #编译
        optimizer = adam,
        loss = 'categorical_crossentropy',
        metrics=['accuracy'], #在更新时同时计算一下accuracy
        )

print("Training~~~~~~~~")
#Another way to train the model
model.fit(x_train,y_train, epochs=1, batch_size=32) #训练2大批，每批32个

print("\nTesting~~~~~~~~~~")
#Evalute the model with the  metrics we define earlier
loss,accuracy = model.evaluate(x_test,y_test)

print('\ntest loss:',loss)
print('\ntest accuracy:', accuracy)







































#from Tkinter import *
# from turtle import *
# import turtle as t
# #from __future__ import print_function
# import os, sys
# import Image
#
#
# def calcu_sub_str_num(mom_str,sun_str):
#   print('打印母字符串：',mom_str)   #打印出母字符串
#   print( '打印子字符串：',sun_str)  #打印出子字符串
#   print('打印母字符串长度：',len(mom_str)) #打印出母字符串长度
#   print( '打印子字符串长度：',len(sun_str))  #打印出子字符串长度
#   count = 0                                  #定义计数器初始值
#   #使用循环遍历字符串，第一次循环，通过切片获取下标从0开始与子字符串长度一致的字符串，并与字符串比较，如果等于子字符串count+1
#   #第二次循环，通过切片获取下标从1开始与子字符串长度一致的字符串，并与字符串比较，如果等于子字符串则count+1，以此类推直到遍历完成
#   for i in range(len(mom_str)-1): #因为i的下标从0开始，所以len（mom_str）-1
#       if mom_str[i:i+len(sun_str)] == sun_str:
#           count+=1
#   return count
#
# mom_str = input('please input mother string:') #使用input获取输入母字符串
# sun_str = input('please input child string:') #使用input获取输入子字符串
# print('子字符串在母字符串中出现的次数：%d'%calcu_sub_str_num(mom_str,sun_str))#%d为数字占位符


# import Image
#
# img=Image.open("p1.eps")
#
# img.save("p1.jpg")


#
# t.forward(100)
# ts = t.getscreen()
#
# ts.getcanvas().postscript(file="duck.eps")
#
# # for infile in sys.argv[1:]:
# infile = Image.open("duck.eps")
# infile.save("duck.jpg",'jpg')
# t.forward(100)
# ts = t.getscreen()
#
# ts.getcanvas().postscript(file="duck.eps")
#
# # for infile in sys.argv[1:]:
# infile = Image.open("duck.eps")
# infile.save("duck.jpg",'jpg')


# import sys
#
# def check_valid(mg, x, y):
#     if x >= 0 and x < len(mg) and y >= 0 and y < len(mg[0]) \
#             and mg[x][y] == 1:
#         return True
#     else:
#         return False
#
#
# # 迷宫结果优化
# def process(step):
#     # 先识别哪些无路可走的点的下一个点
#     change_records = []
#     for i in range(len(step) - 1):
#         if (abs(step[i][0] - step[i + 1][0]) == 0 and abs(step[i][1] - step[i + 1][1]) == 1) or \
#                 (abs(step[i][0] - step[i + 1][0]) == 1 and abs(step[i][1] - step[i + 1][1]) == 0):
#             pass
#         else:
#             change_records.append(i + 1)
#     # print(change_records)
#
#     # 然后根据这些点识别出这个点的最远回退点
#     clip_nums = []
#     for i in change_records:
#         for j in range(i):
#             if (abs(step[j][0] - step[i][0]) == 0 and abs(step[j][1] - step[i][1]) == 1) or \
#                     (abs(step[j][0] - step[i][0]) == 1 and abs(step[j][1] - step[i][1]) == 0):
#                 break
#         clip_nums.append((j, i))
#     # print(clip_nums)
#
#     # 注意回退点之间的包含关系, 逆序处理, 是为了规避顺序对列表进行处理后下标偏移的问题
#     record = []
#     for i in clip_nums[::-1]:
#         if not (i[0] in record or i[1] in record):
#             step = step[:i[0] + 1] + step[i[1]:]
#         record += list(range(i[0], i[1]))
#     print(step)
#
#
# step = []
#
#
# def walk(mg, x, y):
#     global step
#     if x == 0 and y == 0:
#         step.append((x, y))
#         process(step)
#         print("Walk success!")
#         sys.exit()
#
#     if check_valid(mg, x, y):
#         step.append((x, y))
#         mg[x][y] = 2
#         walk(mg, x, y + 1)
#         walk(mg, x, y - 1)
#         walk(mg, x - 1, y)
#         walk(mg, x + 1, y)
#
#
# mg = [[1, 0, 1, 1, 1, 0],
#       [1, 1, 1, 0, 1, 1],
#       [0, 0, 0, 1, 0, 1],
#       [0, 1, 1, 1, 0, 1],
#       [0, 1, 0, 1, 1, 1],
#       [1, 1, 1, 0, 0, 0]]
#
# walk(mg, 5, 0)


# import numpy as np
# from numpy import *
# # get_best_team(3,[],2,50)20
# # 12 35 68 12 12 44 45 23 24 25 12 14 45 23 45 78 91 23 20 22
# # 4 3
# # def get_best_team( numbers, abilities, selectedNum, distance):
# numbers=20
# abilities=[12, 35 ,68 ,12 ,12, 44 ,45, 23, 24 ,25 ,12 ,14 ,45, 23 ,45, 78, 91 ,23 ,20 ,22]
# selectedNum=4
# distance=3
# # list=[0]*numbers
# # list=[list]*numbers
# list=np.zeros((numbers,numbers))
# #print(data1)
# #list= [[0 for i in range(3)] for i in range(3)]
# print(list)
# lista=abilities
# d=distance
# # list[1][1]=1
# # list[1][2]=3
#
# for i in range(numbers):
#     for j in range(i+1,i+d+1) :
#         if j<numbers:
#            list[i][j]=lista[i]*lista[j]
# print(list)
#
# X=[0]*numbers
# for j in range(selectedNum):
#     if X.count(1)!=selectedNum:
#         new_list=[]
#         for i in range(len(list)):
#             new_list.append(max(list[i]))
#         maxnum=max(new_list)
#
#         num=np.argwhere(list == maxnum)
#         listmaxloc=num[0]
#         row=listmaxloc[0]
#         col=listmaxloc[1]
#         X[row]=1
#         X[col]=1
#         print(X[col])
#
#     list[row][col]=0
# fin=1
# for i in range(numbers):
#     if X[i]==1:
#         fin=fin*abilities[i]
# print(fin)
#
#
#

#
# number =[1,8,2,3,  9,7 , 10]
# print(number)
# list1=[0]
# list = list1 * 10
# for i in number:
#     list[i-1]=1
# num1=[i for i in range(len(list)) if list[i] == 0]
# num1.sort()
# print(num1)
# t=len(num1)
#
#
#
# finnum = ''
# for i in range(t):
#     finnum = finnum + str(num1[i]+1)
#     print(str(num1[i]))
# print(finnum)
# print(int(finnum) % 11)
#
# import datetime
#
# def getday(str='2017-08-15',n=0):
#     y=int(str[0:4])
#     m=int(str[5:7])
#     d=int(str[8:10])
#     n=n+d
#     if m in [1,3,5,7,8,10,12] and n>31:
#         m=m+1
#         n=n-31
#     elif m in [4,6,9,11]and n>30:
#         m=m+1
#         n=n-1
#     elif m==2:
#         if
#     if
#
#
#     d = result_date.strftime('%Y-%m-%d')
#     return d
# print(getday('2017-08-15',21)) #8月15日后21天
# print( getday('2017-09-15',-10) )#9月1日前10天
#
# # data = [[col for col in range(4)] for row in range(4)]
# # print(data)
# # row=4
# # col =4
# # if row ==col :
# #     for i in [1,col] :
# #         for j in [i,col,1]:
# #             temp=data[i-1][j-1]
# #             data[i-1][j-1]=data[j-1][i-1]
# #             data[j-1][i-1]=temp
#
# #print(data)
#
#
#
# for row_index, row in enumerate(data):
#     for col_index in range(row_index, len(row)):
#         tmp = data[col_index][row_index]  # 设置一个临时变量
#         data[col_index][row_index] = row[col_index]
#         data[row_index][col_index] = tmp
#    # print('')  # 防止打印结果看上去混乱，输入一个空内容
#
# print(data)
#
#
# data=[[i for i in range(4)] for raw in range(4)]
# for ele in data:
#     print(ele)
# a=len(data)
#
# for i in range(a):#外层循环
#      for j in range(i+1,len(data[i])): #内层循环        #交换数据
#                       temp=data[i][j]
#                       data[i][j]=data[j][i]
#                       data[j][i]=temp
# for ele in data:
#   print (ele)

# from flask import Flask,render_template,request,redirect,session
# app = Flask(__name__)
# app.secret_key = "sdsfdsgdfgdfgfh"   # 设置session时，必须要加盐，否则报错
#
# def wrapper(func):
#     def inner(*args,**kwargs):
#         if not session.get("user_info"):
#             return redirect("/login")
#         ret = func(*args,**kwargs)
#         return ret
#     return inner
#
# @app.route("/login",methods=["GET","POST"])  # 指定该路由可接收的请求方式，默认为GET
# def login():
#     if request.method=="GET":
#         return render_template("login.html")
#     else:
#         # print(request.values)   #这个里面什么都有，相当于body
#         username = request.form.get("username")
#         password = request.form.get("password")
#         if username=="haiyan" and password=="123":
#             session["user_info"] = username
#             # session.pop("user_info")  #删除session
#             return redirect("/index")
#         else:
#             # return render_template("login.html",**{"msg":"用户名或密码错误"})
#             return render_template("login.html",msg="用户名或者密码错误")
#
# @app.route("/index",methods=["GET","POST"])
# @wrapper    #自己定义装饰器时，必须放在路由的装饰器下面
# def index():
#     # if not session.get("user_info"):
#     #     return redirect("/login")
#     return render_template("index.html")
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
# i=1
# for num in range(i,0,-1):
#     print(num)

# t.pendown()
#      t.fd(10)
#      turtleloc.append(t.pos())
#      print(t.pos())
#      t.penup()
#      t.fd(10)
#      t.pendown()
#      t.right(90)
#      t.fd(10)
#      t.goto(turtleloc.pop())
#      t.penup()
# #anay_structofgly(str,list)
#      # list=['asd','qwe','sdf']
#      # print(list.pop())
#      # print(list)
#      # print(len(list))
#
# class Node:
#     def __init__(self,value=None,left=None,right=None):
#          self.value=value
#          self.left=left    #左子树
#          self.right=right  #右子树
#
#
# def preTraverse(root):
#     '''
#     前序遍历
#     '''
#     if root == None:
#         return
#     print(root.value)
#     preTraverse(root.left)
#     preTraverse(root.right)
#
#
# def midTraverse(root):
#     '''
#     中序遍历
#     '''
#     if root == None:
#         return
#     midTraverse(root.left)
#     print(root.value)
#     midTraverse(root.right)
#
#
# def afterTraverse(root):
#     '''
#     后序遍历
#     '''
#     if root == None:
#         return
#     afterTraverse(root.left)
#     afterTraverse(root.right)
#     print(root.value)
#
# if __name__=='__main__':
#     root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
#     print('前序遍历：')
#     preTraverse(root)
#     print('\n')
#     print('中序遍历：')
#     midTraverse(root)
#     print('\n')
#     print('后序遍历：')
#     afterTraverse(root)
#     print('\n')


# import turtle
# from datetime import *
#
#
# # 抬起画笔，向前运动一段距离放下
# def Skip(step):
#     turtle.penup()
#     turtle.forward(step)
#     turtle.pendown()
#
#
# def mkHand(name, length):
#     # 注册Turtle形状，建立表针Turtle
#     turtle.reset()
#     Skip(-length * 0.1)
#     # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
#     turtle.begin_poly()
#     turtle.forward(length * 1.1)
#     # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
#     turtle.end_poly()
#     # 返回最后记录的多边形。
#     handForm = turtle.get_poly()
#     turtle.register_shape(name, handForm)
#
#
# def Init():
#     global secHand, minHand, hurHand, printer
#     # 重置Turtle指向北
#     turtle.mode("logo")
#     # 建立三个表针Turtle并初始化
#     mkHand("secHand", 135)
#     mkHand("minHand", 125)
#     mkHand("hurHand", 90)
#     secHand = turtle.Turtle()
#     secHand.shape("secHand")
#     minHand = turtle.Turtle()
#     minHand.shape("minHand")
#     hurHand = turtle.Turtle()
#     hurHand.shape("hurHand")
#
#     for hand in secHand, minHand, hurHand:
#         hand.shapesize(1, 1, 3)
#         hand.speed(0)
#
#     # 建立输出文字Turtle
#     printer = turtle.Turtle()
#     # 隐藏画笔的turtle形状
#     printer.hideturtle()
#     printer.penup()
#
#
# def SetupClock(radius):
#     # 建立表的外框
#     turtle.reset()
#     turtle.pensize(7)
#     for i in range(60):
#         Skip(radius)
#         if i % 5 == 0:
#             turtle.forward(20)
#             Skip(-radius - 20)
#
#             Skip(radius + 20)
#             if i == 0:
#                 turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
#             elif i == 30:
#                 Skip(25)
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-25)
#             elif (i == 25 or i == 35):
#                 Skip(20)
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-20)
#             else:
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#             Skip(-radius - 20)
#         else:
#             turtle.dot(5)
#             Skip(-radius)
#         turtle.right(6)
#
#
# def Week(t):
#     week = ["星期一", "星期二", "星期三",
#             "星期四", "星期五", "星期六", "星期日"]
#     return week[t.weekday()]
#
#
# def Date(t):
#     y = t.year
#     m = t.month
#     d = t.day
#     return "%s %d%d" % (y, m, d)
#
#
# def Tick():
#     # 绘制表针的动态显示
#     t = datetime.today()
#     second = t.second + t.microsecond * 0.000001
#     minute = t.minute + second / 60.0
#     hour = t.hour + minute / 60.0
#     secHand.setheading(6 * second)
#     minHand.setheading(6 * minute)
#     hurHand.setheading(30 * hour)
#
#     turtle.tracer(False)
#     printer.forward(65)
#     printer.write(Week(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.back(130)
#     printer.write(Date(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.home()
#     turtle.tracer(True)
#
#     # 100ms后继续调用tick
#     turtle.ontimer(Tick, 100)
#
#
# def main():
#     # 打开/关闭龟动画，并为更新图纸设置延迟。
#     turtle.tracer(False)
#     Init()
#     SetupClock(160)
#     turtle.tracer(True)
#     Tick()
#     turtle.mainloop()
#
#
# if __name__ == "__main__":
#     main()
#
# def changeList(list1):
#     list1.append('newStr')
#
#     print("函数中的list ：", list1)
#
#
# # 定义变量num，赋初始值为10
#
# list1 = [1, 2, 3]
#
# print("调用函数前的list: ", list1)
#
# changeList(list1)
#
# print("调用函数后的list：", list1)

# str_1='wo shi yi zhi da da niu '
# char_1=str(input('Please input the Char you want:'))
# count=0
# str_list=list(str_1)
# for each_char in str_list:
#  count+=1
#  if each_char==char_1:
#   print(each_char,count-1)

#
#
# import sys
#
# class MyClass():
#     def __init__(self, name = ""):
#         self.name = name
#         self.data_dic = {}
#         self.index = -1
#
#     class Struct():
#         def __init__(self, contents, name, message, status, num = -1):
#             self.contents = contents
#             self.name = name
#             self.message = message
#             self.status = status
#             self.line_num = num
#     #return struct item.
#     def make_struct(self, contents, name, message, status, num = -1):
#         return self.Struct(contents, name, message, status, num)
#
# if __name__ == "__main__":
#     test = MyClass()
#     test_struct1 = test.make_struct("hello world","s2","你好","success")
#     test_struct2 = test.make_struct("hello world","s2","你好","success")
#
#
#
#
import turtle as t
import random as r


# def pink():
#     color = (1, r.random(), 1)
#     return color
#
#
# def randomrange(min, max):
#     return min + (max- min)*r.random()
#
#
# def moveto(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#
#
# def heart(r, a):
#     factor = 180
#     t.seth(a)
#     t.circle(-r, factor)
#     t.fd(2 * r)
#     t.right(90)
#     t.fd(2 * r)
#     t.circle(-r, factor)
#
#
# t.setup(800, 800, 200, 200)
# t.speed(9)
# t.pensize(1)
# t.penup()
#
# for i in range(3):
#     t.goto(randomrange(-300, 300), randomrange(-300, 300))
#     t.begin_fill()
#     t.fillcolor(pink())
#     heart(randomrange(10, 50), randomrange(0, 90))
#     t.end_fill()
#
# moveto(400, -400)
#
# t.done()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import matplotlib.pyplot as plt
# # import matplotlib
# # import numpy as np
# # x=np.arange(1,17,1) #生成散点列表作为x的值
# # y=np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60]) #给定y的散点值
# # #用3次多项式拟合
# # z1=np.polyfit(x,y,3)
# # p1=np.poly1d(z1)
# # print(p1) #打印拟合的多项式
# # yvals=p1(x) #拟合后的y值
# # plot1=plt.plot(x,y,'r*',label='original values')
# # plot2=plt.plot(x,yvals,'b',label='polyfit values')
# # plt.xlabel('X ')
# # plt.ylabel('Y')
# # 'best'         : 0, (only implemented for axes legends)(自适应方式)
# # 'upper right'  : 1,
# # 'upper left'   : 2,
# # 'lower left'   : 3,
# # 'lower right'  : 4,
# # 'right'        : 5,
# # 'center left'  : 6,
# # 'center right' : 7,
# # 'lower center' : 8,
# # 'upper center' : 9,
# # 'center'       : 10,
# # zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\STSONG.TTF')
# # #font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
# # plt.legend(loc=3) #设置图示的位置
# # plt.title('拟合图像',fontproperties=zhfont1) #设置标题
# # plt.show() #显示图片
# # # plt.savefig('p1.png')
# # import numpy as np
# # import matplotlib.mlab as mlab
# # import matplotlib.pyplot as plt
# #
# #
# # mu, sigma , num_bins = 0, 1, 50
# # x = mu + sigma * np.random.randn(1000000)
# # # 正态分布的数据
# # n, bins, patches = plt.hist(x, num_bins, normed=True, facecolor = 'blue', alpha = 0.5)
# # # 拟合曲线
# # y = mlab.normpdf(bins, mu, sigma)
# # plt.plot(bins, y, 'r--')
# # plt.xlabel('期望')
# # plt.ylabel('概率')
# # plt.title('标准正态分布: $\mu = 0$, $\sigma=1$')
# #
# # plt.subplots_adjust(left = 0.15)
# # plt.show()
#
#
# # import numpy as np
# # import matplotlib.pyplot as plt
# # #初始化数据
# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# # y = [4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60]
# #
# # z1=np.polyfit(x,y,3)#利用函数计算系数
# # p1=np.poly1d(z1)#利用函数得到多项式
# # print(p1) #打印拟合的多项式
# # yvals = p1(x) #拟合后的y值
# # print(yvals)
# #
# # plt.figure()
# # plt.scatter(x[:],y[:],25,'red',label='original values')
# # plt.plot(x,yvals,abel='polyfit values',color="blue",linewidth=2)
# # plt.xlabel('X')
# # plt.ylabel('Y')
#
# # import numpy as np
# # import matplotlib.pyplot as plt
# # x=np.linspace(0,7,1000)
# # y = np.power(x-3,2) + 5
# # plt.figure(figsize=(8,4))
# # plt.plot(x,y,label="$cos(x)$",color="red",linewidth=2)
# # x1=3
# # y1 = np.power(x1-3,2) + 5
# # plt.scatter(x1, y1,  alpha=0.5, marker=(9, 3, 30))
# # plt.annotate(r'$\minvalue=5$',xy=(x1,y1),xycoords='data',xytext=(+10,+30),
# #              textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
# # # plt.plot(x,z,'b--',label="$cos(x^2)$")
# # plt.xlabel("X")
# # plt.ylabel("Y")
# # plt.title("y = (x-3)^2 + 5")
# # plt.legend()
# # plt.show()
#
#
# # import numpy as np
# # import matplotlib.pyplot as plt
# # x=np.linspace(0,10,1000)
# # y=np.cos(x)
# # plt.figure(figsize=(8,4))
# # plt.plot(x,y,label="$cos(x)$",color="red",linewidth=2)
# # x1=2*np.pi/3
# # y1=np.cos(x1)
# # plt.scatter(x1, y1,  alpha=0.5, marker=(9, 3, 30))
# # plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',xy=(x1,y1),xycoords='data',xytext=(+10,+30),
# #              textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
# # # # plt.plot(x,z,'b--',label="$cos(x^2)$")
# # plt.xlabel("X")
# # plt.ylabel("Y")
# # plt.title("y=cos(x)")
# # # plt.legend()
# # # plt.show()
#
#
# # import numpy as np
# # from pylab import *
# #
# # figure(figsize=(8,6),dpi=80)
# # subplot(1,1,1)
# # X=np.linspace(-np.pi,np.pi)
# #
# #
# # t=2*np.pi/3
# # plot([t,t],[0,np.cos(t)],color='blue',linewith=2.5,linstyle="--")
# # scatter([t
# # ,][np.cos(t),],50,color='blue')
# # legend(loc='upper left')
#
#
# #
# #
# # import numpy.random as random
# #
# # tests = 10000 # 设置试验次数10000次
# # # 生成每次实验中的奖品所在的门的编号
# # # 1表示第一扇门，2表示第二扇门，3表示第三扇门
# # winning_doors = random.randint(1, 4, tests)
# #
# # change_mind_wins = 0 # 记录更换门后的中奖次数
# # insist_wins = 0  # 记录坚持选择的中奖次数
# # for winning_door in winning_doors: # winning_door就是获胜门的编号
# # first_try = random.randint(1, 4) # 假设嘉宾随机挑了一扇门
# # remaining_choices = [i for i in range(1,4) if i != first_try] # 其他门的编号
# # # 没有奖品的门的编号，这个信息只有主持人知道
# # wrong_choices = [i for i in range(1,4) if i != winning_door]
# #
# # # 一开始选择的门主持人没法打开，所以从主持人可以打开的门中剔除
# # if first_try in wrong_choices:
# # wrong_choices.remove(first_try)
# #
# # # 这时wrong_choices变量就是主持人可以打开的门的编号
# # # 注意此时如果一开始选择正确，则可以打开的门是两扇，主持人随便开一扇门
# # # 如果一开始选到了空门，则主持人只能打开剩下一扇空门
# #
# # screened_out = random.choice(wrong_choices)
# # remaining_choices.remove(screened_out)
# #
# # # 现在除了一开始选择的编号，和主持人帮助剔除的错误编号，只剩下一扇门
# # # 如果要改变注意则这扇门就是最终的选择
# #
# # changed_mind_try = remaining_choices[0]
# #
# # # 结果揭晓，记录下来
# # if changed_mind_try == winning_door:
# # change_mind_wins += 1
# # if first_try == winning_door:
# # insist_wins += 1
# #
# # # 输出10000次测试的最终结果
# # print(
# # '如果改变主意的话，{0}次实验猜中的次数为：{1}次，此时频率为：{3}\n'
# # '如果不改变主意，{0}次实验猜中的次数为：{2}次，此时频率为：{4}'.format(
# # tests, change_mind_wins, insist_wins,change_mind_wins/tests,insist_wins/tests)
# # )
#
#
