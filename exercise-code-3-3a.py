#!/usr/bin/python3
# Script to get a Fibonacci series between 0 to 50

x = 0
y = 1
z = 0

while z < 50:
    print(z)
    z = x + y
    x = y
    y = z
    