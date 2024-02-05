#Abstract class
#In object-oriented programming, an abstract class(if it has an abstract method) is a class that cannot be instantiated. However, you can create classes that inherit from an abstract class.
#Typically, you use an abstract class to create a blueprint for other classes.
#Similarly, an abstract method is an method without an implementation. An abstract class may or may not include abstract methods.
#Python doesn’t directly support abstract classes. But it does offer a module that allows you to define abstract classes.To define an abstract class, you use the abc (abstract base class) module.
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name,last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate

class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self,employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            pass
            print (f"{e.full_name} \t ${e.get_salary()}")

payroll = Payroll()
payroll.add(FulltimeEmployee('John', 'Doe', 6000))
payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
payroll.print()
#empl = Employee('Say', 'Adh') #this will throw an error since abstract class having an abstract method cannot be initated

# -----------------------------------------------------
#Enumertation: By definition, an enumeration is a set of members that have associated unique constant values. Enumeration is often called enum.
#Create a new enumeration by defining a class that inherits from the Enum type of the enum module.
#Use the enumeration[member_name] to access a member by its name and enumeration(member_value) to access a member by its value.
#Enumerations are interable and hashable(immutable)

from enum import Enum
import json

class ResponseStatus(Enum):
    PENDING = 'pending'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'

response = '''{
    "status":"pending"
}'''

data = json.loads(response)
status = data['status']

try:
    if ResponseStatus(status) is ResponseStatus.FULFILLED:
        print("The response status is FULFILLED")
    elif ResponseStatus(status) is ResponseStatus.PENDING:
        print("The response status is PENDING")
    elif ResponseStatus(status) is ResponseStatus.REJECTED:
        print("The response status is REJECTED")
except ValueError as error:
    print(error)

#By definition, the enumeration member values are unique. However, you can create different member names with the same values.
#When you define multiple members in an enumeration with the same values, Python does not create different members but aliases.

from enum import Enum
from pprint import pprint

class Color(Enum):
    RED = 1
    CRIMSON = 1
    SALMON = 1
    GREEN = 2
    BLUE = 3
print(Color.RED is Color.CRIMSON) #True
print(Color.RED is Color.SALMON) #True
print(Color(1)) #Color.RED,When you look up a member by value, you’ll always get the main member, not aliases.
#When you iterate the members of an enumeration with aliases, you’ll get only the main members, not the aliases:
for color in Color:
    print(color)

#o/p:Color.RED
#Color.GREEN
#Color.BLUE

#To get all the members including aliases, you need to use the __member__ property of the enumeration class.
pprint(Color.__members__)

# -----------------------------------------------------
#Use the @enum.unique decorator from the enum module to enforce the uniqueness of the values of the members.
from enum import Enum
import enum

@enum.unique
class Day(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'

print(Day.TUE.name) #TUE
print(Day.TUE.value) #Tuesday
print(Day.TUE) #Day.TUE
#o/p:ValueError: duplicate values found in <enum 'Day'>: TUE -> MON

#The auto() helper class in the enum module automatically generates unique values for the enumeration members.
from enum import Enum, auto


class State(Enum):
    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()

    def __str__(self):
        return f'{self.name(self.value)}'

for state in State:
    print(state.name,state.value)























