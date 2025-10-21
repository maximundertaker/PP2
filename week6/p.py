import re
def func():
    text = input()
    pattern = r'(?<!^)([A-Z])'
    result = re.sub(pattern, "_", text)
    print(result)
func()