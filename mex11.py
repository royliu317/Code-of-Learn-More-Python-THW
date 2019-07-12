#!/usr/bin/env python3.6                              # 该注释是用于Unix/Linux操作系统的

import sys

def print_uniq_lines(file_list):
    print('file_list: ', file_list, type(file_list))
    all_lines = set()
    #print('file_list: ', file_list, type(file_list)) # file_list 是由元组推导式生成的生成器generator  

    for f in file_list:                               # 通过for循环，遍历生成器对象file_list(生成器是可迭代的对象)，对其内元素f（每个f均是由open函数所生成的文件对象类型'_io.TextIOWrapper')，
        all_lines |= set(f.readlines())               # 进行readlines操作，并依次追加到all_lines集合中，利用集合类型的去重特性，实现所有文件中的所有行均为unique的要求
                
    print("".join(all_lines))
# Zed如上代码，与mex9_2_tools中他最后额外加的函数print_uniq_lines()内容完全相同。简单来说就是利用集合类型Set Type的特点（无重复元素）实现本例的unique需求


if len(sys.argv) > 1:
    print_uniq_lines(open(f) for f in sys.argv[1:]) # 使用元组推导式，在完成全部遍历后，生成一个生成器，然后将其返回给print_uniq_lines函数（即在本程序中，该函数只会被调用1次）
else:
    print_uniq_lines([sys.stdin])                   # stdin, stdout, stderr在Python中都是文件属性的对象 - These streams are regular text files like those returned by open().
    #print_uniq_lines([input()])                    # 将sys.stdin放在list中，生成一个由文件对象组成的列表，是为了便于print_uniq_lines()函数使用for循环读取file_list中的元素
    #上行代码不work，因为input()函数的返回值是(单行)字符串，而字符串并不支持readlines方法（可见f变量必须是文件对象，这就是使用sys.stdin而非input的原因）


# 集合(set): 
# 集合类型（Set Type）是一个 无序不重复 元素序列。可以使用大括号 { } 或者 set() 函数创建集合类型
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# 类似列表推导式，同样集合支持集合推导式(Set comprehension)
# https://www.runoob.com/python3/python3-set.html
# 集合是一个无序不重复元素的集。基本功能包括 关系测试 和 消除重复元素

# 函数 set():
# 它用于创建一个 无序不重复 元素集合(即调用它创建set类型的数据)，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
# 语法: set([iterable])
# 参数说明：iterable -- 可迭代对象（与列表等不同，不支持通过一次性指定多个字符串对集合元素进行赋值的方式）
# 返回值: 返回新的集合对象
# https://www.runoob.com/python/python-func-set.html

# sys.stdin, sys.stdout, sys.stderr：
# https://docs.python.org/3/library/sys.html?highlight=stdin#sys.stdin

# 集合类型（Set Type）：
# 其update(*others)函数， 等价于 set |= other | ...
# Update the set, adding elements from all others.

# sys.argv
# The list of command line arguments passed to a Python script. sys.argv[0] is the script name. 
# If no script name was passed to the Python interpreter, argv[0] is the empty string.
# https://docs.python.org/3/library/sys.html?highlight=sys%20argv#sys.argv

# 命令行参数 - 通用工具脚本经常调用命令行参数。这些命令行参数以 链表形式 存储于 sys 模块的 argv 变量。
# 例如在命令行cmd中执行 "python demo.py one two three" 后可以得到以下输出结果:
# import sys
# print(sys.argv)
# --> ['demo.py', 'one', 'two', 'three']

# Python3 解释器 - 交互式编程，脚本式编程
# https://www.runoob.com/python3/python3-interpreter.html