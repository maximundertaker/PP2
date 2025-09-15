#Format Strings

'''age = 36
txt = "My name is John, I am " + age
print(txt)'''
#it will show u an error

#F-string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

print(" ")

#Placeholders & Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

print(" ")

#a placeholder can include a modifier to format the value. a modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
price = 59
txt3 = f"The price is {price:.2f} dollars"
print(txt3)

print(" ")

#a math operation
txt = f"The price is {20 * 59} dollars"
print(txt)