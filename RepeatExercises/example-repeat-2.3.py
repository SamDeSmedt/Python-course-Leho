#!/usr/bin/python3
################################################################################
# Lists
################################################################################

# Create list named charged with elements "Arg" and "Lys"
charged = ["Arg","Lys"]

# Print the unchanged list
print("The unchanged list charged: {}".format(charged))

# Extend the list with elements "Asp" and "Glu"
charged.extend(["Asp","Glu"])

# Print the extended list
print("The extended list charged: {}".format(charged))
