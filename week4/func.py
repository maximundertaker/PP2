# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")
my_function()

print(" ")
# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

print(" ")
# Arguments are often shortened to args in Python documentations.

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")

print(" ")
# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# his way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Refh", "Nana")

print(" ")
# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_func(child3, child2, child1):
    print("The youngest child is " + child3)
my_func("Lisa", "Dira", "Ura")

print(" ")
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def name(**kid):
    print("His last name is " + kid["lname"])
name(fname = "Tobias", lname = "Refsnes")

print(" ")
# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def coutry(country = "Norway"):
    print("I am from " + country)
coutry("Sweden")
coutry("India")
coutry()
coutry("brazil")

print(" ")
# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def a(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
a(fruits)

print(" ")
# Return Values
# To let a function return a value, use the return statement:
def b(x):
    return 5*x
print(b(3))
print(b(6))

print(" ")
# The pass Statement
# Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def c():
    pass

print(" ")
# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def d(x, /):
    print(x)
d(3)
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def d1(x):
    print(x)
d1(3)
# But when adding the , / you will get an error if you try to send a keyword argument:
# def d1(x, /):
#     print(x)
# d1(x = 3)
print(" ")
# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
def e(*, x):
    print(x)
e(x = 3)
# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:
def e1(x):
    print(x)
e1(x = 3)
# But with the *, you will get an error if you try to send a positional argument:
# def e2(*, x):
#     print(x)
# e2(3)
print(" ")
# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def f(a, b, /, *, c, d):
    print(a + b + c + d)
f(5, 6 ,c = 7, d = 8)

print(" ")
# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Results:")
tri_recursion(6)