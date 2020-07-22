# PROGRAMMING ASSIGNMENT 04
# Filename: 'exercise1.py'
#
# Write a program which asks the user to enter a positive integer N and then
# draws an hourglass of the corresponding size (2 * N - 1 lines).
# The hourglass is obtained by drawing lines containing spaces ' ' and stars '*'.
#
# see the sample examples in the pdf file
#
# NOTE: you MUST use a for loop for this exercise
#
# WRITE YOUR CODE AFTER THIS LINE

n = int(input("Enter a positive integer: ")) # receive user input

# mininum of (2n - 1) - (i + 1) and i for the amount of space
# maximum of (2n - 1) - 2i and 2(i + 1) - (2n - 1) for the amount of stars

for i in range(2 * n - 1): # number of lines
    print(" " * min((2 * n - 1) - (i + 1), i) + '*' * max((2 * n - 1) - (2 * i), 2 * (i + 1) - (2 * n - 1)) + " " * min((2 * n - 1) - (i + 1), i))
