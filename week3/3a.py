# Python - Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print(" ")

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
thislist1 = ["apple", "banana", "cherry"]
print(thislist1[-1])

print(" ")

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[:4])

thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
thislist6 = ["apple", "banana", "cherry"]
if "apple" in thislist6:
  print("Yes, 'apple' is in the fruits list")