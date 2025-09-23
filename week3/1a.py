class myclass():
    def _len_(self):
        return 0

myobj = myclass()
print(bool(myobj))

print(" ")

#Functions can Return a Boolean
def myFunction():
    return True
print(myFunction())

print(" ")

def myFunction():
    return True
if myFunction():
    print("Yes!")
else:
    print("No!")

print(" ")

x = 200
print(isinstance(x, int))