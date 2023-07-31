#!/usr/bin/python3
import MySQLdb as my
import sqlite3
import time

# Reading data from Ensembl
print("\nREADING ENSEMBLE TRANSCRIPT DATA...")
# Record start time
start = time.time()
# Core databases: <genus_species>_core_<version>_<assembly_version>
# Ensembl Release 104 (May 2021)
db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_108_38")
c = db.cursor()
no_rows = c.execute("""\
    SELECT transcript.transcript_id, transcript.gene_id,\
    transcript.stable_id, gene.stable_id, gene.description\
    FROM gene \
    left join transcript on gene.gene_id=transcript.gene_id"""
                    )
# 0 = transcript.transcript_id | 1 = transcript.gene_id
# 2 = transcript.stable_id | 3 = gene.stable_id | 4 = gene.description
#print(c.fetchone()) # Helpfull to see what data is displayed

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

i = 0
result = c.fetchall()
#print(result)

print("Example records:")
for field in result:
    if (i < 5):
        print("{} --> {} = {}".format(field[2],field[3],field[4]))
    i += 1
    # Save in sql ensembl.db and commit
    cursor.execute('INSERT INTO transcript_inf VALUES (?,?,?)', (field[2],field[3],field[4]))

# Print total amount of records
print("Ensembl hg38 transcript table: {} ENST records".format(i))

# Save (commit) changes
conn.commit()
# Close connections
db.close()
conn.close()
# Record time end
end = time.time()
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is: \n\
      {:.2f} s".format((end-start)))
