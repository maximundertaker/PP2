# 7. Write a python program to convert snake case string to camel case string.

import re

def func():
    text = input()
    words = text.split('_')
    if len(words) > 1:
        result = words[0] + ''.join(word.capitalize() for word in words[1:])
        print(result)
    else:
        print("Invalid snake case format")
    print(" ")
    result_regex = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)
    print(result_regex)

func()