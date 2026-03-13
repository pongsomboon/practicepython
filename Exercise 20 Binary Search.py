# Write a function that takes an ordered list of numbers (a list where the elements are in
# order from smallest to largest) and another number. The function decides whether or not the given number is inside the list.
# Extras:
#     Use binary search.

from random import randint

randlist = [randint(0,100) for x in range(randint(10, 20))]
randlist.sort()
print(randlist)

given = int(input("Enter a number."))

def search(lst, target):
    for index, num in enumerate(lst):
        if num == target:
            print (f"Found {target} at position {index + 1}")
            return
    print("Not found.")

search(randlist, given)

def binsearch(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            print (f"Found {target} at position {mid + 1}.")
            return
        elif lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
    print("Not found.")

binsearch(randlist, given)



