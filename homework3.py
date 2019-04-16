#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author:sunwei
# date:2017-9-20 1:48
# 完成    程序：购物车程序
# （商品信息已经建立好    —>  下一页）
# 需求:
# 	1.启动程序后，让用户输入工资，然后打印商品列表
# 	2.允许用户根据商品编号购买商品
# 	3.用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 	4.可随时退出，退出时，打印已购买商品和余额（选做）
#
# 3.商品信息：
# product_list=[("T_shirt",90),
#                          ("dress",100),
#                          ("hat",30)]
#
# user_buy = []      #用户购买的商品

import time
import os
from prettytable import PrettyTable

shopping_list = []
username_password = []
product_info = [
    ("T_shirt", 90),
    ("dress",100),
    ("hat",30)
]


# 提示欢迎语
def welcome():
    print("欢迎%s登陆购物系统..." % username)
    time.sleep(2)
    os.system("clear")


# 输入为空格时循环输入
def get_salary():
    while True:
        salary = input("请输入您的工资：").strip()
        if len(salary) == 0:
            continue
        else:
            break
    return salary


# def first_shopping_system(salary,username,password)

def shopping_system(salary, password, username, product_info, xiaofei_history, file7):
    # 打印商品列表,用户输入商品编号,并检测余额是否足够
    while True:
        x = PrettyTable(["商品编号", "商品名称", "价格"])
        x.align["商品编号"] = 1
        x.padding_width = 1
        print("\033[31;40m")
        # print("以下为商品信息".center(50,"-"))
        for index, i in enumerate(product_info):
            x.add_row([index, i[0], i[1]])
        print("商品列表如下".center(40, "-"))
        print(x, "\033[0m")
        product_num = input("请输入需要购买的商品(输入商品编号即可,q退出)：").strip()
        if len(product_num) == 0:
            continue
        elif product_num == "q":
            count_info = open("db.txt.bak", "a+", encoding="utf-8")
            for line in file7:
                if line.startswith(username):
                    line1 = line.strip().split()
                    line2 = line.replace(line1[2], str(salary))
                    count_info.write(line2)
                else:
                    count_info.write(line)
            count_info.close()
            os.remove("db.txt")
            os.rename("db.txt.bak", "db.txt")
            print("")
            print("\033[31;40m您的余额为：%d\033[0m" % int(salary))
            print("\033[31;40m您本次消费情况如下：\033[0m")
            user_record = open(xiaofei_history, "a+", encoding="utf-8")
            for s1 in shopping_list:
                print(s1)
                user_record.write(s1[0] + " " + str(s1[1]) + "\n")
            user_record.close()
            exit()
        else:
            # 判断用户输入是否为数字字符
            if product_num.isdigit():
                product_num = int(product_num)
                if product_num < len(product_info):
                    p_price = product_info[product_num][1]
                    salary = int(salary)
                    if p_price <= salary:
                        salary -= p_price
                        shopping_list.append(product_info[product_num])
                        print("您的余额：%d" % salary)
                        # 是否还要继续购买
                        print(shopping_list)
                    else:
                        print("您的余额：%d" % salary)
                        print("余额不足,请重新选择商品！")
                else:
                    print("商品不存在！！！")
            else:
                print("输入有误,请重试")


# 判断用户名和密码是否为首次登陆
file1 = open("db.txt", "r", encoding="utf-8")
file7 = open("db.txt", "r", encoding="utf-8")
file8 = open("db.txt", "a+", encoding="utf-8")

# find_status = False
password_times = 0
# username_times = 0
while True:
    username = input("请输入用户名：").strip()
    if len(username) == 0: continue
    for line in file1:
        if line:
            li = line
            line = line.strip().split()
            if username != line[0]:
                continue
            elif username == line[0]:
                while True:
                    if password_times < 3:
                        password = input("请输入密码：").strip()
                        if len(password) == 0: continue
                        if password != line[1]:
                            password_times += 1
                            continue
                        elif password == line[1]:
                            print("输入成功！！！")
                            welcome()
                            salary = line[2]
                            print("\033[31;40m账户余额：%s\033[0m" % salary)
                            print("\033[1;34;40m以下为消费历史清单\033[0m".center(30, "-"))
                            xiaofei_history = username + ".record"
                            file2 = open(xiaofei_history, "r", encoding="utf-8")
                            for i in file2:
                                print(i.strip())
                            file2.close()
                            shopping_system(salary, password, username, product_info, xiaofei_history, file7)
                            exit()
                    else:
                        print("密码输入错误3次，请重新登陆！！！")
                        exit()
    else:
        print("此用户为首次登陆！！！")
        while True:
            password = input("为账户设置密码（不能为空）：").strip()
            if len(password) == 0: continue
            salary = get_salary()
            while True:
                x = PrettyTable(["商品编号", "商品名称", "价格"])
                x.align["商品编号"] = 1
                x.padding_width = 1
                print("\033[31;40m")
                print("以下为商品信息".center(50, "-"))
                for index, i in enumerate(product_info):
                    x.add_row([index, i[0], i[1]])
                print(x, "\033[0m")
                product_num = input("请输入需要购买的商品(输入商品编号即可,q退出)：").strip()
                if len(product_num) == 0:
                    continue
                elif product_num == "q":
                    file1.close()
                    file7.close()
                    file8.close()
                    file9 = open("first_db.txt", "w+", encoding="utf-8")
                    file10 = open("db.txt", "r", encoding="utf-8")
                    # file9.write(username+" "+password+" "+str(salary))

                    for line in file10:
                        if line:
                            file9.write(line)
                        else:
                            continue
                    file9.write(username + " " + password + " " + str(salary) + "\n")
                    file9.close()
                    file10.close()
                    os.remove("db.txt")
                    os.rename("first_db.txt", "db.txt")
                    xiaofei_history = username + ".record"
                    print("")
                    print("\033[31;40m您的余额为：%d\033[0m" % int(salary))
                    print("\033[31;40m您本次消费情况如下：\033[0m")
                    user_record = open(xiaofei_history, "a+", encoding="utf-8")
                    for s1 in shopping_list:
                        print(s1)
                        user_record.write(s1[0] + " " + str(s1[1]) + "\n")
                    user_record.close()
                    exit()

                else:
                    if product_num.isdigit():
                        product_num = int(product_num)
                        if product_num < len(product_info):
                            p_price = product_info[product_num][1]
                            salary = int(salary)
                            if p_price <= salary:
                                salary -= p_price
                                shopping_list.append(product_info[product_num])
                                print("您的余额：%d" % salary)
                                # 是否还要继续购买
                                print(shopping_list)
                            else:
                                print("您的余额：%d" % salary)
                                print("余额不足,请重新选择商品！")
                        else:
                            print("商品不存在！！！")
                    else:
                        print("输入有误,请重试")

#shopping.py