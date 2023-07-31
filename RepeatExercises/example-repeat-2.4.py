#!/usr/bin/python3
################################################################################
# Sets
################################################################################

# Create a set with a list in there
#mySet = {1,2,[3,4]}
#print(mySet)
# Error is generateded because there is a list in a set

# Create an empty set called Sprot
Sprot = set()

# Add following RefSeq identifiers one by one in Sprot:
# NP_001304113 and NP_001304114

# Add NP_001304113 to the set
Sprot.add("NP_001304113")
print("After the addition of \"NP_001304113\", the value inside Sprot is: {}".format(Sprot))
# Add NP_001304113 to the set
Sprot.add("NP_001304114")
print("After the addition of \"NP_001304114\", the value inside Sprot is: {}".format(Sprot))
