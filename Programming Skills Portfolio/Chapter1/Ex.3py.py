
"""

Chapter 1, Exercise 3: Print date and Time ☑️

Write a Python program to display the current date and time.

"""

# The current date and time is important into the code and is printed as output.
import datetime
now=datetime.datetime.now()
print("Date and Time now:")
print(now.strftime ("%Y-%m-%d:%H:%M:%S:"))