#In Python, the descriptor protocol consists of three methods:
#__get__ gets an attribute value
#__set__ sets an attribute value
#__delete__ deletes an attribute
#A descriptor is an object of a class that implements one of the methods specified in the descriptor protocol including __set__, __get__, __del__

#Descriptors have two types: data descriptor and non-data descriptor.
    #A data descriptor is an object of a class that implements the __set__ and/or __delete__ method.
    #A non-data descriptor is an object that implements the __get__ method only.
class RequiredString:
    def __set_name__(self, owner, name):
        print(f'__set_name__ was called with owner={owner} and name={name}')
        self.property_name = name

    def __get__(self, instance, owner):
        print(f'__get__ was called with instance={instance} and owner={owner}')
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        print(f'__set__ was called with instance={instance} and value={value}')

        if not isinstance(value, str):
            raise ValueError(f'The {self.property_name} must a string')

        if len(value) == 0:
            raise ValueError(f'The {self.property_name} cannot be empty')

        instance.__dict__[self.property_name] = value


class Person:
    first_name = RequiredString()
    last_name = RequiredString()

person = Person()
person.first_name = 'John'
person.last_name = 'Snow'
print(person.first_name)

# -----------------------------------------------------
#Exception Handling
def division(a,b):
    try:
        return {
            'success' : True,
            'message' : 'OK',
            'result'  : a/b
        }
    except TypeError as e:
        return {
            'success': False,
            'message': 'Both a & b must be numbers',
            'result': None
        }
    except ZeroDivisionError as e:
        return  {
            'success': False,
            'message': 'b cannot be zero',
            'result': None
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
            'result': None
        }

result = division(10, 2)
print(result)

#If the code that handles different exceptions are the same, you can group all exceptions into one as follows:
def division(a, b):
    try:
        return {
            'success': True,
            'message': 'OK',
            'result': a / b
        }
    except (TypeError, ZeroDivisionError, Exception) as e:
        return {
            'success': False,
            'message': str(e),
            'result': None
        }
    finally:
        print("Am I seen?")


result = division(10, 0)
print(result)

#Example 2:
# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional
		# Part as Answer
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)
	finally:
		# this block is always executed
		# regardless of exception generation.
		print('This is always executed')

# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

#raise exception
def division(a, b):
    try:
        raise ValueError('The value error exception', 'x', 'y')
    except ValueError as ex:
        print(ex.args)

division(10,2)

# -----------------------------------------------------
#Custom Exception : Subclass the Exception class or one of its subclasses to define a custom exception class.
class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self,f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'The {self.f} is not in a valid range {self.min_f, self.max_f}'

def fahrenheit_to_celsius(f: float) -> float:
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        raise FahrenheitError(f)

    return (f - 32) * 5 / 9

if __name__ == '__main__':
    f = input('Enter a temperature in Fahrenheit:')
    try:
        f = float(f)
    except ValueError as ex:
        print(ex)
    else:
        try:
            c = fahrenheit_to_celsius(float(f))
        except FahrenheitError as ex:
            print(ex)
        else:
            print(f'{f} Fahrenheit = {c:.4f} Celsius')