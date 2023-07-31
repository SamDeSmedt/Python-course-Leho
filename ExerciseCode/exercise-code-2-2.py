#!/usr/bin/python3
seq = "MNKMDLVADVAEKTDLSKAKATEVIDAVFA"

# Display hardcoded sequence
print("The default sequence is: {}\nwith length: {}".format(seq, len(seq)))

# Perform slicing operation on the sequence

# The third number indicates the characters to skip
# Also known as step
# Example takes first, fourth and seventh character
slice1 = seq[0:9:3] # output: MVV
print("Slicing the sequence with code seq[0:9:3] result in: {}".format(slice1))
slice2 = seq[16:0:-4] #output: SKDD
print("Slicing the sequence with code seq[16:0:-4] result in: {}".format(slice2))
slice3 = seq[:25:-1] #output: AFVA
print("Slicing the sequence with code seq[:25:-1] result in: {}".format(slice3))
