# 5. Write a Python program with builtin function that returns True if all elements of the tuple are true.

data = input().split()
tup = tuple(bool(x) for x in data)
print(all(tup))