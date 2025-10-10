# 10. Write a Python program to convert a given camel case string to snake case.

import re

def func():
    text = input()
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    print(result)
func()