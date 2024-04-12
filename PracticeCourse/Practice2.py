#Anagram Program : An anagram is a condition in which one string or number is rearranged in such a way that each character of the rearranged string or number is part of another string or number.

def checkAnagram(str1, str2):
    list1 = list(str1.lower())
    list2 = list(str2.lower())
    list1.sort()
    list2.sort()

    position = 0
    matches = True
    while position < len(str1) and matches is True:
        if list1[position] == list2[position]:
            position = position+1
        else:
            matches = False

    return matches

print(checkAnagram("Sayanava", "aaayanvs"))

#Fizzbuzz program :
number = int(input("Enter the range of number:"))
for i in range(number+1):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

#prime number
number = int(input("Enter the number:"))
flag = 0
if number == 1:
    flag = 1
    print("1 is not a prime number")
else:
    for i in range(2,number-1):
        if number % i == 0:
            flag = 1
            print("It is not a prime number")
            break

if flag==0:
    print("It is a prime number!")