x = 10

def swap(a, b): #a = 5, b = 6
    global x
    a = a + b #a=11
    b = a - b #5
    a = a -b #6
    x = 20
    print(f"After swapping a is:{a} and b is:{b}")
    print(f"x inside swap is: {x}")

swap(10,15)
print(f"x is: {x}")

import time
def timing_decorator(func):
    def wrapper(time_count):
            start_time = time.time()
            ret = func(time_count)
            stop = time.time()
            diff = stop - start_time
            print(f"Time to execute the function is {diff}")
    return wrapper

@timing_decorator
def func(n):
    sum = 0
    for i in range(n):
        sum = sum + i

func(1000000)

#fibonacci series
#Generator using yield keyword
def fibonacci():
    a, b = 0, 1
    while True:
        yield a #Generators, in general, are used to create iterators with a different approach. They employ the use of yield keyword rather than return to return a generator object.
        a, b = b, a + b

f = fibonacci()
for _ in range(10):
    print(next(f))

