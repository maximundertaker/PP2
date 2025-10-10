# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

def func():
    text = input()
    pattern = r'a.*b$'
    if re.search(pattern, text):
        print(f"Yes, {text} matches the pattern")
    else:
        print(f"No, {text} does not match the pattern")
func()