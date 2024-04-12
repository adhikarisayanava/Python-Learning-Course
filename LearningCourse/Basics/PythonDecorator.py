import time

def timing_decorator(func):
    def wrapper(time_count):
        start = time.time() # get the current time
        result = func(time_count) # call the original function
        end = time.time() # get the current time again
        print(f"Time taken by {func.__name__} function: {end - start} seconds")
        return result
    return wrapper

@timing_decorator
def my_func(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

my_func(1000000)