#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

print(" ")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(" ")

#Evaluate values and variables
print(bool("Hello"))
print(bool(15))

print(" ")

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(" ")
#Most values are True
##Almost any value is evaluated to True if it has some sort of content.
##Any string is True, except empty strings.
##Any number is True, except 0.
##Any list, tuple, set, and dictionary are True, except empty ones.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

print(" ")

#Some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})