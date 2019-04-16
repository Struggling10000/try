#新建两个文件 account.txt和account_lock.txt ，在account中输入用户名密码 aaa 123root
# Author:oliver
#1.输入用户名密码 2.认证成功后显示登录信息 3.输入错误三次之后退出 用户名：       密码：123456（使用交互方式）

import sys,os
count = 0
name_list = []
while count < 3:
    name = input("请输入用户名：")
    user_file = open('account.txt','r')
    user_list = user_file.readlines()
    for user_line in user_list:
        (user,password) = user_line.strip('\n').split()
        name_list.append(user_line)
        if name == user:
            i = 0
            while i < 3:
                passwd = input('请输入密码：')
                if passwd == password:
                    print('欢迎 %s 登录' % name)
                    print("----系统账户信息----\n", user_list)
                    sys.exit(0)
                else:
                    if i < 2:
                        print('用户 %s 密码错误，请重新输入，还有 %d 次机会.' % (name,2 - i))
                    # elif i==3:
                    #     sys.exit('用户 %s 密码错误，退出' % name)

                i += 1
        else:
            pass
    else:
        if count < 2:
            print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (name,2 - count))
    count += 1
else:
    sys.exit('用户 %s 不存在，退出' % name)

lock_file.close()
user_file.close()