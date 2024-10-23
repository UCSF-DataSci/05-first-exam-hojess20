import random
sequence_length = 1000000
output_file = "bioinformatics_project/data/random_sequence.fasta"

# generate random sequence 
dna_bases = ['A', 'C', 'G', 'T']
random_seq = ''.join(random.choices(dna_bases, k=sequence_length))

# formatting sequence to 

with open(output_file, 'w') as fasta_file:
    for i in range(0, sequence_length, 80):
        # Slice the sequence to get the next 80 base pairs
        line = random_seq[i:i + 80]
        fasta_file.write(line + '\n')

print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")
