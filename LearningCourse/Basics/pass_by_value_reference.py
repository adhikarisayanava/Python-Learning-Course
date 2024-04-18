#In Python, it is neither "pass-by-value" nor "pass-by-reference" but "pass-by-object-reference".

#If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like call-by-value. 
def update_value(x):
  x = 10
  print("x inside function: ", x) #10

val = 5
update_value(val)
print("val outside function: ", val) #5

#If you pass mutable arguments like lists, dictionary, they are also passed by object reference, but they can change the original variable i.e. caller.
def update_list(lst):
    lst.append(10)
    print("List inside function", lst)
    

my_list = [1,2,3,4,5]
update_list(my_list)
print("List outside function", my_list)
# Output: List inside function [1, 2, 3, 4, 5, 10]
# Output: List outside function [1, 2, 3, 4, 5, 10]