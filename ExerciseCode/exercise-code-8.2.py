#!/usr/bin/python3
################################################################################
# Get information from sequence.fasta file and print the length of the exons
# 1) Read in the DNA sequence from the file
# 2) Identify all exons in the sequence
# 3) Calculate the length of each exon
# 4) Print the lengt of exon to an excel file
################################################################################
import re
from openpyxl import Workbook

# Hardcoded sequence
#seq = "GTTGAGCAGAACACTAAAGCCCGATCGGGTCAATCTAGTTTAGACCCGCATCGTAGTCCATGAAAAGGCCGATGATTTTCAGTGATCGTAGTTAACAGTTCCCGCCGGATCGTAGGGGCGAAGTCGGAGGGGGACGAAGCAGAGGGCGTAGTCTGAAGATCCACTGTCTACTGCGTCTCAGGCAAACGATGTAACGCATAAGCGGTTAACTAGTACTTAATGGCGGTTGTTCAGCCCTCGGAAAGGGTGACTTTTAGCGTCTCTATAACCCTTGTTTCCAAAGTCACGTATAAACGCAACAAGAATGTGCGGCCGGCGATATCGAATCGTAGCACGCCCAGCATCTTCAAAATCCTTCACTAGGGTACCCGAAGAATACGACCCAGCCTTGAAGCGCTGACGTCCGTTATCTCCCTCGAGTGTACAGTTCTCCTAAATGGCAGGGGTACTTCGGGTCTCTGTTCTATACACATATGGCTAGGGGTGTGCAACGGAAGATC"
# Sequence that marks the beginning and ending of an exon
# If this sequence is not present in the beginning of the split sequence then
# this is considered part of an intron en therefor excluded
exon_codon = "ATCGTAG"

# for each even occurance the length should be determined including the exon_condon
# at the beginning and the end of the sequence
# Open excel file to write information to

# Initialize Workbook
wb = Workbook()
# Active worksheet
ws = wb.active
# Add headers to Workbook
ws.append(["SequenceId", "Exon length", "Exon sequence"])

# Create an empty list to store the data
data = []
# Open the FASTA file and read in the DNA sequence
with open("sequences.fasta", "r") as file:
    for seq in file:
        # Initiate exon couting per sequence
        i = 0
        if re.match("^>",seq):
            seq_id = seq.strip()[1:]
            #print(seq)
        else:
            result = seq.split(exon_codon)[1:-1]
            for exon in result:
                if i % 2 == 0:
                    #print(i)
                    exon_seq = exon_codon + exon + exon_codon
                    exon_len = len(exon)+(2*len(exon_codon))
                    data.append([seq_id, exon_len, exon_seq])
                    #print("Exon sequence: \n{}\nExon length: {}\n".format(exon_seq, exon_len))
                i += 1
# Write the data to the excel file
for row in data:
    ws.append(row)

# Save the workbook
wb.save("exon_data.xlsx")
            