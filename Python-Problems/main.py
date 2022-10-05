# First app in python
from cgi import print_exception
from tkinter import Y
from turtle import width
from unicodedata import name
from urllib import response


print("Hello, World")

# declaring a variable
name = 'Steve' # You can change your name here to whatever you want
response = True
print("Hello " + name + "," +  " How are you today?")
if(response == True):
    print("I'm fine thank you!")

# Conditional if statement
the_world_is_flat = True
if(the_world_is_flat):
    print("Be careful not to fall of")

"""
Numbers and arithmetic operations
Int => 1, 2, 3, 9, 100 ....
Float => 1.2, 2.5, 9.1, 11.05 
Complex => Syntax: X + Yj
"""

# Numbers, height and width variables
width = 15
height = 2 * 5 # value is equal to the result of multiplying two by five
print(height * width)
# When height is multiplayed to width and devided by 5 it will print a new result
if(height * width):
    print(height * width / 5)


# Numbers and division type
chair = 1500
table = 200
print(chair // table) # result will be an Integer number

# We use single slash to get a float number
if(chair / table == 7.5):
    print("This is a float number")

# We use the double slash to get an integer number
if(chair // table == 7):
    print("This is an Integer number")
