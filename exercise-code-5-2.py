#!/usr/bin/python3

import os
import re
import humanfriendly
from openpyxl import Workbook

# Initialize Workbook
wb = Workbook()
# Active worksheet
ws = wb.active
# Append headers to excel file
ws.append(["sample_id","filesize"])

# Use present working direction to work with the folder
# Create the pathway to the correct directory
location = os.getcwd() # Use the pwd as directory to work in
#print(location)
file_loc = location + "/exercise-5-2-htseqcount/" 
print("Files and folders in {} :\n".format(file_loc))

#print("\nCurrent working directory: ", os.listdir(file_loc)) #get pwd
# List all files that are present in the present working location
file_list = os.listdir(file_loc)

for file in file_list:
    # Store the path to the file in a variable
    file_path = file_loc + file
    #Need path to file to determine the filesize --human readable
    size_bytes = os.path.getsize(file_path)
    fsize = humanfriendly.format_size(size_bytes, binary=True)
    if re.match("^counts",file): # use "^" to match the first string
        # Split the file names using the "_" as seperator
        sample = file.split("_")
        ws.append([sample[1], fsize])
        print("sample_id = {}\nfilesize = {}\n".format(sample[1],fsize))
wb.save("example.xlsx")
