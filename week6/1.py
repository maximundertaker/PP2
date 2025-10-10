# Python RegEx
# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

def func():
    text = input()
    pattern = r'ab*'
    if re.search(pattern, text):
        print(f"Yes, {text} matches the pattern")
    else:
        print(f"No, {text} does not match the pattern")
func()