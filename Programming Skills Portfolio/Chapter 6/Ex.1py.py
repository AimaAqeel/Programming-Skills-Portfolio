
"""

Chapter 6, Exercise 1: Pizza Toppings ☑️
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.

"""

prompt="\nwhat topping would you like on your pizza?"
prompt+="\nenter'quit when you are finished:"

while True:
    topping=input(prompt)
    if topping!='quit':
        print(" I'll add{topping} to your pizza.")
    else:
        break