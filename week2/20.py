#Modify Strings
a = "Hello, World!"
print(a.upper())

#Lower Strings
a = "Hello, WORLD!"
print(a.lower())

#Remove Whitespace
a = "    Hello, World! "
print(a.strip())

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.replace("H", a[4]), a.replace("l", a[0]))

#Split String
a = "Hello, World!"
print(a.split(","))