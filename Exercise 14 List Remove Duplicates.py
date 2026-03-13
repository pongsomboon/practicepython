# Write a program (function!) that takes a list and returns a new list that contains all
# the elements of the first list minus all the duplicates.
# Extras:
#     Write two different functions to do this - one using a loop and constructing a list,
#     and another using sets.

import random

lst = list(random.randint(1, 10) for x in range(random.randint(5,10)))

print(lst)

def setdupe(a):
    return list(set(a))

def loopdupe(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b

print(setdupe(lst))
print(loopdupe(lst))