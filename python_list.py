'''
List
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
'''

mylist = ["apple", "banana", "cherry"]
print(mylist)

'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

# Access list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#his example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Change or edit list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# change or range of list values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

'''
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

###------  Add List Items -------###
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

''' 
Extend List
To append elements from another list to the current list, use the extend() method.
'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

'''
Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

'''

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

### -------- Remove Specified Item ----------- ###
# The remove() method removes the specified item.

#thislist = ["apple", "banana", "cherry"]
thislist.remove("rock")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.

#thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#The del keyword also removes the specified index:
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
del thislist

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

## ----- Loop list ------ ##
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

'''
Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
'''

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

'''
Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, 
then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
'''

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# ---------------------------------------------------------------------------------------

# ------------ Very IMP below ----------------#
# List Comprehension
'''
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits]
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
# he expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".


print(newlist)

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Use the copy() method
# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
mylist = list(thislist)
print(mylist)

# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# --------- Join List -------- #

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)