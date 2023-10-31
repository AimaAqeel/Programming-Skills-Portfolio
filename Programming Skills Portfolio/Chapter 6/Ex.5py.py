
"""

Chapter 6, Exercise 5: No Pastrami ☑️

Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.


"""

sandwich_orders={
    'pastrami','club','veggie','chicken','pastrami','turkey','beef','champ','pastrami',
    }
finished_sandwiches={}

print("I'm sorry, we're all out of pastrami tody.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
    print("\n")
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"I'm working on your {current_sandwich} sandwich.")
        finished_sandwiches.append (current_sandwich)
        
        print("\n")
        for sandwich in finished_sandwiches:
            print(f"I made a {sandwich} sandwich.")
            
           