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

FwStr = input("Provide a word to be reversed: \n")
print(string_reverse(FwStr))
###############################################################
'''
def string_reverse(str1):
    return str1[::-1]
print("Reverse of live desserts = ", end=" ")
print(string_reverse("live desserts"))
'''
