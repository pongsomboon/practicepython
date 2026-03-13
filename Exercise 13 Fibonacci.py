#Write a program that asks the user how many Fibonacci numbers to generate and then generates
# them. Take this opportunity to think about how you can use functions. Make sure to ask the user
# to enter the number of numbers in the sequence to generate.(Hint: The Fibonacci sequence is a
# sequence of numbers where the next number in the sequence is the sum of the previous two numbers
# in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

times = int(input("How many numbers of the Fibonacci sequence would you like to generate?"))
lst = [1]
count = 0
a = 1
b = 1
    while count <= times - 1:
        var = a
        a = a + b
        b = var
        lst.append(var)
        count += 1

print(lst)