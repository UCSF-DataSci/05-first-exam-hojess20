import argparse

# read DNA sequence from fasta file
def read_fasta(file):
    seq = ""
    with open(file, 'r') as fasta_file:
        for line in fasta_file:
            if line.startswith('>'):  # skip header ('>') if present
                continue
            seq += line.strip() # remove spaces or newline characters and adding line to sequence
    return seq

# find cut site positions
def find_cut_sites(seq, cut_site):
    cut_site = cut_site.replace('|', '')
    cut_locations = []
    index = seq.find(cut_site)

    while index != -1:
        cut_locations.append(index)
        index = seq.find(cut_site, index + 1)
    return cut_locations


def find_cut_site_pairs(cut_locations, min_distance=80000, max_distance=120000):
    pairs = []
    total_locations = len(cut_locations)
    for i in range(total_locations):
        for j in range(i + 1, total_locations):
            distance = cut_locations[j] - cut_locations[i]
            if min_distance <= distance <= max_distance:
                pairs.append((cut_locations[i], cut_locations[j]))
    return pairs

def main():
    parser = argparse.ArgumentParser(description= "Find pairs of cut sites in a DNA sequence.")
    parser.add_argument("fasta_file", type=str, help= "FASTA file path")
    parser.add_argument("cut_site", type=str, help= "Cut site sequence (e.g., 'G|GATCC')")
    
    args = parser.parse_args()
    dna_seq = read_fasta(args.fasta_file) # read DNA sequence from FASTA file
    cut_locations = find_cut_sites(dna_seq, args.cut_site) # find all cut sites
    cut_site_pairs = find_cut_site_pairs(cut_locations)

    print(f"Analyzing cut site: {args.cut_site}")
    print(f"Total cut sites found: {len(cut_locations)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")
    print(f"First 5 pairs:")
    for i, (site1, site2) in enumerate(cut_site_pairs[:5], start=1):
        print(f"{i}. {site1} - {site2}\n")    


    summary_file = "bioinformatics_project/results/cutsite_summary.txt"
    with open(summary_file, 'w') as summary:
        summary.write(f"Analyzing cut site: {args.cut_site}\n")
        summary.write(f"Total cut sites found: {len(cut_locations)}\n")
        summary.write(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        summary.write("First 5 pairs:\n")
        for i, (site1, site2) in enumerate(cut_site_pairs[:5], start=1):
            summary.write(f"{i}. {site1} - {site2}\n")

if __name__ == "__main__":
    main()