# Higher Order Functions
# In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable
# In this section, we will cover:

# Handling functions as parameters
# Returning functions as return value from another functions
# Using Python closures and decorators


# function as parameter

# def sum_number(num):
#     return sum(num)

# def highorder_function(f,lst):
#     sumadd=f(lst)
#     return sumadd
# result = highorder_function(sum_number,[1,2,3,4])
# print(result)


# ------------closure-----------

# def add_ten():
#     ten = 10
#     def add(num):
#         return num + ten
#     return add

# closure_result = add_ten()
# print(closure_result(5))  # 15
# print(closure_result(10))  # 20


def square(num):
    def n(x):
        return x * num

    return n


result = square(3)
# print(result(3))
print(result(4))





