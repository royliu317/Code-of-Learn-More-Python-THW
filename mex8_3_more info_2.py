import sys

def fibonacci(n):  # 定义普通函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        #yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10) # f变量是一个普通函数(其类型是 NoneType)


# ----------------------------------------------------------------------------------------------

import sys

def fibonacci(n): # 定义生成器函数（斐波那契）
    a, b, counter = 0, 1, 0

    while True:
        if (counter > n): 
            return
        yield a   # 在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值, 并在下一次执行next()方法时从当前位置继续运行。
        a, b = b, a + b
        print('a = %d, b = %d' % (a,b))
        counter += 1


f = fibonacci(10) # f变量是一个迭代器，是由生成器fibonacci()返回所生成的（其类型是 generator object）

while True:
    try:
        print("next(f) =", next(f), end="  /  ")  # next(f)的值即是当前fibonacci()函数yield的值（即yield时a的值，类型为int）
    except :
        sys.exit()



# 只要调用 next() 方法，生成器函数就会从 yield时 的位置继续运行，即便调用的是 print(type(next(f))) 也是如此。
# 要注意区分 fibonacci 和 fibonacci(10)：fibonacci是一个 generator function，而 fibonacci(10) 是调用 fibonacci 函数所返回的1个 generator object（GeneratorType, Iterable），
# 好比类的定义和类的实例的区别。
