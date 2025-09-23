# Python - Remove Set Items
# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# Example
# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

print(" ")
# Note: If the item to remove does not exist, remove() will raise an error.

# Example
# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

print(" ")
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

# Example
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

print(" ")
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Example
# The clear() method empties the set:
thisset1 = {"apple", "banana", "cherry"}
thisset1.clear()
print(thisset1)

print(" ")

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)