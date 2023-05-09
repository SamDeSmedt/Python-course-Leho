#!/usr/bin/python3
################################################################################
# Accessing a database and collect protein sequences
################################################################################
from eutils import Client
# Initialize client that handles all caching and query
# Using API key from NCBI account settings e.g. 
eclient = Client(api_key="cf9fdefa66d8e8b9e6ea5a8d27f0b8c59c09")
print("\nUsing NCBI E-utilities in Python\n")
################################################################################
# ESEARCH: search for sequences, any valid NCBI query may be used
################################################################################
prot_esearch = eclient.esearch(db='Protein',term='DSG* [gene] AND "Mus Musculus" [orgn] AND srcdb refseq [prop]')
#print("\n\nResults of protein esearch:\n{}".format(prot_esearch))
obj_summary_list = dir(prot_esearch)
#print(obj_summary_list)
# Gene esearch summary result
'''
print("\nProt esearch summary result:")
print("="*28)
print("Count: {}".format(prot_esearch.count))
print("Retmax: {}".format(prot_esearch.retmax))
print("Retstart: {}".format(prot_esearch.retstart))
print("Ids: {}".format(prot_esearch.ids))
'''
################################################################################
# EFETCH: get record using Id e.g. protein id 165377226
################################################################################
result_file = open("result.fasta", "+a")
for ids in prot_esearch.ids:
    prot_efetch = eclient.efetch(db='Protein', id=ids)
    #prot_obj_list = dir(prot_efetch)
    #print(prot_obj_list)
    #print("\nRefSeq using gbseq: {}".format(prot_efetch.gbseqs[0]))
    #refseq_list = dir(prot_efetch.gbseqs[0])
    #print(refseq_list)
    refseq = prot_efetch.gbseqs[0]
    print(
    "acv : {}\ncds: {}\ngi: {}\nlocus: {}\norganism: {}\n".format(refseq.acv,refseq.cds, refseq.gi, refseq.locus, refseq.organism))
    print("Loop over Ids: \n" + "="*28)
    print(">{}\n{}".format(refseq.locus, refseq.sequence))
    result_file.write(">"+refseq.locus+"\n"+refseq.sequence+"\n")
result_file.close()


