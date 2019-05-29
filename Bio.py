#!/usr/bin/python
# -*- coding: utf-8 -*-
#"思路整理：利用递归解析字符串，利用海龟绘图体系绘制结构"
#'''
# 改进点：
#        三角形的特殊情况未处理
#
#        没有异常处理
#        枝条有重叠
# '''

import numpy as np
import turtle as t
import math

# def yellow():
#     color = (1,1,0)
#     return color
# def red():
#     color = (1,0,0)
#     return color
# def blue():
#     color = (0, 0, 1)
#     return color
# def green():
#     color = (1,1,0)
#     return color
# def purple():
#     color = (1,0,1)
#     return color
sita=math.atan(2)
def type_1(size=20):#圆形
    t.pendown()
    t.begin_fill()
    t.fillcolor((1,1,0))
    t.circle(size/2)
    t.end_fill()
    t.penup()
    t.left(90)
    t.fd(size)
    t.right(90)

def type_2(size=20):#正方形
    t.pendown()
    t.begin_fill()
    t.fillcolor(0, 0, 1)
    t.fd(size/2)
    i = 1
    while i <= 3:
        t.left(90)
        t.forward(size)
        i = i + 1
    t.left(90)
    t.fd(size/2)
    t.end_fill()
    t.penup()
    t.left(90)
    t.fd(size)
    t.right(90)

def type_3(size=20):
    t.pendown()
    t.begin_fill()
    t.fillcolor(1, 0, 1)
    t.left(45)
    t.fd(size/2 *2**0.5)
    i=1
    for i in range(3):
        t.left(90)
        t.fd(size/2 * 2 ** 0.5)
    t.left(135)
    t.end_fill()
    t.penup()
    t.fd(size)
    t.right(90)
def type_4(size=20):#白色菱形
    t.pendown()
    t.left(45)
    t.fd(size/2  * 2 ** 0.5)
    i = 1
    for i in range(3):
        t.left(90)
        t.fd(size/2 * 2 ** 0.5)
    t.left(135)
    t.penup()
    t.fd(size)
    t.right(90)

def type_5(size=20):#红色三角
    t.pendown()
    t.begin_fill()
    t.fillcolor(1, 0, 0)
    t.left(30)
    for i in range(3):
        t.fd(size)
        t.right(120)
    t.right(30)
    t.end_fill()
    t.penup()

def begin_draw():
    t.setup(800, 800, 200, 200)
    t.pensize(1)
    t.penup()
    t.speed(10000)
    t.hideturtle()


def end_draw(ogly_str):
    #save pic [, font=("font-name", font_size, "font_type")
    ##保存图片
    #t.hideturtle()
    #ts = t.getscreen()
    #ts.getcanvas().postscript(file=ogly_str+".eps")

    #t.write(ogly_str)
    t.done()
def find_loc(str,c):
    count = 0
    strloc=[]
    for echar in str:
        count=count+1
        if echar == c:
            strloc.append(count-1)
    return strloc
def draw_type(c):
    for case in c:
        if case=='1':
            type_1()
            break
        if case=='2':
            type_2()
            break
        if case=='3':
            type_3()
            break
        if case=='4':
            type_4()
            break
        if case=='5':
            type_5()
            break
        if case=='':  # default
            print('no type!')

