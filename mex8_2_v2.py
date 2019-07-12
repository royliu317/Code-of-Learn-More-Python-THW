# Zed的这段代码，使用了Python的generator（生成器），更详细信息可参见下方链接及mex8_3_more info_2(more info)

import sys

_, delim, fields = sys.argv  # 运行本代码时，必须同时附带命令行参数（delim-以何符号分隔句子如空格, fields-选取分隔后的哪个index输出）。 fields type: str（eg. 2）
split_at = [int(x) for x in fields.split(',')] # # split_at type: list（eg. [2]）

def lines_of_input():
    try:
        while True:
            yield input() # 带有yield的函数在Python中被称为 generator（生成器）。在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值, 并在下一次执行next()方法时从当前位置继续运行
    except KeyboardInterrupt:
            return        # List类型在函数运行中占用的内存大，如果需要控制内存占用，最好通过 iterable 迭代器对象来进行迭代（在每次迭代中返回下一个数值，内存占用始终为常数）
            #raise StopIteration


try:                      # 设置异常捕获，以防因为设置了过大的fields值，造成跳出 IndexError: list index out of range 异常的情况
    split_lines = (line.split(delim) for line in lines_of_input()) 
    print("1. split_lines: ", split_lines)

    cuts = (line[split_at[0]] for line in split_lines)
    print("2. cuts: ", cuts)

    #print(cut for cut in cuts)
    #Zed代码中的如上语句是错误的，不能用这种方式进行打印。需要使用如下 for循环方式 或 调用next()函数方式 对生成器cuts进行迭代打印

    for cut in cuts:
        print(cut)

    # 如上两行代码也可用如下代替，效果相同：
    #while True:
    #    try:
    #        print(next(cuts))
    #    except:
    #        sys.exit()

except IndexError:        # 异常捕获的位置，一定要设置正确。如果把IndexError这个捕获设置在上面的函数中，那么当出现“列表索引越界”时，则无法捕获该异常以防止其跳出
        pass




# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
# 虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
# 看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
# yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用 类的实例 保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。

# Python yield 使用浅析(注意：文中所用代码基于python2版本)：
# http://www.runoob.com/w3cnote/python-yield-used-analysis.html
# Python3 迭代器与生成器：
# http://www.runoob.com/python3/python3-iterator-generator.html

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。迭代器是一个 “可以记住遍历的位置” 的对象。
# range() 函数返回的是一个可迭代对象（generator object），而不是列表类型， 所以打印的时候不会打印列表。
# 在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。

# 不定长参数:
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# https://www.runoob.com/python3/python3-function.html

# Python join() 方法用于将可迭代对象中的元素sequence，以指定的字符str连接，生成一个新的字符串。
# 语法：str.join(sequence)
# 参数: sequence -- 要连接的可迭代对象。
# 返回值: 返回通过指定字符连接可迭代对象中的元素后，生成的新字符串。
# join() 方法的确是程序中字符串与可迭代对象（如列表等）相互转换的很好用的工具（输入可迭代对象，输出由可迭代对象的元素所组成的一个新的字符串）
# https://www.runoob.com/python3/python3-string-join.html