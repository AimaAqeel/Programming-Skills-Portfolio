
"""

Chapter 3, Exercise 5: Change Guest List ☑️

You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.


"""

#invitation some people to dinner.
guests=['noor', 'mubarka','maida']

name=guests[0].title()
print(f"{name}, please come to dinner.")

name=guests[1].title()
print(f"{name}, please come to dinner.")


name=guests[2].title()
print(f"{name}, please come to dinner.")

name=guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

#mubarka can't make it! Let's invite saher intead.
del(guests[1])
guests.insert(1, 'saher')

#print the invitation again.
name=guests[0].title()
print(f"\n{name}, please come to dinner.")

name=guests[1].title()
print(f"\n{name}, please come to dinner.")

name=guests[2].title()
print(f"\n{name}, please come to dinner.")
