# Squares in Range
# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2
for sq in squares(1, 5):
    print(sq)