#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
# number, then tell them whether they guessed too low, too high, or exactly right. (Hint:
# remember to use the user input lessons from the very first exercise)

import random
import sys

count = 1
number = random.randint(1,9)
guess = input("Guess a random number from 1 to 9. Type 'exit' to quit.")
while True:
    try:
        int(guess)
    except ValueError:
        if guess != 'exit':
            guess = input("Guess a random number from 1 to 9. Type 'exit' to quit.")
        else:
            sys.exit()
    else:
        break

guess = int(guess)
while guess != number:
    if guess > number:
        guess = int(input("Too high, try again."))
        count += 1
    elif guess < number:
        guess = int(input("Too low, try again."))
        count += 1
else:
    print(f"Correct. It took you {count} tries.")