# print msg
print ("Hello world!")

# Declare variable
x = 5
X = "Rambo"

print (X)
print (x)

# best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)



# declare and datatype conversion 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

print(type(x))
print(type(y))

""" Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions
"""
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	


# Convert from one datatype to another :
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Below multi line commenting
""" If you have a collection of values in a list, tuple etc.
 Python allows you to extract the values into variables. This is called unpacking """

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

##-----Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:----##

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

"""Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables."""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

""" The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""
# Global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)