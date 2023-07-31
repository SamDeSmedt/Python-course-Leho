#!/usr/bin/python3
# Script to the largest number from a script

list = [2, 28, 11, 7, 40, 15]
'''
nLarge = 0

if nLarge == 0:
    print("Before: None\n" + "-"*20)
else:
    print("Before: {}\n".format(nLarge) + "-"*20)
'''
nLarge = None

print("Before: {}".format(nLarge))

for itervar in list:
    if nLarge is None or itervar > nLarge:
        nLarge = itervar
        print("Loop:\t{}\t{}".format(itervar,nLarge))
    else:
        print("Loop:\t{}\t{}".format(itervar,nLarge))

print("-"*20 + "\nLargest: {}".format(nLarge))