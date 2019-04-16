# import numpy as np
# data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
# 'formats':('U10', 'i4', 'f8')})
# print(data.dtype)
import time
import os
product_list=[("T_shirt",90),
                ("dress",100),
                ("hat",30)
]
shopping_list=[]
salary=input("input your salary:")
if salary.isdigit():
    salary=int(salary)
    while True:
          for item in product_list:
              print(product_list.index(item),item)
          user_choice=input("which do you want to buy:(end shopping with 'a')")
          if user_choice.isdigit():
               user_choice=int(user_choice)
               if user_choice<len(product_list) and user_choice>=0:
                          p_item=product_list[user_choice]
                          if p_item[1]<=salary:
                               shopping_list.append(p_item)
                               salary-=p_item[1]
                               print("Added %s in shopping car,your current balance is %s"%(p_item,salary))
                          else:
                               print("Your current balance is not enough")
               else:
                    print("ERROR！The code is not exist")
          elif user_choice=='a':
               print("------shopping list------")
               for p in shopping_list:
                   print(p)
               print("Your current balance is",salary)
               exit()
          else:
               print("wrong input")