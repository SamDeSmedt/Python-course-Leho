#!/usr/bin/python3
import MySQLdb as my
import sqlite3
import time

code = input("Enter ENSG number: ")
# Reading data from Ensembl
print("\nREADING ENSEMBLE TRANSCRIPT DATA...")
# Record start time
start = time.time()
# Core databases: <genus_species>_core_<version>_<assembly_version>
# Ensembl Release 104 (May 2021)
db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_108_38")
c = db.cursor()
no_rows = c.execute("""SELECT transcript.stable_id, gene.stable_id, gene.description FROM gene join transcript on gene.gene_id=transcript.gene_id where gene.stable_id = %s""",(code,))
#print(c.fetchone()) # Helpfull to see what data is displayed
i = 0
result = c.fetchall()
#print(result)

print("Example records:")
for field in result:
    if (i < 5):
        print("{} --> {} = {}".format(field[0],field[1],field[2]))
    i += 1
c.close()

# Print total amount of records
print("Ensembl hg38 transcript table: {} ENST records".format(i))

# First step: create database connection object
conn = sqlite3.connect('ensembl.db')
#Next create cursor object
# and call its execute() method to perform SQL query
cursor = conn.cursor()
# Create table
try: # Test the code
    cursor.execute('''CREATE TABLE transcript_inf \
            (ENST, ENSG, description)''')
except sqlite3.OperationalError:
    print("\nTable transcript_inf already exists\n")
cursor.executemany('INSERT INTO transcript_inf VALUES (?,?,?)', result)
# Save (commit) changes
conn.commit()
# Close connection
conn.close()
# Record time end
end = time.time()
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is: \n\
      {0:.2f} s".format((end-start)))