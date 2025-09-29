#5. String Permutations
# Write a function that accepts string from user and print all permutations of that string.

def print_permutations(s):
    from itertools import permutations
    for  p in permutations(s):
        print(''.join(p))
a = input()
print_permutations(a)