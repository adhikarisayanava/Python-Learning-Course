from pprint import pprint
#Defining a basic class and instance
class Person:
    counter = 0 #class attribute, shared by all instances of the class

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi {self.name}"


person1 = Person("Shayo",30)
print(person1.greet())
person2 = Person("Pallabi",32)
print(person2.greet())
print(Person.counter)
# -----------------------------------------------------
#class method and static method
class Book:
    TYPES = ("hardcover","paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    #a class method is shared by all instances of the class
    #A class method is a method that is bound to a class rather than its object.
    # It doesn't require creation of a class instance, much like staticmethod.
    #You can use class methods for any methods that are not bound to a specific instance but the class.
    # In practice, you often use class methods for methods that create an instance of the class.
    # The difference between a static method and a class method is: Static method knows nothing about the class and just deals with the parameters.
    @classmethod
    def hardcover(cls, name, weight):
        return Book(name, cls.TYPES[0], weight+100)

    #instance method
    def hello_name(self):
        print(f"I am printing this inside instance method : {self.name}")

    #A static method is not bound to a class or any instances of the class. In Python, you use static methods to group logically related functions in a class.
    @staticmethod
    def static_method(c):
        print("static method called!")
        return 9 * c / 5 + 32


print(Book.static_method(30)) #calling the static method using class name
book = Book.hardcover("HarryPotter", 1500)
print(book.weight)
book2 = Book("Chetan", "hardcover", 1700)
book2.static_method(12)
print(book2.weight)
book2.hello_name()
book.hello_name()

# -----------------------------------------------------
#inheritance
class Person:
    counter = 0 #class attribute, shared by all instances of the class.They are useful in some cases such as storing class constants, tracking data across all instances, and defining default values

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi it's {self.name}."


class Employee(Person):
    def __init__(self, name, age, job_title, location):
        super().__init__(name,age)
        self.job_title = job_title
        self.location = location

    def greet(self):
        return super().greet() + f"I am a {self.job_title}"

    def location_info(self):
        print(f"I stay in {self.location}")


person = Person('Roy', 30)
print(person.greet())
employee = Employee('John',25, "Python developer.", "Hoofddorp")
print(employee.greet())
employee.location_info()

# -----------------------------------------------------
class HtmlDocument:
    extension = 'html'
    version = '5'

print(HtmlDocument.extension)
print(HtmlDocument.version)
#The getattr() function accepts an object and a variable name. It returns the value of the class variable. For example:
extension = getattr(HtmlDocument, 'extension')
version = getattr(HtmlDocument, 'version')
#To set a value for a class variable, you cane use the dot notation, or setattr() function:
HtmlDocument.media_type = "text/html"
setattr(HtmlDocument, 'owner', 'Sayanava')
#Python stores class variables in the __dict__ attribute. The __dict__ is a mapping proxy, which is a dictionary. For example:
pprint(HtmlDocument.__dict__)

#Note : when you define a class that doesn’t inherit from any class, it’ll implicitly inherit from the built-in object class.

# -----------------------------------------------------
#Encapsulation : Encapsulation is the packing of data and functions that work on that data within a single object.
# By doing so, you can hide the internal state of the object from the outside. This is known as information hiding.
#A class is an example of encapsulation. A class bundles data and methods into a single unit. And a class provides the access to its attributes via methods.
#Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class.
#If you prefix an attribute name with double underscores (__),Python will automatically change the name of the __attribute to:  _class__attribute.This is called name mangling in Python.
class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

counter = Counter()
#print(counter.__current) #won't work, you cannot access the __attribute directly from outside of a class
print(counter._Counter__current) #this is possible

# -----------------------------------------------------
#__str__ : To customize the string representation of a class instance, the class needs to implement the __str__ magic method.
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'

person = Person('John', 'Doe', 25)
print(person) #when you use the print() function to print out an instance of the Person class, Python calls the __str__ method defined in the Person class.
#o/p:Person(John,Doe,25)

#__repr__ : The __str__ method returns a string representation of an object that is human-readable while the __repr__ method returns a string representation of an object that is machine-readable.
#The __str__ calls __repr__ internally by default.
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'


person = Person('John', 'Doe', 25)
# use str()
print(person)

# use repr()
print(repr(person))

# -----------------------------------------------------
#__eq__ :  method to define the equality logic for comparing two objects using the equal operator (==)
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age

        return False


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27)

print(john == jane)  # True
print(john == mary)  # False


john = Person('John', 'Doe', 25)
print(john == 20)  # False

# -----------------------------------------------------
#In Python, the garbage collector manages memory automatically. The garbage collector will destroy the objects that are not referenced.
#If an object implements the __del__ method, Python calls the __del__ method right before the garbage collector destroys the object.
#Exception occurs inside the __del__ method is not raised but silent.
#Avoid using __del__ for clean up resources; use the context manager instead.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called')


if __name__ == '__main__': #this statement checks if the script is being run as the main program.
    person = Person('John Doe', 23)
    #person = None
    #OR
    del person

