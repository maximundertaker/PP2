# Python iterators and generators
# Squares Generator
# Create a generator that generates the squares of numbers up to some number N.

def squares_up_to(n):
    for i in range(n + 1):
        yield i ** 2

for sq in squares_up_to(5):
    print(sq)