#13. Guess the Number Game
# Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
# Hello! What is your name?
# KBTU
# Well, KBTU, I am thinking of a number between 1 and 20.
# Take a guess.
# 12
# Your guess is too low.
# Take a guess.
# 16
# Your guess is too low.
# Take a guess.
# 19
# Good job, KBTU! You guessed my number in 3 guesses!

import random

def guess():
    name = input("Hello! What is your name? ")
    number = random.randint(1, 20)
    guesses = 0

    print(f"Well, {name}, I'm thinking of a number between 1 and 20.")
    while True:
        guess = int(input("Take a guess: "))
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed in {guesses} guesses")
            break
guess()