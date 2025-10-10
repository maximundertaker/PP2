# 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

def func():
    text = input()
    pattern = r'ab{2,3}'
    if re.search(pattern, text):
        print(f"Yes, {text} matches the pattern")
    else:
        print(f"No, {text} does not match the pattern")

func()