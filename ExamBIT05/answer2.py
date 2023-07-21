#!/usr/bin/python3
################################################################################
# Aswer 2 for the python exam
################################################################################
import re
from openpyxl import Workbook

# Initialize Workbook
wb = Workbook()
# Active worksheet
ws = wb.active
# Write headers to workbook
ws.append(["species", "LPSN link", "NCBI genome link", "LPSN status", "LPSN reference"])
# open NCBI_Genome_result_Legionella.txt file
with open("NCBI_Genome_result_Legionella.txt") as file:
    i = 0
    #start an empty lists
    name_list = []
    id_list = []
    for line in file.readlines():
        i += 1
        if line[0].isdigit():
            print(line.strip())
            name = line.strip().split(".")
            name_list.append(name[1])
            #print(name_list)

        elif re.match("Genome ID", line):
            split = line.split(" ")[2]
            id = split.replace("\n", "")
            id_list.append(id)
            #print(id_list)
# Print newline
print("\n")
# Put values in dictionary
d = dict(zip(name_list, id_list))
print(d)

import csv
ncbi_link_base = "https://www.ncbi.nlm.nih.gov/genome/?term="
# Open lpsn_export.csv file
with open('lpsn_export.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    
    print("Reading LPSN file and searching for Legionella nomenclature:\n")
    for row in csv_reader:
        if re.match("Legionella", row[0]):
            i += 1
            species = row[0] + " " + row[1]
            lpsnlink = row[6]
            status = row[4]
            ref = row[3]
            print("Found ({}) {}\n\
                  --> {}\n\
                  --> {}".format(i, species, lpsnlink, ncbi_link_base))
            
            # COMMENT: THIS PIECE OF CODE GENERATES ERROR BUT IS ALSO PEACE OF THE SOLUTION
            #ncbi_link = ncbi_link_base + d[" " + species]
            #print("this is the full link".format(ncbi_link))

            ws.append([species, lpsnlink, ncbi_link_base, status, ref])
            
            #print(species)
            #print(lpsnlink)
            #print(status)
            #print(ref)


# Save file
wb.save("Legionella.xlsx")
         
        

    
    
        

        
        

        
