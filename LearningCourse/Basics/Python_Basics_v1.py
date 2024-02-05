#for listing the python keywords
import keyword
print(keyword.kwlist)
#-----------------------------------------------------
#first hello world
print ('Hello World!')
#-----------------------------------------------------
#learning indentation
def main():
    i = 1
    max = 10
    while ( i <= max ):
        print(i)
        i = i+1

#calling the main function
main()
#-----------------------------------------------------
#for continuation of statements, use backslash (\) character
a = True
b = True
c = True
if (a == True) and (b == True) and \
   (c == True):
    print("Contination of statements")
#-----------------------------------------------------
#String Literals
s = "This is a string"
print(s)
s1 = 'This is also a string'
print(s1)
#use ''' ''' triple quotes to span a string in multiple lines
s2 = '''This is yet 
      another string'''
print(s2)

#-----------------------------------------------------
#Python String
message = 'It\'s also a valid string'
#below raw strings can be used by adding the letter r
message2 = r'C:\python\bin'
print(message)
print(message2)
#-----------------------------------------------------
name = 'John'
message = 'Hi'
#to use value of variables in a string, use "f" which gives a format string
print(f"{message} {name}")
#-----------------------------------------------------
str = "Python String"
print(str[0])
print(str[1])
print(str[-1]) #returns character from end of string
print(str[-2])
str_length = len(str) #returns length of string
print(f"Length of string is : {str_length}")
#-----------------------------------------------------
#String slicing
str = "Sayanava Adhikari"
print(str[0:8]) #excludes the string at the end
#-----------------------------------------------------
#python string are immutable : it means you cannot change the string
str = "Sayanava Adhikari"
#str[0] = "J" #not allowed and will throw an error, instead you need to create a new one
new_str = "J" + str[1:]
print(new_str)
#-----------------------------------------------------
#To make the long numbers more readable, you can group digits using underscores, like this:
count = 10_000_000_000
print(count)
#-----------------------------------------------------
""" multiline
 docstrings
 """
#-----------------------------------------------------
#The input() function returns a string, not an integer.
price = int(input("Enter the price $:"))
tax = int(input("Enter the tax %:"))
print(type(tax))
tax_amount = (price * tax) / 100
print(tax_amount)
#-----------------------------------------------------
#if...elif...else
age = int(input("Enter your age:"))
if age < 5:
    ticket_price = 5
elif age < 16:
    ticket_price = 10
else:
    ticket_price = 20

print(f"Ticket price is ${ticket_price}")

#-----------------------------------------------------
#TERNARY OPERATOR
if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5
#INSTEAD WITH USE OF TERNARY OPERATOR, IT CAN BE WRITTEN AS:
ticket_price = 20 if int(age) >= 18 else 5

#-----------------------------------------------------
#FOR loop
for index in range(10):
    print(index)
#range(start, stop)
for index in range(1,6):
    print(f"for loop : {index}") #o/p: 1,2,3,4,5
#range(start, stop, step)
for index in range(0,11,2):
    print(index)

# -----------------------------------------------------
#while loop
max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1

# -----------------------------------------------------
#break statement
for index in range(0, 10):
    print(index)
    if index == 3:
        break

print('-- Help: type quit to exit --')
while True:
    color = input('Enter your favourite color:')
    if color.lower() == 'quit':
        break

# -----------------------------------------------------
#continue statement
for index in range(10):
    #print(index % 2)
    if index % 2:
        continue
    print(index)