def painting_brance(brance_num,nobr,size=20,special=0):
    #功能：绘制好枝干，并放置好turtle的位置
    if nobr==-1 : ##特殊情况
        t.right(45)
        t.fd(size/2*2**0.5)
        t.left(45)
        t.pendown()
        t.fd(size)
        t.penup()
    elif nobr==-2 :
        t.right(135)
        t.fd(size/2*2**0.5)
        t.right(45)
        t.pendown()
        t.fd(size)
        t.penup()
    if brance_num==1 :
        if nobr==1:
            t.pendown()
            t.left(90)
            t.fd(size)
            t.right(90)
            t.penup()
    if brance_num==2:
        if nobr==1 and special==0:
            t.pendown()
            t.left(150)
            t.fd(size * 3 ** 0.5)
            t.right(150)
            t.penup()
        if nobr==2 and special==0:
            t.pendown()
            t.left(30)
            #t.left(sita)
            t.fd(size * 3 ** 0.5)
            t.right(30)
            #t.right(sita)
            t.penup()
        if nobr == 1 and special == 1:
            t.pendown()
            t.left(160)
            t.fd(size*1.5* 3 ** 0.5)
            t.right(160)
            t.penup()
        if nobr == 2 and special == 1:
            t.pendown()
            #t.left(30)
            t.left(20)
            t.fd(size *1.5* 3 ** 0.5)
            #t.right(30)
            t.right(20)
            t.penup()
    if brance_num==3 :
        if nobr==1 and special==0:
            t.pendown()
            t.left(150)
            t.fd(2*size)
            t.right(150)
            t.penup()
        if nobr==2 and special==0:
            t.pendown()
            t.left(90)
            t.fd(size)
            t.right(90)
            t.penup()
        if nobr==3 and special==0:
            t.pendown()
            t.left(30)
            t.fd(2*size)
            t.right(30)
            t.penup()


