import sys

def fibonacci(n): 
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        #yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10) 

# ----------------------------------------------------------------------------------------------

import sys

def fibonacci(n): # generator function
    a, b, counter = 0, 1, 0

    while True:
        if (counter > n): 
            return
        yield a   
        a, b = b, a + b
        print('a = %d, b = %d' % (a,b))
        counter += 1


f = fibonacci(10) # f is an iterator return by generator fibonacci()

while True:
    try:
        print("next(f) =", next(f), end="  /  ")  
    except :
        sys.exit()

