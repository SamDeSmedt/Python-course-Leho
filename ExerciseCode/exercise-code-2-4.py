#!/usr/bin/python3

# Explain the following line of code
#mySet = {1, 2, [3, 4]} # Causes an error: unhashable type: 'list'
# Sets cannot have mutable items 

# Creating an empty set
Sprot = set()
#print(type(Sprot))
#initialize with set() to get empty set

Sprot.add("NP_001304113")
Sprot.add("NP_001304114")
print("RefSeq identifiers in the protein set: \n {}".format(Sprot))