#List is an ordered collection of items
numbers = [1, 3, 2, 7, 9, 4]
print(numbers)
print(numbers[-1])
numbers[0] = 10
print(numbers)
numbers.append(100)
print(numbers)
numbers.insert(2, 100) #the following inserts the number 100 at index 2 of the numbers list
print(numbers)
del numbers[0] #The del statement allows you to remove an element from a list by specifying the position of the element
print(numbers)
numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop() #The pop() method removes the last element from a list
print(last)
print(numbers)
numbers = [1, 3, 2, 7, 9, 4]
second = numbers.pop(1) #Typically, you use the pop() method when you want to remove an element from a list and still want to access the value of that element
print(second)
print(numbers)
numbers = [1, 3, 2, 7, 9, 4, 9] #o remove an element by value, you use the remove() method. Note that the remove() method removes only the first element it encounters in the list.
numbers.remove(9)
print(numbers)
# -----------------------------------------------------
#Tuples : Sometimes, you want to create a list of items that cannot be changed throughout the program. Tuples allow you to do that.
rgb = ('red', 'green', 'blue')
print(rgb)
print(rgb[0])
#To define a tuple with one element, you need to include a trailing comma after the first element. For example:
numbers = (3,)
print(type(numbers))
#If you exclude the trailing comma, the type of the numbers will be int , which stands for integer. And its value is 3. Python won’t create a tuple that includes the number 3
#Even though you can’t change a tuple, you can assign a new tuple to a variable that references a tuple.For example:
colors = ('red', 'green', 'blue')
print(colors)

colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)
# -----------------------------------------------------
#sort() function
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort() #by default it places the lower elements before the higher ones
print(guests)

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort(reverse=True)
print(guests)

scores = [5, 7, 4, 6, 9, 8]
scores.sort()
print(scores)
scores = [5, 7, 4, 6, 9, 8]
scores.sort(reverse=True)
print(scores)
# -----------------------------------------------------
#sorted() : does not change the original list unlike sort()
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests)

print(guests)
print(sorted_guests)
# -----------------------------------------------------
#list slice:
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[0:4] #or color[:4]
print(sub_colors)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[-3:] #the following returns a list that includes the last 3 elements of the colors list
print(sub_colors)
#o/p : ['blue', 'indigo', 'violet']

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[::2]
print(sub_colors) #The following example uses the step to return a sublist that includes every 2nd element of the colors list

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
reversed_colors = colors[::-1]
print(reversed_colors) #When you use a negative step, the slice includes the list of elements starting from the last element to the first element. In other words, it reverses the list.

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[0:2] = ['black', 'white'] #The following example changes the first two elements in the colors list to the new values
print(colors)
#o/p : ['black', 'white', 'yellow', 'green', 'blue', 'indigo', 'violet']

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(f"The list has {len(colors)} elements")
colors[0:2] = ['black', 'white', 'gray'] #The following example uses the list slice to replace the first and second elements with the new ones and also add a new element to the list
print(colors)
print(f"The list now has {len(colors)} elements")

#o/p:
#The list has 7 elements
#['black', 'white', 'gray', 'yellow', 'green', 'blue', 'indigo', 'violet']
#The list now has 8 elements

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
del colors[2:5] #The following shows how to use the list slice to delete the 3rd, 4th, and 5th elements from the colors list
print(colors)
#O/P: ['red', 'orange', 'indigo', 'violet']

# -----------------------------------------------------
#List unpacking
colors = ['red', 'blue', 'green']
red, green, blue = colors
print(red)

colors = ['red', 'blue', 'green']
red, blue, *other = colors
print(red) #red
print(blue) #blue
print(other) #['green']

colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *other = colors
print(cyan) #cyan
print(magenta) #magenta
print(other) #['yellow', 'black']

# -----------------------------------------------------
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for city in cities:
    print(city)

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
#The enumerate() function returns a tuple that contains the current index and element of the list.
for item in enumerate(cities):
    print(item)

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
#The enumerate() function returns a tuple that contains the current index and element of the list.
for item, city in enumerate(cities):
    print(f"{item}:{city}")

# -----------------------------------------------------
#index()
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'Cairo'

if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")

# -----------------------------------------------------
#range() function is an iterable
for index in range(3):
    print(index)

#Also, a string is an iterable because you can use a for loop to iterate over it
str = "Sayanava"
for ch in str:
    print(ch)

#Lists and tuples are also iterables because you can loop over them. For example:
ranks = ['high', 'medium', 'low']

for rank in ranks:
    print(rank)

#iter() function
colors = ['red', 'green', 'blue']
iterator = iter(colors)

for color in iterator:
    print(color)

# -----------------------------------------------------
#map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.
def double(bonus):
    return bonus * 2

bonuses = [100, 200, 300]
iterator = map(double, bonuses) #map function returns an iterator
print(list(iterator))

# -----------------------------------------------------
#hash() : The Python hash() function is used to return a hash value of an object if it has one.
#The Python hash() built-in function returns an integer value for every object which is hashable.
#The hash method is used in programming to return integer values that can be used to compare dictionary keys using a dictionary look-up function.
#If an item has a hash value that never changes during its lifespan, it is hashable.
#Hence hash() function only works on immutable objects such as int, string, tuple, float, long, Unicode, bool. Mutable objects such as list, dict, set, bytearray are non-hashable.
a = 100
b = 12.35
txt = 'Hello'

print('Hash value of 100 is:', hash(a))
print('Hash value of 12.35 is:', hash(b))
print('Hash value of Hello is:', hash(txt))

#o/p:Hash value of 100 is: 100
#Hash value of 12.35 is: 807045053224792076
#Hash value of Hello is: -6456706318375158412