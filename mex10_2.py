# 本代码实现的是通过用户输入1个或多个文件路径，或不输入文件路径改为手动输入要sort的内容，来实现对所有内容进行统一重新排序的功能
# 注意：本代码实现的是对所有文件的内容或手动输入的内容进行统一重新排序，而不是对文件夹中的文件进行排序！
# 注：下面的 file_name 所表示的实际上是文件的相对或绝对路径，如 './mex10_related/test.txt', 'test.txt', 'C:\\Users\\roy\\projects\\moreZed\\mex10_related\\test.txt', 'mex10_related\test.txt'

import sys

lines = []

if len(sys.argv) > 1:                 # 第一种情况：当用户传入命令行参数（即用户输入1个或多个文件路径）时
    for file_name in sys.argv[1:]:
        lines += [line for line in open(file_name).readlines() if len(line) > 20] # 列表推导式 list comprehension，根据用户给出的文件路径打开文件，取len大于20的每行组成一个新list（即line），并追加到当前的list中（即lines = lines + line）
        #当需要单独sort每一个文件（而不是sort所有文件）时，可用如下这两行，替换上面这行以及最下面的print语句那一行
        #output = "".join(sorted(line for line in open(file_name).readlines())) 
        #print(output)
         
else:                                 # 第二种情况：当用户不传入命令行参数（即用户不输入文件路径）时
    while True:                       # 由用户手动输入要sort的内容，并通过 while 循环追加到空的list（即lines）中，最后使用 Ctrl+Z 跳出循环
        try:
            line = input() + '\n'     # '\n'的作用是给每次input的内容的末尾加上一个回车，然后才追加到list中，不然打印出来时所有内容就在一行上了（与readlines读文件的方式不同，通过input手动输入的方式，每行不会包含末尾的回车）
            lines.append(line)
        except EOFError:
            break

print("".join(sorted(lines)), end="") # 最终，无论是第一或第二种情况，都通过sorted（）方式进行排序打印




# += is an assignment（赋值符号，如 = ）
# 注：We can't put an assignment inside a function call. e.g. lines.append(line += '\n')  --> Wrong!

# readlines() 方法：
# 用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。 如果碰到结束符 EOF 则返回空字符串。如果碰到结束符 EOF 则返回空字符串。
# fileObject.readlines( )
# 参数: 无。
# 返回值: 返回列表，包含所有的行。每一行是列表的一个元素。
# http://www.runoob.com/python3/python3-file-readlines.html

# 手动触发EOFError:
# 在windows平台下，一般模拟eof的输入是在一个新行的开头输入 ctrl+z 就行了；
# 在unix环境下，是在一个新行的开始出输入 ctrl+D 就可以了！

# Python join() 方法用于将可迭代对象中的元素sequence，以指定的字符str连接，生成一个新的字符串。
# 语法：str.join(sequence)
# 参数: sequence -- 要连接的可迭代对象。
# 返回值: 返回通过指定字符连接可迭代对象中的元素后，生成的新字符串。
# join() 方法的确是程序中字符串与可迭代对象（如列表等）相互转换的很好用的工具（输入可迭代对象，输出由可迭代对象的元素所组成的一个新的字符串）
# https://www.runoob.com/python3/python3-string-join.html

# sorted 语法：
# sorted(iterable, key=None, reverse=False)  
# 参数说明：
# iterable -- 可迭代对象。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
# 返回值：返回重新排序的列表。
# sort 与 sorted 区别：sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作，
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
# https://www.runoob.com/python3/python3-func-sorted.html