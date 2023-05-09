#!/usr/bin/python3
################################################################################
# Skill exam excercise 1
# Iterate over csv file to create a fasta file
################################################################################
import csv
import os
from eutils import Client

# Initialize client that handles all caching and query
# Using API key from NCBI account settings e.g. 
eclient = Client(api_key="cf9fdefa66d8e8b9e6ea5a8d27f0b8c59c09")

# Change path to correct directory
os.chdir("/home/guest/Python/Scripts/ExampleExam")

fasta_file = open("sequences.fasta", '+a')
# Reading csv file line by line
with open('gene_species.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print column names
            print("Column names are:")
            print("{0:5s} | {1:5s}".format(row[0],row[1]))
            line_count += 1
        else:
            #Hardcoded input row[0] and row[1]
            #row = ["Cdh1","Mus musculus"]
            gene = row[0]
            species = row[1]

            # Define variable search term
            searchterm = gene + ' [gene] AND "' + species + '" [orgn] AND srcdb refseq [prop]'
            #print(searchterm)
            prot_esearch = eclient.esearch(db="protein", term=searchterm)
            #print("\n\nResults of gene esearch:\n{}".format(prot_esearch))
            #print("Ids: {}".format(prot_esearch.ids))
            ################################################################################
            # EFETCH: get record using Id
            ################################################################################
            for id in prot_esearch.ids:
                prot_efetch = eclient.efetch(db='protein', id=id)
                #print("\n\nResults of prot efetch:\n{}".format(prot_efetch))
                # One may fetch multiple genes at a time
                #print("\nProt object attributes:")
                ## These are returned as an gbseqs
                refseq = prot_efetch.gbseqs[0]
                #prot_obj_list = dir(refseq)
                #print(prot_obj_list)
                species = species.replace(" ", "_")
                #print(species)
                print(">{}_{}_id={}\n{}".format(gene,species,id, refseq.sequence))
                fasta_file.write(">{}_{}_id={}\n{}\n".format(gene,species,id, refseq.sequence))
fasta_file.close()
    
    
    
