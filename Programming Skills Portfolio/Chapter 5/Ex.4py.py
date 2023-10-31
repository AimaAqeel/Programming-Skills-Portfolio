
"""
Chapter 5, Exercise 4: Rivers ☑️

Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.


"""

rivers={
        'nile':'egypt',
        'amazon':'brzail',
        'mississippi':'united ststes',
        'Yenisey':'Russia',
        'yangtze':'china',
        }

for river, country in rivers.items():
    print(f"the{river.title()}flos through{country.title()}.")
    
    print("\nthe following countries are in clude in this data set:")
    for country in rivers.values():
        print(F"-{country.title()}")
        
    print("\nthe following rivers are in clude in this data set:")
    for river in rivers.keys():
            print(F"-{river.title()}")
        
