
"""
Chapter 7, Exercise 4: Large Shirts ☑️

Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.

"""

def make_shirt(size='large', message='I Love Python'):
    "Summarize the shirt that's going to be made."
    print(f"\n I'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')
    
make_shirt()
make_shirt(size='small')
make_shirt('medium','Python is very interesting.')


