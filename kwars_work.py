# Write a function that takes an unknown number of arguments and returns their sum.
def number_known(*number):
    return number

number_known(1,2,45,67,89,9)
 


# Write a function that takes two arguments,
#  the first being a string and the second being an unknown number of integers.
#  The function should return a new string where the integers have been added to the original string.
def integers_to_string(string, *integers):
    for integer in integers:
        string += str(integer)
    return string
integers_to_string("Hey", 1, 2, 3)


# Write a function that takes an unknown number of keyword arguments and
#  returns a dictionary where the keys are the argument names and the values are the argument values.
def kwargs_dict(**kwargs):
    return kwargs

kwargs_dict(name="Ann", age=20, location="Nairobi")



# Write a function that takes a function and an unknown number of arguments, 
# and returns the result of calling the function with the arguments.
def number_argument( fun,*args):
  
    return fun(*args)

# Write a function that takes a list of integers and an unknown number of keyword arguments.
#  The function should return a new list where each integer in 
# the original list has been multiplied by the value of the 
# corresponding keyword argument.
def multiply_with_keyword_arguments(integers, **kwarg):
    result = []
    for integer in integers:

# Write a function that takes a list of integers and an unknown 
# number of additional integers as arguments. The function
#  should return the index of the first occurrence of the 
# sum of the list and the additional integers.
def find_sum_index(nums, *args):
    total = sum(nums) + sum(args)
    for i, num in enumerate(nums):
        if total - num == num:
            return i
    return -1



# Write a function that takes an unknown number of keyword 
# arguments, each with a string value. The function should concatenate
#  all the strings and return the resulting string.
def concatenate_strings(**kwargs):
    return "".join(kwargs.values())