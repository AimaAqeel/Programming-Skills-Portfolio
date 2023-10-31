
"""


Chapter 7, Exercise 3: T-Shirt ☑️

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.


"""

def make_shirt(size, message):
    "Summarize the shirt that's going to be made."
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say "{message}"')
    
make_shirt('small','Tom and Jerry!')
make_shirt(message="Hard Times.",size='medium')
