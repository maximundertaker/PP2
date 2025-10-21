# 4. Write a Python program to count the number of lines in a text file.

filename = input()
with open(filename, 'r') as file:
    print(sum(1 for line in file))