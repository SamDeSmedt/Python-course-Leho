#!/usr/bin/python3
################################################################################
# Reading a .sam file
################################################################################
import re
import os
# Change path to correct directory
os.chdir("/home/guest/Python/Scripts/ExampleExam")

# Counter to iterate over each comment line in the file
i = 0
# Counter to iterate over each information line in the file
c = 0
# Create empty dictionary
dictionary = {}
 # Open file to get data from
with open("SRR3233298-20000.sam", mode="r") as fileObj:
    print("Reading file SRR3233298-20000.sam")
    for line in fileObj.readlines():
        # Split the lines using the tab delimiter
        split = line.split("\t")
        # Check if the content is a comment line or information line
        # Comment line starts for .sam file with "@"
        if re.match("^@",line):
            i += 1
            print("Read comment line {}:\n{}".format(i, line))
        else:
            # Append information to dictionary
            dictionary[split[0]] = split[4]
            if c % 4000 == 0:
                #print("Parsing read {}: READ={}".format(i, split[0]))
                print("Parsing read {}: READ={}, MAPQ={}\n".format(c, split[0], split[4]))
            c += 1
print("Read {} lines!".format(c))
# Initialize limit
limit = 5
rev_limit = len(dictionary) - limit
res = dict(list(dictionary.items())[0:limit])
print("First 5 records in dictionary:\n{}".format(res))
res = dict(list(dictionary.items())[rev_limit:])
print("Last 5 records in dictionary:\n{}".format(res))

# Start new emtpy dictionary and new counter
i = 0
mapq = {}
set = set()
for k,v in dictionary.items():
    # Increment the count for this value in the mapq dictionary
    mapq[v] = mapq.get(v,0) + 1
    set.add(v)

# Sort the keys in the dictionary
set_keys = sorted(mapq.keys())

print("Unique MAPQ values: {}".format((set_keys)))
# orint the value per sorted key
for key in set_keys:
    value = mapq[key]
    print("counting {} --> {}".format(key, value))


