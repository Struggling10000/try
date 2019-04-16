import string
'''
题目：有这么一串字符串 str = “my Name is alex”想要将每一个单词首字母大写,其他不变str = “My Name Is Alex”
'''
s = 'my Name is alex.'
print('原字符串：s='+s)
print('直接调用函数结果：'+string.capwords(s))
s1=s.split(' ')
print('切分后的字符串列表是：')
print(s1)
def normallize(name):
	return name.capitalize()
s2=list(map(normallize,s1))
print('处理后的列表是：')
print(s2)
a=' '
print('应用第二种方法的结果：'+ a.join(s2))




