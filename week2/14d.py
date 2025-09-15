x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

#it shows that the Global Keyboard has a huger priority than a simple x