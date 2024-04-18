#Swapping 2 numbers without using third variable and variable scope
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

##############################################################

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

##############################################################
#an iterator is an object that contains a countable number of values and that can be iterated upon. It is used to abstract the process of looping over a collection of items, like lists, tuples, dictionaries, sets, etc.
def trying_iterator():
    myList = [1,2,3,4]
    myIter = iter(myList)

    print(f"\n From Iterator :{next(myIter)}")

trying_iterator()