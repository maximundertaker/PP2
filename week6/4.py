# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

def func():
    text = input()
    pattern = r'[A-z][a-z]+'
    matches = re.findall(pattern, text)
    if matches:
        print(f"There are sequences: {matches}")
    else:
        print(f"There are no sequences")
func()