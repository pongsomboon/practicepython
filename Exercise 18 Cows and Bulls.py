# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a “cow”. For every
# digit the user guessed correctly in the wrong place is a “bull.” Every time the user
# makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over. Keep track of the number of guesses the user makes
# throughout the game and tell the user at the end.

from random import randint

def game():
    number = str(randint(1000, 9999))
    guess = input("Guess a 4 digit number.")
    while int(guess) != int(number):
        cows = 0
        bulls = 0
        splitnum = [x for x in number]
        splitguess = [x for x in guess]
        for x in enumerate(splitnum):
            if x in enumerate(splitguess):
                cows += 1
            else:
                bulls += 1
        print(f"You have {cows} cow(s) and {bulls} bull(s).")
        guess = input("Guess the number again.")
    else:
        print(f"Correct. The number was {number}.")

game()
