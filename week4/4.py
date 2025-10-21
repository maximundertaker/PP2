def function(s):
    vowels = "aeiouAEIOU"
    count = 0
    for w in s:
        if w in vowels:
            count += 1
    return count

s = input()
print(function(s))