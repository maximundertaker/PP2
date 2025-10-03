# Divisible by 3 & 4
# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divide(n):
    for i in range(n+1):
        if i % 12 == 0:
            yield i
for num in divide(50):
    print(num)