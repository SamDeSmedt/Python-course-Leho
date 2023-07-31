#!/usr/bin/python3
'''
# Ask for input and print
# Feedback: limit the amount of print and echo functions in the code
textinput = input("Please provide input: ")
print("Input in upper case: {}\n"
    "Input in lower case: {}"
    .format(textinput.upper(), textinput.lower()))
#####################################################################

# Ask for input sequence and motif
seq = input("Provide the sequence input: ")
motif = input ("Provide the motif input: ")

# Search for motif in sequence
find_pos = seq.find(motif)+1
print("[FIND] Motif found at position: {}".format(find_pos))
index_pos = seq.find(motif)
print("[INDEX] Motif found as sequence: {}".format(index_pos))
'''
######################################################################
# Ask for input sequence and cleavage site
seq = input("Provide the sequence input: ")
split = input("Provide the cleavage site for the sequence: ")

# Display sequence fragment after cleavage
cleav = seq.split(split)
print("[CLEAVING] Cleaving products of the sequence are: {}".format(cleav))
