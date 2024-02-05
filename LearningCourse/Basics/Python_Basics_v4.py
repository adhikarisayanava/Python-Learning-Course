#Use the Python filter() function to filter a list (or a tuple).
#Example 1:
scores = [70,60,80,90,50]
filtered = filter(lambda score: score >=70, scores)
#The filter() function iterates over the elements of the list and applies the fn() function to each element. It returns an iterator for the elements(similar to map()).
print(list(filtered))

#Example 2:
countries = [
    ('China', 1394015977),
    ('United States', 329877505),
    ('India', 1326093247),
    ('Indonesia', 267026366),
    ('Bangladesh', 162650853),
    ('Pakistan', 233500636),
    ('Nigeria', 214028302),
    ('Brazil', 21171597),
    ('Russia', 141722205),
    ('Mexico', 128649565)
]
populated = filter(lambda c: c[1] > 300000000, countries)
print(list(populated))

# -----------------------------------------------------
#Dictionary in Python : is a collection of key-value pairs, where each key has an associated value.
#Use square brackets or get() method to access a value by its key.
#Use the del statement to remove a key-value pair by the key from the dictionary.

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
print(person['first_name']) #John
print(person['last_name']) #Doe
#ssn = person['ssn'] #If you attempt to access a key that doesn’t exist, you’ll get an error.To avoid this error, you can use the get() method of the dictionary
ssn = person.get('ssn')
print(ssn) #o/p: None
#Adding new key-value pairs
person['gender'] = 'Female'
print(person)
person['age'] = 26
print(person)
del person['gender']
print(person)
#looping in dictionary
for key, value in person.items():
    print(f"{key}:{value}")

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

# -----------------------------------------------------
#Set in python : is an unordered list of immutable elements.
#Elements in a set are unordered.Elements in a set are unique. A set doesn’t allow duplicate elements.
empty_set = {} # but this is treated as empty dictionary
empty_set = set() #this is treated as empty set. An empty set evaulates to False.
#you can pass an iterable to the set() function to create a set.for example:
skills = set(['Problem solving','Critical Thinking'])
print(skills) #{'Critical Thinking', 'Problem solving'}
#If an iterable has duplicate elements, the set() function will remove them. For example:
characters = set('letter')
print(characters) #{'r', 'l', 't', 'e'}
#getting size of a set:
ratings = {1, 2, 3, 4, 5}
size = len(ratings)
print(size)
#Checking if an element is in a set
ratings = {1, 2, 3, 4, 5}
rating = 1
if rating in ratings:
    print(f'The set contains {rating}') #The set contains 1

#Adding element to a set
skills = {'Python programming', 'Software design'}
skills.add('Problem solving')
print(skills) #{'Problem solving', 'Software design', 'Python programming'}, this order can vary

#Removing element from a set
skills.remove('Problem solving')
skills.discard('Debugging') #this allows to remove a non-existing element without throwing an error

#To remove and return an element from a set, you use the pop() method.
skills = {'Problem solving', 'Software design', 'Python programming'}
skill = skills.pop() #it’ll show a different value each time
print(skill)

#To make a set immutable, you use the built-in function called frozenset(). The frozenset() returns a new immutable set from an existing one.
skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)
#skills.add('Django') #if you attempt to modify elements of the set, you’ll get an error

#Looping through set elements:
skills = {'Problem solving', 'Software design', 'Python programming'}
for skill in skills:
    print(skill)

#OR, use enumerate function similar to list, to access the index of the current element inside the loop:
for index, skill in enumerate(skills):
    print(f"{index}.{skill}")

# -----------------------------------------------------
#Union() method vs set union operator
rates = {1, 2, 3}
ranks = [2, 3, 4]
ratings = rates.union(ranks) #the union() method accepts one or more iterables, converts the iterables to sets, and performs the union(finds all unique entries).
print(ratings) #{1, 2, 3, 4}
#set union | operator : only allows sets
rates = {1, 2, 3}
ranks = [2, 3, 4]
#ratings = rates | ranks #It will throw an error
#instead:
rates = {1, 2, 3}
ranks = {2, 3, 4}
ratings = rates | ranks
print(ratings)

# -----------------------------------------------------
#Intersection() method, like union(),can accept any iterables, like strings, lists, and dictionaries.
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.intersection(s2)
print(s)
#set intersection operator (&)
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 & s2
print(s)

#example2:
numbers = {1, 2, 3}
scores = [2, 3, 4]
values = (2,5,6)
numbers = numbers.intersection(scores,values)
print(numbers) #o/p:{2}
#Whereas below one will fail:
numbers = {1, 2, 3}
scores = [2, 3, 4]
#numbers = numbers & scores #will thrown an error since it works with sets only

# -----------------------------------------------------
#Set difference() method
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)
print(s) #{'Python'}

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2.difference(s1)
print(s) #{'C#'}

#difference operator (-)
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 - s2
print(s) #{'Python'}

scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores.difference(numbers)
print(new_scores)
#However, below will throw an error:
scores = {7, 8, 9}
numbers = [9, 10]
#new_scores = scores - numbers #won't work since it works only wit sets

# -----------------------------------------------------
#symmetric_difference() method that returns the symmetric difference of two or more sets
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.symmetric_difference(s2)
print(s) #{'Python', 'C#'}, order can vary
#symmetric difference operator(^)
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 ^ s2
print(s)#{'Python', 'C#'}, order can vary

#Example2:
scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores.symmetric_difference(ratings)
print(new_set) #{10,7}

scores = {7, 8, 9}
ratings = [8, 9, 10]
#new_set = scores ^ ratings #won't work since it works only wit sets

# -----------------------------------------------------
#issubset() method returns True if a set is a subset of another set.Exact similarly there is also issuperset(), superset operator(>=) or proper superset operator(>)
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
print(scores.issubset(numbers)) #True

numbers = {1, 2, 3, 4, 5}
print(numbers.issubset(numbers)) #True

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
print(numbers.issubset(scores)) #False

#Besides using the issubset() method, you can use the subset operator (<=) to check if a set is a subset of another set
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores <= numbers
print(result)  # True

result = numbers <= numbers
print(result)  # True

#The proper subset operator (<) check if the set_a is a proper subset of the set_b
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores < numbers
print(result)  # True

result = numbers < numbers
print(result)  # False

# -----------------------------------------------------
#isdisjoint() : no elements in common
letters = {'A', 'B', 'C'}
result = letters.isdisjoint([1, 2, 3]) #The following example passes a list to the isdisjoint() method instead of a set
print(result) #true