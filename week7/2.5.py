# 5. Write a Python program to write a list to a file.

filename = input()
data = input().split()
with open(filename, 'w') as file:
    for item in data:
        file.write(item + '\n')