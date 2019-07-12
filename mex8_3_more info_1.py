# 创建一个类，将其作为迭代器使用

import sys

class Fab():    # 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
 
    def __init__(self, max):   # 构造函数 __init__(), 会在对象初始化的时候执行。对于实例方法，self在定义时不可省略
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 
 
    def __iter__(self):        # __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了__next__()方法并通过 StopIteration异常 标识迭代的完成
        return self 
 
    def __next__(self):        # __next__() 方法会返回下一个迭代器对象（在Python2中是next()）
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()  # StopIteration异常 用于标识迭代的完成，防止出现无限循环的情况。在 __next__() 中可设置在完成指定循环次数后（如上面的if语句）触发StopIteration异常 来结束迭代

#for n in Fab(5): 
#    print(n)
#如上两行代码也可用如下代替，效果相同：

f = Fab(5)
while True:
    try:
        print(next(f))
    except :
        sys.exit()



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
