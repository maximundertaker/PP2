#11. Palindrome Check
# Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
a = input()
print(f"Is palindrome: {is_palindrome(a)}")