# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity
# to practice using functions, described below.
a = []
def prime(number):
    for x in range(1, int(number) + 1):
        if int(number) % x == 0:
            a.append(x)
    if len(a) == 1 or len(a) == 2:
        return "Prime"
    else:
        return "Not Prime"

number = int(input("Enter a whole number."))
print(prime(number))
print(a)