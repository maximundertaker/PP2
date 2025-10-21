# 7. Write a Python program to copy the contents of a file to another file

source = input()
dest = input()
with open(source, 'r') as src:
    content = src.read()
with open(dest, 'w') as dst:
    dst.write(content)