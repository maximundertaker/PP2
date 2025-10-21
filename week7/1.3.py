# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.

text = input()
cleaned = ''.join(filter(str.isalnum, text)).lower()
print(cleaned == cleaned[::-1])