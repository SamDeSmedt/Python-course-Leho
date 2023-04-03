#!/usr/bin/python3
# Script that takes the odd numbers from a given list and put it in a new list
# Using a comprehension

M = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a range of the amount of numbers
rangeM = list(range(0,len(M),1))
#print(lenM)

# Iterate over each number to check if it is odd
# If the number is odd add it to the list
numOdd = [M[i] for i in rangeM if M[i] %2 == 0]
print("The old list with numbers is: {}\n"
      "The new list with odd numbers is: {}".format(M, numOdd))
