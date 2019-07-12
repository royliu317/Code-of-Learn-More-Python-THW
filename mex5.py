import argparse

parser = argparse.ArgumentParser()  # 1.创建一个解析器：使用argparse的第1步是创建一个ArgumentParser对象，它会保存把命令行解析成Python数据类型所需要的所有信息。

parser.add_argument('files', metavar='F', type=str, nargs='+') # 2.添加参数：调用add_argument()方法向ArgumentParser添加程序的参数信息。通常情况下，
parser.add_argument('-n', '--numbers', action='store_true', help='Print line numbers') # 这些信息告诉ArgumentParser如何接收命令行上的字符串并将它们转换成对象。这些信息被保存下来并在调用parse_args()时用到。

args = parser.parse_args()          # 3.解析参数：ArgumentParser通过parse_args()方法解析参数。它将检查命令行，把每个参数转换成恰当的类型并采取恰当的动作。在大部分情况下，这意味着将从命令行中解析出来的属性建立一个简单的Namespace对象。在脚本中，parse_args()调用一般不带参数，ArgumentParser将根据sys.argv自动确定命令行参数。
print(">>> parsed args: ", args)

line_number = 1
for in_file_name in args.files:     # args对象的files属性是一个列表，所有命令行参数都会被收集到该列表中。如果没有至少出现一个命令行参数将会产生一个错误信息（因为设置了nargs='+'）
    in_file = open(in_file_name)
    if args.numbers:                # 当命令行中有-n这个参数时，args.numbers为True(因为设置了action=store_true)，继而会运行if中的语句；如果没有-n，则会直接运行else中的语句。
        #print(args.numbers)        
        for line in in_file.readlines():
            print(f"\t{line_number}\t {line}", end='')
            line_number += 1
        print()
    else:
        print(in_file.read())



# parse_args() 方法：
# ArgumentParser.parse_args(args=None, namespace=None)
# 将参数字符串转换成对象，并设置成命名空间namespace的属性。返回的是构成的命名空间。
# 之前对add_argument()的调用，完全决定了创建什么对象以及如何设置。详见如下add_argument()的介绍。
# 默认情况下，参数字符串取自于sys.argv，并创建一个空的Namespace对象用于保存属性。


# Namespace 对象：
# class argparse.Namespace
# parse_args() 默认使用的简单的类，用于创建一个保存属性的对象并返回该对象。
# 这个类故意设计得非常简单，只是object的一个可以打印可读字符串的子类。如果你喜欢以字典的形式查看其属性，可以使用Python标准的语句vars()：vars(args)
# 有时可能需要让ArgumentParser分配属性给一个已经存在的对象而不是一个新的Namespace对象。这可以通过指定namespace=关键字参数达到：


# add_argument() 方法：
# 定义应该如何解析一个命令行参数。下面每个参数有它们自己详细的描述，简单地讲它们是：
# name or flags - 选项字符串的名字或者列表，例如foo 或者-f, --foo。
# action - 在命令行遇到该参数时采取的基本动作类型。
# nargs - 应该读取的命令行参数数目。
# const - 某些action和nargs选项要求的常数值。
# default - 如果命令行中没有出现该参数时的默认值。
# type - 命令行参数应该被转换成的类型。
# choices - 参数可允许的值的一个容器。
# required - 该命令行选项是否可以省略（只针对可选参数）。
# help - 参数的简短描述。
# metavar - 参数在帮助信息中的名字。
# dest - 给parse_args()返回的对象要添加的属性名称。
# 对于add_argument() 方法，它必须知道期望的是可选参数，比如-f 或者--foo，还是位置参数，比如一个文件列表。因此，传递给add_argument() 的第一个参数必须是一个标记序列或者一个简单的参数名字。
# 当调用parse_args()时，可选的参数将以- 前缀标识，剩余的参数将被假定为位置参数。


# enumerate() 函数：
# 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# enumerate(sequence, [start=0])
# 参数: sequence -- 一个序列、迭代器或其他支持迭代对象。start -- 下标起始位置。
# 返回值: 返回 enumerate(枚举) 对象。
# http://www.runoob.com/python3/python3-func-enumerate.html


# readlines() 方法：
# 用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。 如果碰到结束符 EOF 则返回空字符串。如果碰到结束符 EOF 则返回空字符串。
# fileObject.readlines( )
# 参数: 无。
# 返回值: 返回列表，包含所有的行。每一行是列表的一个元素。
# http://www.runoob.com/python3/python3-file-readlines.html


# argparse — 命令行选项、参数和子命令的解析器: https://www.cnblogs.com/xiaofeiIDO/p/6154953.html
# Zed's Answer: https://github.com/zedshaw/learn-more-python-the-hard-way-solutions/blob/master/ex05_cat/cat.py