def anay_structofgly(ogly_str,list,turtleloc):
    if len(ogly_str)==0 and len(list)==0:
        print('--------------------------------------')
        print('当前栈中存储的是：',end="")
        print(list)
        print('当前解析的结点是：',end="")
        print(ogly_str)
        return 0
    elif len(ogly_str)==3 and len(list)==0:#最后一个的话，直接绘制
        print('--------------------------------------')
        print('当前栈中存储的是：',end="")
        print(list)
        print('当前解析的结点是：',end="")
        print(ogly_str)
        draw_type(ogly_str[1])
        return 0
    elif len(ogly_str)==0 and len(list)!=0:
        print('--------------------------------------')
        print('当前栈中存储的是：',end="")
        print(list)
        print('当前解析的结点是：',end="")
        print(ogly_str)
        t.goto(turtleloc.pop())
        temp_str = list.pop()
        return anay_structofgly(temp_str, list, turtleloc)
    elif len(ogly_str)==3 and len(list)!=0:
        #print(ogly_str[0] + 'end')
        print('--------------------------------------')
        print('当前栈中存储的是：',end="")
        print(list)
        print('当前解析的结点是：',end="")
        print(ogly_str)
        draw_type(ogly_str[1])  # 先绘制糖，在绘制枝条
        t.goto(turtleloc.pop())
        temp_str=list.pop()
        return anay_structofgly(temp_str,list,turtleloc)

    elif ogly_str.count(ogly_str[0]) == 1 and ogly_str[0]==ogly_str[len(ogly_str)-1].upper():
        """
        想法：先绘制糖，再看这个糖有没有右侧相连的类型5 在绘制下一层的枝条
        """
        print('--------------------------------------')
        print('当前栈中存储的是：',end="")
        print(list)
        print('当前解析的结点是：',end="")
        print(ogly_str)
        # print (ogly_str[0])
        # print(ogly_str[-1])
        draw_type(ogly_str[1])#先绘制糖，在绘制枝条
        tloc = t.pos()

        #num = ogly_str.count(ogly_str[2])
        Stang=ogly_str[2]+'5'+ogly_str[2].lower()
        branchcount=0
        for i in range(3):
            if Stang in ogly_str:
                #print("HAHAIHEIHEI~")
                branchcount=branchcount+1
                t.goto(tloc)
                painting_brance(1, -branchcount)
                draw_type('5')
                if branchcount==1:
                    t.left(90)
                    t.fd(10)
                    t.left(90)
                    t.fd(30)
                    t.right(180)
                    tloc = t.pos()
                elif branchcount==2:
                    t.left(90)
                    t.fd(10)
                    t.right(90)
                    t.fd(30)
                    t.right(180)
                    t.loc=t.pos()
                else :
                    print('这种情况罕见')
                index=ogly_str.index(Stang)
                ogly_str=ogly_str[0:index]+ogly_str[index+3:-1]+ogly_str[-1]
                #print(ogly_str)

            # if ogly_str[-3]=='5':
            #     print ("HAHAHA!")
            #     t.goto(tloc)
            #     painting_brance(1, -1)
            #     draw_type('5')
            #     t.left(90)
            #     t.fd(10)
            #     t.left(90)
            #     t.fd(30)
            #     t.right(180)
            #     tloc=t.pos()
            #     ogly_str=ogly_str[0:-4]+ogly_str[-1]

        if len(ogly_str)>4:
            num =ogly_str.count(ogly_str[2])

            special=0
            glynum=0
            for str in ogly_str:
                if str.isdigit():
                    glynum=glynum+1
            if glynum>10:
                special=1


            for i in range(num,0,-1):
                t.goto(tloc)
                painting_brance(num, i,20,special)
                if i>1:
                    turtleloc.append(t.pos())
                elif i==1:
                    pass

        #记录位置
        ogly_str1 = ogly_str[2:-1]
        return anay_structofgly(ogly_str1,list,turtleloc)
    elif ogly_str.count(ogly_str[0])==2 and ogly_str[0]==ogly_str[len(ogly_str)-1].upper():
        """
        本层有两个，将这两个绘制出来，并对它的下一层递归
        """
        print('--------------------------------------')
        print('当前栈中存储的是：',end="")
        print(list)
        print('当前解析的结点是：',end="")
        print(ogly_str)
        #找到两个字符串的位置
        loc2= find_loc(ogly_str, ogly_str[0])
        #print(ogly_str[0],loc2[0])
        #print(loc2)
        #绘制分叉的两个
       # print(ogly_str[loc2[1]],loc2[1])
        draw_type(ogly_str[1])
        tloc=t.pos()
       # paiting_brance(2, 1)
       # paiting_brance(2, 2)
       # 记录结束的地方
        ogly_str1 = ogly_str[2:loc2[1] - 1]
        Stang = ogly_str[2] + '5' + ogly_str1[2].lower()
        branchcount = 0
        for i in range(3):
            if Stang in ogly_str1:
                #print("HAHAIHEIHEI~")
                branchcount = branchcount + 1
                t.goto(tloc)
                painting_brance(1, -branchcount)
                draw_type('5')
                if branchcount == 1:
                    t.left(90)
                    t.fd(10)
                    t.left(90)
                    t.fd(30)
                    t.right(180)
                    tloc = t.pos()
                elif branchcount == 2:
                    t.left(90)
                    t.fd(10)
                    t.right(90)
                    t.fd(30)
                    t.right(180)
                    t.loc = t.pos()
                else:
                    print('这种情况罕见')
                index = ogly_str.index(Stang)
                ogly_str = ogly_str[0:index] + ogly_str[index + 3:-1] + ogly_str[-1]
                #print(ogly_str)
        num = ogly_str1.count(ogly_str[2])
        # num = ogly_str1.count(ogly_str[2])
        #
        # for i in range(num):
        #     if ogly_str1[-3] == '5':
        #         print("HAHAHA!")
        #         t.goto(tloc)
        #         painting_brance(1, -1)
        #         draw_type('5')
        #         t.left(90)
        #         t.fd(10)
        #         t.left(90)
        #         t.fd(30)
        #         t.right(180)
        #         tloc = t.pos()
        #         ogly_str1 = ogly_str1[0:-4]+ogly_str1[-1]

        # glynum=ogly_str1.isdigit()
        '''
        若整体比较多的画，画宽一点。
        '''
        # digitnum=0
        # for str in ogly_str:
        #     if str.isdigit():
        #         digitnum=digitnum+1
        # if digitnum>11:
        #     for i in range(num, 0, -1):
        #         t.goto(tloc)
        #         painting_brance(num, i,20,1)
        #         if i > 1:
        #             turtleloc.append(t.pos())
        #         elif i == 1:
        #             pass
        #
        # else :
        for i in range(num, 0, -1):
            t.goto(tloc)
            painting_brance(num, i)
            if i > 1:
                turtleloc.append(t.pos())
            elif i == 1:
                pass
        ogly_str2 = ogly_str[loc2[1]:]
        #print(ogly_str2)
        if len(ogly_str2)>0:
            list.append(ogly_str2)
        #print(list)
        return anay_structofgly(ogly_str1,list,turtleloc)
    elif ogly_str.count(ogly_str[0])==3 and ogly_str[0]==ogly_str[len(ogly_str)-1].upper():
        '''
        本层是三个分支的情况
        '''
        print('--------------------------------------')
        print('当前栈中存储的是：', end="")
        print(list)
        print('当前解析的结点是：', end="")
        print(ogly_str)
        loc3= find_loc(ogly_str, ogly_str[0])
        #print(ogly_str[0],loc3[0])
       # print(ogly_str[loc3[0]-1],loc3[1])
       # print(ogly_str[ogly_str[1]-1],loc3[2])
        ogly_str1 = ogly_str[2:loc3[1] - 1]
        ogly_str2 = ogly_str[loc3[1]:loc3[2]]
        ogly_str3 = ogly_str[loc3[2]:]

        draw_type(ogly_str[1])
        tloc = t.pos()

        Stang = ogly_str[2] + '5' + ogly_str1[2].lower()
        branchcount = 0

        for i in range(3):
            if Stang in ogly_str1:
                #print("HAHAIHEIHEI~")
                branchcount = branchcount + 1
                t.goto(tloc)
                painting_brance(1, -branchcount)
                draw_type('5')
                if branchcount == 1:
                    t.left(90)
                    t.fd(10)
                    t.left(90)
                    t.fd(30)
                    t.right(180)
                    tloc = t.pos()
                elif branchcount == 2:
                    t.left(90)
                    t.fd(10)
                    t.right(90)
                    t.fd(30)
                    t.right(180)
                    t.loc = t.pos()
                else:
                    print('这种情况罕见')
                index = ogly_str.index(Stang)
                ogly_str = ogly_str[0:index] + ogly_str[index + 3:-1] + ogly_str[-1]
                print(ogly_str)

        num = ogly_str1.count(ogly_str[2])
        # for i in range(num):
        #     if ogly_str1[-3] =='5':
        #         print("HAHAHA!")
        #         t.goto(tloc)
        #         painting_brance(1, -1)
        #         draw_type('5')
        #         t.left(90)
        #         t.fd(10)
        #         t.left(90)
        #         t.fd(30)
        #         t.right(180)
        #         tloc = t.pos()
        #         ogly_str1 = ogly_str1[0:-4]+ogly_str1[-1]
        for i in range(num, 0, -1):
            t.goto(tloc)
            painting_brance(num, i)
            if i > 1:
                turtleloc.append(t.pos())
            elif i == 1:
                pass
        list.append(ogly_str3)
        list.append(ogly_str2)
        return anay_structofgly(ogly_str1,list,turtleloc)


def test(ogly_str):
    list = []
    turtleloc = []
    begin_draw()
    # type_5()
    # type_1()
    # painting_brance(1, -1)
    # type_5()
    # type_3()
    # type_4()
    # type_2()
    anay_structofgly(ogly_str, list, turtleloc)
    end_draw(ogly_str)
    print('--------------------------------------')
    print('end')
    #t.reset()




if __name__ == "__main__":

     #str='A2B2C1D1E2F2fedD1dcba'
     #str='A2B2C1D1E2eE2eE2edD1dcba'
     #str=''
     #list=['A2B2C1D1E2F1G3gfF3fedD2dD1E2eE2eE5edcba','D1E2eE2eE5ed']
     #str = ''
     #str='A2B2C1D1E2F1G5gfF5fF5fedD1E2F1feE2F1G5gfF5fedcbB5bB5ba'
     #str='A2B2C1D1E2F1G5gfF5fedD1E2F1fedcbB5ba'
     str='A2B2C1D1E2F1G5gfF5fF5fedD1E2F1fF5fedcbB5ba'
     #str='A2B2C1D1E2F1G3gfF5fedD1E2F1fF5fedcbB5ba'
     # for i in range(len(list)):
     #      #    test(list[i])
     test(str)
     #


















