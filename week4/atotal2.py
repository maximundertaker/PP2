def grams_to_ounces(grams):
    return grams * 28.3495231

grams = int(input())
print(f"{grams} grams = {grams_to_ounces(grams)} ounces")

def f_to_c(f):
    return (5 / 9) * (f - 32)

f = int(input())
print(f"{f}°F = {f_to_c(f):.2f}°C")

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No solution"
print(solve(35, 94))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))

def print_permutations(s):
    from itertools import permutations
    for  p in permutations(s):
        print(''.join(p))
a = input()
print_permutations(a)

def reverse_w(s):
    words = s.split()
    return ' '.join(words[::-1])
a = input()
print(reverse_w(a))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1]))

def game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False
print(game([1, 2, 4, 0, 0, 7, 5]))
print(game([1, 0, 2, 4, 0, 5, 7]))
print(game([1, 7, 2, 0, 4, 5, 0]))

def sphere(radius):
    return (4/3) * 3.14 * radius ** 3
r = int(input())
print(f"Volume: {sphere(r):.2f}")

def unique(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
numbers = [1, 2, 2, 3, 4, 4, 5]
print(unique(numbers))

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
a = input()
print(f"Is palindrome: {is_palindrome(a)}")

def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram([4, 9, 7])

#def guess():
#    name = input("Hello! What is your name? ")
#    number = random.randint(1, 20)
#    guesses = 0
#
#    print(f"Well, {name}, I'm thinking of a number between 1 and 20.")
#    while True:
#        guess = int(input("Take a guess: "))
#        guesses += 1
#
#        if guess < number:
#            print("Your guess is too low.")
#        elif guess > number:
#            print("Your guess is too high.")
#        else:
#            print(f"Good job, {name}! You guessed in {guesses} guesses")
#            break
#guess()