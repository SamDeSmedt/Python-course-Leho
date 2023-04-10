#!/usr/bin/python3

# Script to count the amount per base type and calculate the frequency

input = input("Enter DNA sequence: ")
bases = {}

def basefreq(input):

    # calculate the base count
    count = len(input)
    #print(len)

    # Place each individual character in a list
    list = set(input)
    #print(list)

    # Count each individual character in the input and update in a dictionary
    for i in list:
        bases.update({i:input.count(i)})

    # Calcute the frequency of each base 
    for k,v in bases.items():
        bases.update({k:(v*1.0/count)})
    return bases
print("Calculate base frequency: \n{}".format(basefreq(input)))
