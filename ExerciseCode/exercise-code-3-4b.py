#!/usr/bin/python3
# script to creat an arrow to the right
'''
base = int(input("Choose the amount of start: "))

n = list(range(1,(base + 1)))

for i in n:
    print("* "*i)

for i in n:
    print("* "*(base - i))
'''
################################################################
# Using a nested loop

n = 5
for i in range(n):
    #print("i = {}".format(i))
    for j in range(i):
        print("* ", end=" ")
    #print a newline
    print(" ")

for i in range(n,0,-1):
    #print("i = {}".format(i))S
    for j in range(i):
        print("* ", end=" ")
    #print a newline
    print(" ")