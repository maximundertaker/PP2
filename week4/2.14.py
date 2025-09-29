#14. Import and Use Functions
# Create a python file and import some of the functions from the above 13 tasks and try to use them.

from atotal2 import *
print(f"{grams} grams = {grams_to_ounces(grams)} ounces")

print(f"{f}°F = {f_to_c(f):.2f}°C")

print(solve(35, 94))

print(filter_prime(numbers))

print_permutations(a)

print(reverse_w(a))

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1]))

print(game([1, 2, 4, 0, 0, 7, 5]))
print(game([1, 0, 2, 4, 0, 5, 7]))
print(game([1, 7, 2, 0, 4, 5, 0]))

print(f"Volume: {sphere(r):.2f}")

print(unique(numbers))

print(f"Is palindrome: {is_palindrome(a)}")

histogram([4, 9, 7])