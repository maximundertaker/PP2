# 8. Write a Python program to split a string at uppercase letters.

import re

def func():
    text = input()
    parts = re.findall(r'[A-Z][^A-Z]*', text)
    if parts:
        print(parts)
    else:
        print("There are no uppercase letters to split")
func()