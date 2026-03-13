# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last elements of the given list. For practice,
# write this code inside a function.

import random

lst = [random.randint(1,10) for i in range(random.randint(5,10))]
print(f"Here is a random list: {lst}.")
def lstends(a):
    """This function creates a new list from the initial list's first and last elements."""
    b = [x for i,x in enumerate(a) if i == 0 or i == len(a) - 1]
    return b

print(f"Here is a new list that only contains the first and last elements: {lstends(lst)}")

