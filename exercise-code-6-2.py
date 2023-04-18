#!/usr/bin/python3
import MySQLdb as my

# Reading data from Ensembl
print("\nREADING ENSEMBLE TRANSCRIPT DATA")
# Core databases: <genus_species>_core_<version>_<assembly_version>
# Ensembl Release 104 (May 2021)
db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_108_38")
c = db.cursor()
no_rows3 = c.execute("""SELECT * FROM gene limit 5""")
#print(c.fetchone())
result = c.fetchall()
for field in result:
    print("Example record:\n{} --> {} = {}".format(1,2,3)) # random input used
    # tabeles should be joined to get all the necessary information

