# import re
# def func():
#     text = input()
#     pattern = r'[a-z]+_[a-z]+'
#     matches = re.findall(pattern, text)
#     print(matches)
# func()

# import re
# def func():
#     text = input()
#     pattern = r'[A-Z][a-z]+'
#     matches = re.findall(pattern, text)
#     print(matches)
# func()

# import re
# def func():
#     text = input()
#     pattern = r'a.*b$'
#     if re.search(pattern, text):
#         print(f'Yes, {text} matches the pattern')
#     else:
#         print(f'No, {text} does not match the pattern')
# func()

# import re
# def func():
#     text = input()
#     pattern = r'[ ,.]'
#     replace = re.sub(pattern, ":", text)
#     print(replace)
# func()

# import re
# def func():
#     text = input()
#     words = text.split('_')
#     result = words[0] + ''.join(word.capitalize() for word in words[1:])
#     print(result)
# func()

# import re
# def func():
#     text = input()
#     pattern = r'[A-Z][a-z]*'
#     parts = re.findall(pattern, text)
#     print(parts)
# func()

# import re
# def func():
#     text = input()
#     pattern = r'([a-z])([A-Z])'
#     result = re.sub(pattern, r'\1 \2', text)
#     print(result)
# func()

# import re
# def func():
#     text = input()
#     pattern = r'(?<!^)(?=[A-Z])'
#     result = re.sub(pattern, "_", text).lower()
#     print(result)
# func()

import re
def func():
    text = input()
    pattern = r'he.{2}b$'
    if re.search(pattern, text):
        print(f'Yes, {text} matches')
    else:
        print(f'No, {text} does not match')
func()