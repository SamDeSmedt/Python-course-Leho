#!/usr/bin/python3

# Create a list with 2 values
charged = ["Arg", "Lys"]
print("The original list: {}".format(charged))

# Create a second list with different values
charged2 = ["Asp", "Glu"]
print("The second list: {}".format(charged2))

# Use the list.extend() function to combine the lists
# Note that this changes the values of the original charged variable
charged.extend(charged2)
print("The combined list: {}".format(charged))
