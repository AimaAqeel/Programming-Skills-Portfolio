
"""

Chapter 6, Exercise 2: Movie Tickets: ☑️

A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket.


"""

prompt="Movie Tickets"
prompt+="\n enter'quit'when you are finished."

while True:
    age=input(prompt)
    if age =='quit':
        break
        age=int(age)
        
        if age<3:
            print("you get is free")
        elif age<13:
            print("your ticket is $10.")
        else:
            print("your ticket is $15.")