# Set Items - Data Types
# Set items can be of any data type:
# Example
# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

print(" ")
# A set can contain different data types:
# Example
# A set with strings, integers and boolean values:
set4 = {"abc", 34, True, 40, "male"}
print(set4)

print(" ")
# type()
# From Python's perspective, sets are defined as objects with the data type 'set':
# <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))

print(" ")
# The set() Constructor
# It is also possible to use the set() constructor to make a set.
# Example
# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.