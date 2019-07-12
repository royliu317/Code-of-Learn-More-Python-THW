import os, sys

filelist = os.listdir(input())

# 对文件夹中的文件进行正向排序并打印：
for i in filelist:
    print(i)

# 对文件夹中的文件进行反向排序并打印：
for i in filelist[::-1]:
    print(i)


#---------------------------------------------------------------------------------
# 通过列表推导式，可生成一个新list（以 中括号 包起来时）。如果附加在原list中的element上的function是如print()等函数，
# 则新生成的list中只会有None元素（因为function只是通过推导式对原list中的element循环执行了一次print的动作，什么也没传到新list中）
# 推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层。

>>> import sys
>>> a = [1, 2, 3]
>>> [print(line) for line in a]
1
2
3
[None, None, None]
>>>
>>> a
[1, 2, 3]
>>>
>>> b = [print(line) for line in a]
a
c
b
>>>
>>> b
[None, None, None]
>>>
>>> b = [line+'d' for line in a]
>>> b
['ad', 'cd', 'bd']
>>>
>>> b = [print(line+'d') for line in a]
ad
cd
bd
>>> b
[None, None, None]
>>>
