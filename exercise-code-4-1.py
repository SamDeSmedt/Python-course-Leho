#!/usr/bin/python3
# Function to reverse a string

#Function definition
def string_reverse(FwStr):

    # Define index
    index = (len(FwStr))-1

    #Define variable reverse string
    RvStr = ""

    # Print character backwards
    while index >= 0:
        #print(FwStr[index])
        RvStr = RvStr + FwStr[index]
        index = index -1
    return RvStr

print(string_reverse("meetsysteemstrook"))