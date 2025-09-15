#Strings

print("Hello")
print('Hello')

#Quotes inside quotes
print("It's alright")
print('My name is Maxim')

#Assign string to a variable
a = "Hello"
print(a)

a = 'hello'
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#In the result, the line breaks are inserted at the same position as in the code

print(" ")

#Strings are arrays
a = "Hello, World!"
print(a[0])

print(" ")

#Looping through a string
for x in "banana":
    print(x)

print(" ")

#String length
a = "Hello, World!"
print(len(a))

b = "Hello "
print(len(b))

print(" ")

#Check String
txt = "the best things in life are free!"
print("free" in txt)

print(" ")

#If - statement
txt = "the best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

print(" ")

#If not - statement
txt = "the best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")