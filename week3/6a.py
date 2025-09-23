# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example
# Get the value of the "model" key:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict["model"]
print(x)
print(type(x))

print(" ")
# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)

print(" ")
# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Example
# Get a list of the keys:
x = thisdict.keys()
print(x)

print(" ")
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

print(" ")
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)

print(" ")
# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

print(" ")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

print(" ")
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()

print(" ")
# Example
# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

print(" ")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

print(" ")
# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# Example
# Check if "model" is present in the dictionary:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")