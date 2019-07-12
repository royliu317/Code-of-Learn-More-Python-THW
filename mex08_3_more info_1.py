# Create a class and use it as an iterator

import sys

class Fab():                   # crete an iterator needs to accomplish two methods: __iter__()  and  __next__()
 
    def __init__(self, max):   #  __init__() will run during the object's initiation
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 
 
    def __iter__(self):        # __iter__() returns a specific iterator object which accomplish __next__() method and mark the iteration's completion via StopIteration error
        return self 
 
    def __next__(self):        # __next__() returns the next iterator object
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()  


f = Fab(5)
while True:
    try:
        print(next(f))
    except :
        sys.exit()

