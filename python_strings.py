# Assign String to a Variable

a = "Hello"
print(a)

# Assign Multi-line string

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# or

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

"""
strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

a = "Hello, World!"
print(a[1])

# we can loop through the characters in a string, with a for loop

for x in "banana":
  print(x)


# check string length
a = "Hello, World!"
print(len(a))  

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

## Slicing string ##
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

## Modify String ##
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = " Hello, World! "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(","))

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
'''
F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
'''

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)

'''
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
'''
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Character
''' 
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''