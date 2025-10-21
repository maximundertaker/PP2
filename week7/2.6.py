# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as file:
        file.write(letter)