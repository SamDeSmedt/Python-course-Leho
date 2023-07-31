#!/usr/bin/python3

import re
import csv

# Open file to start writing in
with open("exercise-code-output-5-1.csv", mode="w") as output_file:
    output_writer = csv.writer(output_file, 
    delimiter=';', 
    quotechar='"', 
    quoting=csv.QUOTE_MINIMAL)
    # Open file to get data from
    with open("129P2_OlaHsd.mgp.v5.indels.dbSNP142.normed.vcf", mode="r") as fileObj:
        for line in fileObj.readlines():
            # Check if the content is a comment line or information line
            # Comment line starts for .vcf file with "#"
            if re.match("#",line):
                None # Nothing should be performed when met
            else:
                # All data with information are used
                # Initialize empty string for each line
                csq = ""
                # Split all the lines that using a tab-delimiter
                del_list = line.split("\t")
                # FIELDS: 
                # CHROM=0 POS=1 ID=2 REF=3 ALT=4 QUAL=5
                # FILTER=6 INFO=7 FORMAT=8 GENE=9     
                # Check all the lines for the specified strings
                str_match1 = re.search("stop_gained",del_list[7]) # TRUE if found
                str_match2 = re.search("frameshift",del_list[7]) # TRUE if found
                if  str_match1 or str_match2:
                    #Check which of the expression is found "stop_gained" or "frameshift"
                    if str_match1:
                        csq = csq + "stop_gained"
                    elif str_match2:
                        csq = csq + "frameshift"
                    output_writer.writerow([del_list[0],del_list[1],del_list[3],del_list[4],csq])
    fileObj.close()
output_file.close()
                
                
