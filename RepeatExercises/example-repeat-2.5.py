#!/usr/bin/python3
################################################################################
# Operators
################################################################################
# Script to calculate the area of a triangle
# using Heron's formula
import math

#a = 18
a = int(input("Give the length of side a: "))
#b = 12
b = int(input("Give the length of side b: "))
#c = 10
c = int(input("Give the length of side c: "))

# Calculate the semiperimeter s
s = (a+b+c)/2

# Calculate area A
A = math.sqrt(s*(s-a)*(s-b)*(s-c))
A = round(A,2)

print("Trangle having side lengths: \na = {}\nb = {}\nc = {}".format(a,b,c))
print("Semiperimeter s: {}\narea A: {}".format(s,A))