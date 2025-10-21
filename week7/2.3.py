# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os
path = input()
if os.path.exists(path):
    print(os.path.dirname(path))
    print(os.path.basename(path))
else:
    print("Path does not exist")