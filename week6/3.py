# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

def func():
    text = input()
    pattern = r'[a-z]+_[a-z]+'
    matches = re.findall(pattern, text)
    if matches:
        print(f"There are sequences: {matches}")
    else:
        print(f"There are no sequences.")
func()