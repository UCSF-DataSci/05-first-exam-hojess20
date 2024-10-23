import argparse

# dictionary of base complements
complement_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    'a': 't',
    't': 'a',
    'c': 'g',
    'g': 'c'
}
# return complement of DNA sequence
def complement(sequence):
    complement_sequence = ""
    for base in sequence:
        complement_sequence += complement_map[base] # Append complement of base to the complement_sequence
    return complement_sequence

# return reversed DNA sequence
def reverse(sequence):
    return sequence[::-1]

# return reverse complement of DNA sequence
def reverse_complement(sequence):
    return reverse(complement(sequence))

def main():
    parser = argparse.ArgumentParser(description="Perform operations on a DNA sequence.")
    parser.add_argument("sequence", type=str, help="Input DNA sequence")
    
    args = parser.parse_args()

    input_sequence = args.sequence # get sequence from the arguments

    # printing the results
    print(f"Original sequence: {input_sequence}")
    print(f"Complement: {complement(input_sequence)}")
    print(f"Reverse: {reverse(input_sequence)}")
    print(f"Reverse complement: {reverse_complement(input_sequence)}")

if __name__ == "__main__":
    main()
