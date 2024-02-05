from pprint import pprint
#Operator overloading
#The ability to use the built-in operator (+) on a custom type is known as operator overloading.
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, point): #+ from line 22 below calls in turn this function
        if not isinstance(point, Point2D):
            raise ValueError('The other must be an instance of the Point2D')

        return Point2D(self.x + point.x, self.y + point.y)


if __name__ == '__main__':
    a = Point2D(10, 20)
    b = Point2D(15, 25)
    c = a + b
    print(c)

# -----------------------------------------------------
#Getter and Setter methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

    #To define a getter and setter method while achieving backward compatibility, you can use the property() class.
    #The property() has the following parameters:
        #fget is a function to get the value of the attribute, or the getter method.
        #fset is a function to set the value of the attribute, or the setter method.
        #fdel is a function to delete the attribute.
        #doc is a docstring i.e., a comment.
    #The property class returns a property object. The property() class has the following syntax:property(fget=None, fset=None, fdel=None, doc=None)
    age = property(fget=get_age, fset=set_age)

print(Person.age)
john = Person('John', 18)
#pprint(john.__dict__)
print(john.get_age())
print(john.age)
john.set_age(20)
print(john.age)

# -----------------------------------------------------
#@property decorator : is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property().
# Defining class
class Portal:

    # Defining __init__ method
    def __init__(self):
        self._name = ''

    # Using @property decorator
    @property
    # Getter method
    def name(self):
        print("I am inside getter method")
        return self._name

    # Setter method
    @name.setter
    def name(self, val):
        print("I am inside setter method")
        self._name = val

    # Deleter method : to delete a property of an instance of a class
    @name.deleter
    def name(self):
        del self._name


# Creating object
p = Portal()

# Setting name
p.name = 'GeeksforGeeks'

# Prints name
print(p.name)

# Deletes name
del p.name

# As name is deleted above this
# will throw an error
#print(p.name)

# -----------------------------------------------------
#Method overriding
class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, incentive):
        #self.name = name
        #self.base_pay = base_pay
        #Above 2 lines can be replaced by super(), for example:
        super().__init__(name, base_pay)
        self.incentive = incentive

    def get_pay(self):
        #return self.base_pay + self.incentive
        #Above line also can be rewritten as:
        return super().get_pay() + self.incentive

if __name__ == '__main__':
    john = SalesEmployee('John', 5000, 1000)
    print(john.get_pay())
    jane = Employee('Jane', 5500)
    print(jane.get_pay())