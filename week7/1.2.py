# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

text = input()
upper = sum(1 for char in text if char.isupper())
lower = sum(1 for char in text if char.islower())
print(upper)
print(lower)