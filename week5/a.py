import math

def square(x):
    return math.pow(x, 2)

def square_iter(numbers):
    for x in numbers:
        yield x ** 2

numbers = [int(x) for x in input().split()]

for num in numbers:
    print(int(square(num)))

for squared in square_iter(numbers):
    print(squared)

print(" ")

import datetime
x = datetime.datetime(1941, 5, 23)
print(x.strftime("%C"))