# 2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os
path = input()
print(os.path.exists(path))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))