# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Example
# Create a dictionary that contain three dictionaries:
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}   
# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Example
# Print the name of child 2:
print(myfamily["child2"]["name"])

print(" ")
# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this:
# Example
# Loop through the keys and values of all nested dictionaries:
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])