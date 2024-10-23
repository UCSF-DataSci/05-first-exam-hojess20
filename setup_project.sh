mkdir -p bioinformatics_project

cd bioinformatics_project
mkdir -p data scripts results
touch scripts/generate_fasta.py scripts/dna_operations.py scripts/find_cutsites.py
touch results/cutsite_summary.txt
touch data/random_sequence.fasta

echo "# Bioinformatics Project" > README.md
echo "This project contains 3 subdirectories:" >> README.md
echo "1. data" >> README.md
echo "	- random_sequence.fasta" >> README.md
echo "2. results" >> README.md
echo "	- cutsite_summary.txt" >> README.md
echo "3. scripts" >> README.md
echo "	- generate_fasta.py" >> README.md
echo "	- dna_operations.py" >> README.md
echo "	- find_cutsites.py" >> README.md

echo "Project directory structure created successfully."
