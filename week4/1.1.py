#1. String class
# Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class string:
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())

obj = string()
obj.getString()
obj.printString()