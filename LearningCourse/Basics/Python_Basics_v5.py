#reading a text file in python
'''
with open('the-zen-of-python.txt') as f:
    contents = f.read() #reads the entire file
    #f.readline() #read a single line from a text file and return the line as a string. If the end of a file has been reached, the readline() returns an empty string.
    #f.readlines() #read all the lines of the text file into a list of strings. This method is useful if you have a small file and you want to manipulate the whole text of that file.
    print(contents)
    f.close()

#OR
with open('the-zen-of-python.txt') as f:
    [print(line.strip()) for line in f.readlines()] #To remove the blank line after each line , you can use the strip() method.
f.close()

#OR
with open('the-zen-of-python.txt') as f: #The open() function returns a file object which is an iterable object. Therefore, you can use a for loop to iterate over the lines of a text file as follows:
    for line in f:
        print(line.strip())
f.close()

# -----------------------------------------------------
#Writing to a file
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
f.close()

lines = ['Readme', 'How to write text files in Python']
with open('readme2.txt', 'w') as f:
    f.writelines('\n'.join(lines)) #to join each line using a new line
f.close()

#Appending text files
more_lines = ['Append text files','The End!']
with open('readme.txt', 'a') as f:
    for line in more_lines:
        f.write(line)
        f.write('\n')
f.close()

# -----------------------------------------------------
#Check if a file exists
#Approach1
from os.path import exists
file_exists=exists('readme.txt')
print(file_exists)

#Approach2
from pathlib import Path
path = Path('readme2.txt')
print(path.is_file())

# -----------------------------------------------------
#Reading a csv file in python
import csv
with open('country.csv', encoding="UTF-8") as f:
    csv_reader = csv.DictReader(f)
    #Skip the header
    next(csv_reader)
    for line in csv_reader:
        print(f"The are of {line['name']} is {line['area']} km2")
f.close()

#If you want to have different field names other than the ones specified in the first line,
# you can explicitly specify them by passing a list of field names to the DictReader() constructor like this:
import csv

fieldnames = ['country_name', 'area', 'code2', 'code3']

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldnames)
    # Skip the header
    next(csv_reader)
    for line in csv_reader:
        print(f"The area of {line['country_name']} is {line['area']} km2")
f.close()

# -----------------------------------------------------
#Writing a csv file
import csv
header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']
data1 = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]
with open('countries.csv','w', encoding='UTF-8', newline='') as f: #To remove the blank line, you pass the keyword argument newline='' to the open() function
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    writer.writerows(data1) #to write multiple rows to csv

#If each row of the CSV file is a dictionary, you can use the DictWriter class of the csv module to write the dictionary to the CSV file.
import csv
fieldnames = ['name', 'area', 'country_code2', 'country_code3']
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]
with open('countries1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f,fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# -----------------------------------------------------
#Deleting a file
import os
file_name = 'readme.txt'
if os.path.exists(file_name):
    os.remove(file_name)

# -----------------------------------------------------
#Python rename file
import os
os.rename('readme2.txt','readme3.txt')
'''
# -----------------------------------------------------
import os
print(os.getcwd())
os.chdir('./script/')
print(os.getcwd())

# -----------------------------------------------------
#join and split a path
#The join() function joins path components together and returns a path with the corresponding path separator. \
# For example, it uses backslash (\) on Windows and forward slash (/) on macOS or Linux.
import os
fp = os.path.join('temp', 'python')
print(fp)  # temp\python (on Windows)
pc = os.path.split(fp)
print(pc)  # ('temp', 'python')

#Example2:
import os
dir = os.path.join("C:\\", "Users")
print(dir)
if os.path.exists(dir) or os.path.isdir(dir):
    print(f'The {dir} is a directory')
else:
    print("Dir does not exist")

#Create a directory
import os
dir = os.path.join("C:\\", "Users", "Sayanava_Adhikari", "Pictures", "DirFromPython")
if not os.path.exists(dir):
    os.mkdir(dir)

#Renaming a directory
'''
import os
old_path = os.path.join("C:\\", "Users", "Sayanava_Adhikari", "Pictures", "DirFromPython")
new_path = os.path.join("C:\\", "Users", "Sayanava_Adhikari", "Pictures", "DirFromPythonRenamed")

if os.path.exists(old_path) and not os.path.exists(new_path):
    os.rename(old_path,new_path)
'''
#Removing a directory
import os
dir_path = os.path.join("C:\\", "Users", "Sayanava_Adhikari", "Pictures", "DirFromPython")
if os.path.exists(dir_path):
    os.rmdir(dir_path)
    print(f"{dir_path} is removed")

# -----------------------------------------------------
#The os.walk() function generates file names in a directory by walking the tree either top-down or bottom-up.
#The os.walk() function yields a tuple with three fields (dirpath, dirnames, and filenames) for each directory in the directory tree.
import os
os.chdir('C:/Users/Sayanava_Adhikari/Pictures')
path = os.getcwd()
png_files = []
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('png'):
            png_files.append(os.path.join(dirpath,filename))

for files in png_files:
    print(files)

