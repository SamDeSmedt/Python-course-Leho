#!/usr/bin/python3
################################################################################
import random

# Define the length of the random sequences and the number of times to repeat the pattern
sequence_length = 500
pattern_repetitions = 4

# Define the pattern
pattern = "ATCGTAG"

# Create a file for the sequences
sequence_file = open("sequences.fasta", "w")

# Generate and write the random sequences to the file
for i in range(10):
    # Generate a random sequence
    sequence = ""
    for j in range(sequence_length):
        nucleotide = random.choice(["A", "T", "C", "G"])
        sequence += nucleotide
        
    # Insert the pattern at random positions in the sequence
    for j in range(pattern_repetitions):
        start_index = random.randint(0, sequence_length - len(pattern))
        end_index = start_index + len(pattern)
        sequence = sequence[:start_index] + pattern + sequence[end_index:]
    
    # Write the sequence to the file in FASTA format
    sequence_file.write(">sequence_{}\n{}\n".format(i+1, sequence))

# Close the file
sequence_file.close()
