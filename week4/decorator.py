# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

# Basic Decorator
# Define the decorator first, then apply it with @decorator_name above the function.
def changecase(func):
    def inner():
        return func().upper()
    return inner
@changecase
def function():
    return "Hello Sally"
print(function())

print(" ")
# By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
# The function changecase is the decorator.
# The function myfunction is the function that gets decorated.

# Multiple Decorator Calls
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

# Example
# Using the @changecase decorator on two functions:
def changecase(func):
    def inner():
        return func().upper()
    return inner
@changecase
def function():
    return "Hello, Sally"
@changecase
def function1():
    return "I am speed!"
print(function())
print(function1())