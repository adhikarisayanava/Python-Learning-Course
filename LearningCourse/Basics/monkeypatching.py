#Monkey patching refers to the practice of dynamically modifying a class or a module at runtime.

class Myclass:
    def greet(self):
        print("Hello")

def new_greet(self):
    print("Hello, I have been monkey patched")

obj = Myclass()
obj.greet() #Hello

#Monkey-patching
Myclass.greet = new_greet
obj.greet() #Hello, I have been monkey patched