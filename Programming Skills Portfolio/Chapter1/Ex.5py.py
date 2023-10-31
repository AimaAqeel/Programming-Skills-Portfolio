# -*- coding: utf-8 -*-
"""
Chapter 1, Exercise 5: Compute area of Circle ☑️

Write a Python program which accepts the radius of a circle from the user and compute the area.


"""

from math import pi 
# The value of pi is imported to the program to be used in the area of the circle
r=float(input("input radius of a circle"))
#The variable r is used to store input (radius of circle)
print("The area of the circle with radius",str(r), "is:", str(pi*r**2))
#The area is then calculated and printed as output
