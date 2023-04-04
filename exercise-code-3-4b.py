#!/usr/bin/python3
# script to creat an arrow to the right

base = int(input("Choose the amount of start: "))

n = list(range(1,(base + 1)))

for itervar in n:
    print("* "*itervar)

for itervar in n:
    print("* "*(base - itervar))