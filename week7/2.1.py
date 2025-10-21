# Python Directories and Files exercises
# 1. Write a Python program to list only directories, files and all directories, files in a specified path.

import os
path = input()
print("Directories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)
print("Files:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)