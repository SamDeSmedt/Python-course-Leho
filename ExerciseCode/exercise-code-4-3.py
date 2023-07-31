#!/usr/bin/python3

# Script to count the amount per base type and calculate the frequency

#input = input("Enter DNA sequence: ")
# Hardcoded input
input = "AAGGTCGATCGATGATATCTTTCTAATTCTTATTATCTCTAACACCAAAGGAGATGATGACGTAGCTA"
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
        bases.update({k:(v*100.0/count)})
    return bases
print("Calculate base frequency: \n{}".format(basefreq(input)))
################################################################################
# Visualise output using matplotlib
################################################################################
import matplotlib.pyplot as plt
# Defining the values for the barplot
base_key = list(bases.keys())
base_value = list(bases.values())

fig = plt.figure(figsize= (10,5))
# Creating the barplot
plt.bar(base_key, base_value, color="maroon", width=0.4)
plt.xlabel("Base")
plt.ylabel("Percentage")
plt.title("Base percentage")
plt.show()
