# Data Types
# Data type specifies the type of value a variable requires to do various operations without causing an error. By default, Python provides the following built-in data types:

# Numeric data: int, float, complex


icecream = "Vanilla"    # global variable
def foods():
    vegetable = "Potato"    # local variable
    fruit = "Lichi"         # local variable
    print(vegetable + " is a local variable value.")

foods()
print(icecream + " is a global variable value.")
#print(fruit + " is a local variable value.")  # This line would cause an error


# Sequenced data: list, tuple, range
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

#tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and cannot be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

#range: Returns a sequence of numbers as specified by the user. If not specified by the user, it starts from 0 by default and increments by 1.
sequence1 = range(4, 14, 2)
for i in sequence1:
    print(i)

#Mapped data: dict
#dict: A dictionary is an unordered collection of data containing a key:value pair. The key-value pairs are enclosed within curly brackets.
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)

# Set data:
# Set is an unordered collection of elements in which no element is repeated. The elements of sets are separated by a comma and contained within curly braces.
set1 = {4, -4, -5, 8, 3, 2.9}
print(set1)


# Mutable Data Types
# Mutable means changeable. If a data type is mutable, it means you can add, remove, or modify its elements without creating a new object in memory. When you change a mutable object, its memory address (ID) stays the same.
# Common mutable data types:
# list
# dict
# set
# bytearray
# Example of a mutable data type (list)
fruits = ["apple", "banana", "cherry"]
print(id(fruits))  # Memory address before modification

fruits.append("mango")  # Adding a new item
print(fruits)
print(id(fruits))  # Same memory address → same object

# Immutable Data Types
# Immutable means unchangeable. If a data type is immutable, it means its value cannot be changed once created. If you try to modify it, Python will create a new object instead of changing the existing one. As a result, its memory address (ID) changes.

# Common immutable data types:

# int
# float
# complex
# str
# tuple
# bool
# bytes
# Example of an immutable data type (string)
name = "Harry"
print(id(name))  # Memory address before modification

name = " Potter"  # Concatenating creates a new string
print(name)
print(id(name))  # Different memory address → new object created

str1 = "7"          
str2 = "3.142"
str3 = "13"
num1 = 29
num2 = 6.67

print(type(int(str1)))
print(float(str2))
print(float(str3))
print(str(num1))
print(str(num2))

# Operation on Strings
# Length of a String:
# We can find the length of a string using the len() function.

# Example:

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# String as an Array:
# A string is essentially a sequence of characters and can be accessed like an array, although it is not technically one. Thus, we can access the elements of this array.

# Example:

pie = "ApplePie"
print(pie[2:5])
print(pie[6])  # returns character at specified index


print(pie[:5])      # Slicing from Start
print(pie[5:])      # Slicing till End
print(pie[2:6])     # Slicing in between
print(pie[-8:-3])      # Slicing using negative index


# Loop through a String:
# Strings are arrays, and arrays are iterable. Thus, we can loop through strings.

# Example:

alphabets = "ABCDE"
for i in alphabets:
    print(i)

#     String Methods
# Python provides a set of built-in methods that we can use to modify and manipulate strings.

# upper():
# The upper() method converts a string to upper case.

# Example:

str1 = "AbcDEfghIJ"
print(str1.upper())

# lower():
# The lower() method converts a string to lower case.

# Example:

str1 = "AbcDEfghIJ"
print(str1.lower())

# strip():
# The strip() method removes any white spaces before and after the string.

# Example:

str2 = " Silver Spoon "
print(str2.strip())

# rstrip():
# The rstrip() method removes specified trailing characters (defaults to whitespace).

# Example:

str3 = "Hello !!!"
print(str3.rstrip("!"))

# replace():
# The replace() method replaces a string with another string.

# Example:

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

# split():
# The split() method splits the given string at the specified instance and returns the separated strings as list items.

# Example:

str2 = "Silver Spoon Hello"
print(str2.split(" "))  # Splits the string at the whitespace " ".

# capitalize():
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

# Example:

str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)