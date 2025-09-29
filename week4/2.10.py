#10. Unique Elements
# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
numbers = [1, 2, 2, 3, 4, 4, 5]
print(unique(numbers))