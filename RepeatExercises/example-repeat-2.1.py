#!/usr/bin/python3
################################################################################
# String methods
################################################################################

# Display input in upper and lower cases
seq = input("Provide sequence: ")

# Search for the motif in the sequence and return the position of the motif
# Split the input sequence using a cleavage site
site = input("Provide an cleavage site: ")

if site in seq:
    index = seq.index(site)
    pos = index + 1
    split = seq.split(site)
    # Give the calculated output
    print("Input displayed in upper cases: \"{}\"".format(seq.upper()))
    print("Input displayed in lower cases: \"{}\"".format(seq.lower()))
    print("The index of the motif in the sequence: {}".format(index))
    print("The position of the motif in the sequence: {}".format(pos))
    print("After splicing input sequence \"{}\", fragment 1 is \"{}\" and fragment 2 is: {}".format(seq,split[0],split[1]))
    print("After splicing input sequence \"{}\", fragment 1 is \"{}\" and fragment 2 is: {}".format(seq,split[0],split[1]))
else:
    print("The cleavage site \"{}\" is not present in sequence \"{}\"".format(site, seq))