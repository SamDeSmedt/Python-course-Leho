#!/usr/bin/python3
# Script to get a Fibonacci series between 0 to 50

x = 0
y = 1
z = 0

end = int(input("Provide a number for the Fibonacci series to end: "))
while x < end:
    print("{} + {} = {}".format(x,y,z))
    
    #update variables
    x = y
    y = z
    z = x + y
    