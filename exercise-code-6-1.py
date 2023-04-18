#!/usr/bin/python3

import MySQLdb as my

# Reading data from UCSC
# Select data from db="hg19"
print("\nREADING DATA FROM UCSC DATABASE hg19")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg19")
c = db.cursor()
no_rows = c.execute("""SELECT * FROM ncbiRefSeq where name like 'NM_%'""")
print("Amount of mRNA transcripts in hg19: {}".format(no_rows))
######################################################################
print("\nREADING DATA FROM UCSC DATABASE hg38")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")
c = db.cursor()
no_rows2 = c.execute("""SELECT * FROM ncbiRefSeq where name like 'NM_%'""")
print("Amount of mRNA transcripts in hg38: {}\n".format(no_rows2))

######################################################################
#Calculate difference in trascript total
total = no_rows2 - no_rows
print("hg38 has {} more transcripts compared to hg19".format(total))