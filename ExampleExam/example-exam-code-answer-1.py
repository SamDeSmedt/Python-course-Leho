#!/usr/bin/python3
################################################################################
# Skill exam excercise 1
# Look for SNP data in the UCSC database and store it in an excel file
################################################################################
import MySQLdb as my
from openpyxl import Workbook
# Create an empty list to store user input
input_list = []
print("\nThis script will look for SNPs using RefSeq accession numbers")
print("="*100)

# Hardcoded input
#input_list = ["NM_001511", "NM_032738"]

# Input from user
while True:
    user_input = input("Enter accession no. or type 0 to stop: ")
    if user_input == "0":
        break
    else:
        input_list.append(user_input)
print("\nYour list: \n{}\n".format(input_list))

# Initialize Workbook
wb = Workbook()
# Active worksheet
ws = wb.active
# Append headers to worksheet
ws.append(["Accession no.", "SNP", "Chr:start-stop"])
# Reading data from UCSC
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")
c = db.cursor()
# Iterate over the input_list accession numbers
for snp in input_list:
    #print(snp)
    print("Getting SNPs for: {}".format(snp))
    print("using query: SELECT * FROM snp151CodingDbSnp WHERE transcript = '{}'".format(snp))
    #Excecute command to perform in the database
    no_rows = c.execute("SELECT * FROM snp151CodingDbSnp WHERE transcript = '%s'" % snp)
    print("Total SNPs found for {}: {}\n".format(snp, no_rows))
    # Fetch all results
    result = c.fetchall()
    # Iterate over result
    for row in result:
        description = "%s:%s-%s" % (row[1],row[2],row[3])
        accNo = row[5]
        snpNO = row[4]
        #print("Accession no.: {}\nSNP: {}\nDescription: {}".format(row[5],row[4],description))
        ws.append([accNo, snpNO, description])
# Close db connection
db.close()
# Save workbook
wb.save("SNPs.xlsx")
