#!/usr/bin/python3
seq = "MNKMDLVADVAEKTDLSKAKATEVIDAVFA"

# Display hardcoded sequence
print("The default sequence is: {}".format(seq))

# Perform slicing operation on the sequence
# Show the characters with offset 3 each time
slice1 = seq[0:9:3]
print("Slicing the sequence with code seq[0:9:3] result in: {}".format(slice1))
# 
slice2 = seq[16:0:-4]
print("Slicing the sequence with code seq[16:0:-4] result in: {}".format(slice2))
slice3 = seq[:25:-1]
print("Slicing the sequence with code seq[:25:-1] result in: {}".format(slice3))
