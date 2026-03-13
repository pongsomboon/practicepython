# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and
# symbols. The passwords should be random, generating a new password every time the
# user asks for a new password. Include your run-time code in a main method.

# Extra: Ask the user how strong they want their password to be. For weak passwords,
# pick a word or two from a list.

import random
import string
symbols = '!@#$%^&*()_-+='

author = 'Nightjar'
print(f"Password Generator by {author}.")

def main():
    pw = []
    length = int(input("How many characters would you like your password to be?"))
    strength = input("Would you like a weak or strong password?")
    for x in range(0, length):
        if strength == 'strong':
            char = random.choice([1,2,3])
        else:
            char = random.choice([1,2])
        if char == 1:
            pw.append(str(random.choice(string.digits)))
        elif char == 2:
            pw.append(str(random.choice(string.ascii_letters)))
        elif char == 3:
            pw.append(str(random.choice(symbols)))
    print(''.join(pw))
main()
