#Addition of 2 numbers

def add(a,b):
    return a+b

print(add(4,5))

#Print whether a number is even or odd
user_input = int(input("Enter the number to check even or odd:"))
if user_input % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

#Reverse a number
number = int(input("Enter the integer number to reverse: "))
revs_number = 0
while number > 0:
    remainder = number % 10                                #3,2
    revs_number = (revs_number * 10) + remainder           #3,32,321
    number = number // 10 #integer(floor division)         #12,1

print("The reverse number is :", revs_number)

#Reverse a number(second way using string slicing)
n = input("Enter the number to reverse:")
#num = str(n)
print(type(n))
print(f"Num is {n}")
result = int(n[::-1])
print(result)

#Armstrong number, for example 153 = 1**3 + 5**3 + 3**3
n = input("Enter the number to check if it is armstrong:")
length = len(n)
print(f"Length of number is {length}")
sum = 0
number = int(n)
while (number > 0):
    remainder = number % 10
    sum = sum + remainder ** length
    number = number // 10

print(f"The final sum value is: {sum} and number is {number}")
if sum == int(n):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

#Leap Year program : A leap year is a year that follows any one of the below-specified conditions:
#Year divisible by 400.
#Year divisible by 4 but not by 100.
def checkLeapYear(year):
    import calendar
    return (calendar.isleap(year))

year = int(input("Enter the year to check if it is leap year or not:"))
if (checkLeapYear(year)):
    print("It is a leap year!")
else:
    print("It is not a leap year!")
'''
#Another approach
if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0):
    print("It is a leap year!")
else:
    print("It is not a leap year!")
'''
#Factorial of a number
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))

number = int(input("Enter the number to check factorial:"))
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    print(factorial(number))















