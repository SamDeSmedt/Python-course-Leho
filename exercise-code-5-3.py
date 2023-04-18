#!/usr/bin/python3

import os
import fnmatch
import re

# Change location to where the files are located
# Location could also be given using argparse
fastqc_dir = "/home/guest/Python/Files/exercise-5-3-fastqc/fastqc"
os.chdir(fastqc_dir)



for root, dirs, files in os.walk(fastqc_dir):
    
    for filename in fnmatch.filter(files,'*.txt'):
        # All the textfiles have .txt extionsion to work with
        # Get the information from the fastqc data files
        fastqc_match = re.match("^fastqc",filename)
        if fastqc_match:
            file_dir = root + "/" + filename
            #print(file_dir)
            with open(file_dir, "r") as fileObj:

                # reading each line
                for line in fileObj:
                    if re.search("Total Sequences",line):
                        TotalSeq = line.split()
                        print(TotalSeq)
            fileObj.close

