
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 10) 
print(result)

# Create a function which adds two numbers and returns the result

#Create a function to check if a given
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True 

result = is_prime(5)
if result == True:
    print("The number is prime")
else:
    print("The number is not prime")

    