#!/usr/bin/python3
# Python program to find the area of a traingle

# Define parameters
a = 18
b = 12
c = 10
'''
# Code not using the math module
# Ask for variable input
a = input("a: ")
b = input ("b: ")
c = input ("c: ")

# Semiparameters calculations
s = (a + b + c)/2

# Area A calculation
A = (s*(s-a)*(s-b)*(s-c)) ** 0.5
'''
# Code uses the math module
import math

# Calculations
s = (a + b + c)/2
A = (s*(s-a)*(s-b)*(s-c))
A = math.sqrt(A)

# Print the output
print("The semiparameters is: {} cm\n"
      "The Area is: {} cm²".format(s, A))

#Show only two decimals
print("="*40)
print("semiparameter s = {0: .2f}".format(s))
print("Area triangle A = {0: .2f}".format(A))
print("="*40)
print(" Area of triangle A is %0.2f" %A)