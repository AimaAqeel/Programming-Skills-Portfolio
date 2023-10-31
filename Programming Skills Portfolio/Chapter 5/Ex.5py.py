
"""

Chapter 5, Exercise 5: Pets ☑️

Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet


"""

#make an empty list t store the pets in.
pets={}

#make individual pets, and store each one in the list.
pets={
      'type of animal':'wolf',
      'name':'hunti',
      'owner':'Aims',
      'weight':'35',
      'eats':'meat',
      }
pets.append(pets),

pet={
     'type of animal':'cat',
     'name':'kitti',
     'owner':'mano',
     'weight':'3',
     'eats':'Cooked beef',
     }
pets.append(pets),

#display information about each pet.
for pet in pets:
    print(f"\n here's what I know about{pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}:{value}")
        
