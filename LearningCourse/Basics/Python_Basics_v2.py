#function in python
def greet(name):
    print(f"Hi {name}")

ask_name = input("What is your name:")
greet(ask_name)

# -----------------------------------------------------
#return in function
def greet(name):
    return (f"Hi {name}")

greeting = greet("Sayan")
print(greeting)

def sum(a, b):
    return a + b

total = sum(10,20)
print(total)

# -----------------------------------------------------
#keyword arguments
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(price=100, discount=0.1)
#or, both returns same result
net_price = get_net_price(discount=0.1, price=100)


def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

net_price = get_net_price(price=100, discount=0.06)
print(net_price)
#or, both returns same result
net_price = get_net_price(100, discount=0.06)
print(net_price)
#Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.
#net_price = get_net_price(100, tax=0.08, 0.06) this will result in an error because it uses positional argument after a keyword argument
#To fix this, you need to use the keyword argument for the third argument like this:
net_price = get_net_price(100, tax=0.08, discount=0.06)
print(net_price)
# -----------------------------------------------------
#Recursive function
def fac_recursive(n):
    if n == 1:
        return 1
    else:
        return (n * fac_recursive(n-1))

result = fac_recursive(5)
print(f"Factorial of 5 is {result}")

# -----------------------------------------------------
#Use Python lambda expressions to create anonymous functions, which are functions without names.
#A lambda expression accepts one or more arguments, contains an expression, and returns the result of that expression.
add = lambda x,y : x+y
print(add(3,4))
#or
print((lambda x,y : x+y)(4,6))

# -----------------------------------------------------
#docstrings to document functions
from pprint import pprint
def adding(a, b):
    ''' Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    '''
    return a + b

help(adding) #will return the description of the function