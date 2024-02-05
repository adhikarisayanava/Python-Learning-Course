#Example1
name = 'John'
s = f'Hello, {name}!'
print(s)

#Example2
name = 'John'
s = f'Hello, {name.upper()}!' #"F" in uppercase is also valid here
print(s)

#Example3
name = 'John'
website = 'PythonTutorial.net'
message = f'''Hello {name}.
You're learning Python at {website}.'''
print(message)

#Example4
s = f'{{1+2}}' #{1+2}
print(s)

s = f'{{{1+2}}}' #{3}
print(s)

s = f'{{{{1+2}}}}' #{{1+2}}
print(s)

#Example5
number = 16
s = f'{number:x}'
print(s)  # 10

number = 0.01
s = f'{number:e}'
print(s)  # 1.000000e-02

number = 200
s = f'{number: 06}'
print(s)  # 00200

number = 9.98567
s = f'{number: .2f}'
print(s)  # 9.99

number = 400000000000
s = f'{number: ,}'  # also can use _
print(s)  # 400,000,000,000

number = 0.1259
s = f'{number: .2%}'
print(s)  # 12.59%

s = f'{number: .1%}'
print(s)  # 12.5%

# -----------------------------------------------------
#In Python, when you prefix a string with the letter r or R such as r'...' and R'...',
# that string becomes a raw string. Unlike a regular string, a raw string treats the backslashes (\) as literal characters.
s1 = r'lang\tver\nPython\t3'
s2 = 'lang\\tver\\nPython\\t3'
print(s1 == s2) # True

s = '\n'
print(len(s)) # 1

s = r'\n'
print(len(s)) # 2
#Since the backslash (\) escapes the single quote (') or double quotes ("), a raw string cannot end with an odd number of backslashes.

# -----------------------------------------------------
#To convert a regular string into a raw string, you use the built-in repr() function. For example:
s = '\n'
print(s)
raw_string = repr(s)
print(raw_string) #'\n'

# -----------------------------------------------------
#string join() : It returns a string which is the concatenation of strings in an iterable such as a tuple, a list, a dictionary, and a set.
colors = ('red', 'green', 'blue')
rgb = ','.join(colors)
print(rgb) #red,green,blue

#Concatenating strings
#Example1
s = 'String' + ' Concatenation'
print(s)

#Example2
s1, s2, s3 = 'Python', 'String', 'Concatenation'
s = f'{s1} {s2} {s3}'
print(s)

#Example3
s1, s2, s3 = 'Python', 'String', 'Concatenation'
s = ','.join([s1, s2, s3])
print(s)

#String split() example
s = 'Python String split'
substrings = s.split()
print(substrings) #['Python', 'String', 'split']

s = 'John,Doe,john.doe@example.com,(408)-999-1111'
contact = s.split(',')
print(contact)

s = 'apple,orange,banana'
results = s.split(',', 1)
print(results) #['apple', 'orange,banana']

s = 'apple,orange,banana'
results = s.split(',', -1)
print(results) #['apple', 'orange', 'banana']


