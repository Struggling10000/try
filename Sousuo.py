#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import numpy as np
import Tkinter as tk
# import math
# import xlwt
from datetime import date,datetime
def find_newstr(aimstr,l):
    newlist=[]
    for i in range(0,len(aimstr)-l):
        newlist.append(aimstr[i:i+l])
    newlist.append(aimstr[len(aimstr)-l:])
    return newlist

def calcu_sub_str_num(mom_str,sun_str):
  #print('打印母字符串：',mom_str)   #打印出母字符串
  #print( '打印子字符串：',sun_str)  #打印出子字符串
  #print('打印母字符串长度：',len(mom_str)) #打印出母字符串长度
  #print( '打印子字符串长度：',len(sun_str))  #打印出子字符串长度
  count = 0                                  #定义计数器初始值
  #使用循环遍历字符串，第一次循环，通过切片获取下标从0开始与子字符串长度一致的字符串，并与字符串比较，如果等于子字符串count+1
  #第二次循环，通过切片获取下标从1开始与子字符串长度一致的字符串，并与字符串比较，如果等于子字符串则count+1，以此类推直到遍历完成
  for i in range(len(mom_str)-1): #因为i的下标从0开始，所以len（mom_str）-1
      if mom_str[i:i+len(sun_str)] == sun_str:
          count+=1
  return count

def Rank(matix):
    row,col=matix.shape
    #print(matix)
    #print(row,col)
    scores=np.zeros((row,1))
    for i in range(row):
        for j in range(col):
            scores[i] = scores[i]+matix[i][j]*10**(col-j-1)
    #print(scores)
    return scores

    #data = data[data[:, 2].argsort()]
def takeSecond(elem):
    return elem[1]

def matching(aimstr, datastr):
    strlen=len(aimstr)
    datalen=len(datastr)
    arrrate=np.zeros((datalen ,strlen-int(len(aimstr)/2)))
    #print(arrrate[3][2])
    for i in range(strlen,int(len(aimstr)/2),-1):
        #print(int(len(aimstr)/2))
        #print(strlen,datalen,i)
        strseq=find_newstr(aimstr,i)
        #print(strseq)

        for j in range(datalen):
            # COUNT1=calcu_sub_str_num(datastr[j], 'TFT')
            # COUNT2=calcu_sub_str_num(datastr[j], 'FTF')
            # print(COUNT1+COUNT2)
            for temp_aim_str in strseq:
                #print(temp_aim_str)
                #count=calcu_sub_str_num(datastr[j],temp_aim_str)
                #print(j,strlen-i,count)
                arrrate[j][strlen-i]=arrrate[j][strlen-i] + calcu_sub_str_num(datastr[j],temp_aim_str)
                #print(arrrate[j][strlen-i])
    #print(arrrate)



    ##算分
    rank=Rank(arrrate)
    #data = datastr[rank[:].argsort()]
    #print(rank)

    ##逆序排列
    L=[]
    for i in range(datalen):
        #print(i,datalen)
        datatuple = [datastr[i],int(rank[i])]
        L.append(datatuple)
    #print(L)
    S=L
    S.sort(key=lambda ele:ele[1],reverse=True)
    #print(S)
    #Finaldata=np.array(S)
    #print(Finaldata)
    #print(S[2][0])
    #K=np.array(datalen,1)
    K=[]
    K_s=[]
    for i in range(datalen):
        #print(i)
        K.append(S[i][0])
    #print(K)
        if S[i][1]>0:
            K_s.append(S[i][0])
    if len(K_s)==0:
        K_s.append("No result！")
    return K,K_s
def read_xls(filename):
    # 打开文件
    workbook = xlrd.open_workbook(filename)
    # 获取所有sheet
    #print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    sheet1_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    # sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet1 = workbook.sheet_by_name('Sheet1')
    # sheet的名称，行数，列数S
    #print(sheet2.name, sheet2.nrows, sheet2.ncols)
    # 获取整行和整列的值（数组）
    #rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet1.col_values(0)
    #print(rows)
   # print(cols)
    return cols


    # 获取单元格内容
    # print(sheet2.cell(1, 0).value.encode('utf-8'))
    # print(sheet2.cell_value(1, 0).encode('utf-8'))
    # print(sheet2.row(1)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型
    #print(sheet2.cell(1, 0).ctype)
#def GUI():

def test():
   #aimstr='DFTNNASQ'
   aimstr='FTFT'
   alldata=read_xls('data.xlsx')
   #print(alldata)
   # print(len(aimstr))
   # print(aimstr[3:6])
   K,K_s=matching(aimstr,alldata)
   print(K)
   print(K_s)




if __name__ == "__main__":
    test()