#Python Lists

# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
mylist = ["apple", "banana", "cherry"]
print(mylist)

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print(" ")

# List length
alist = ["apple", "banana", "cherry"]
print(len(alist))

print(" ")

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

print(" ")

list4 = ["abc", 34, True, 40, "male"]
print(list4)

print(" ")

# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))  #<class 'list'>

print(" ")

# The list() constructor
thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist1)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# - List is a collection which is ordered and changeable. Allows duplicate members.
# - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# - Dictionary is a collection which is ordered** and changeable. No duplicate members.