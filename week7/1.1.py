# Python builtin functions exercises
# 1. Write a Python program with builtin function to multiply all the numbers in a list

from functools import reduce
numbers = list(map(int, input().split()))
result = reduce(lambda x, y: x * y, numbers)
print(result)