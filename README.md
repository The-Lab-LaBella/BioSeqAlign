# BioSeqAlign
Python script designed to take a FASTA file containing nucleotide sequences, translates them into protein sequences, performs a multiple sequence alignment using MAFFT (a bioinformatics tool), and then untranslates the aligned protein sequences back into nucleotides.
Prerequisites:

Make sure you have Python installed on your system.
Ensure you have the Biopython library installed. You can install it using pip: pip install biopython.
Also, ensure that you have MAFFT installed.

Prepare Input:

Create a FASTA file containing DNA sequences that you want to process

Run the Script:

Open your terminal or command prompt.
Navigate to the directory where the script is located.

python BioSeqAlign.py input_file.fasta 

Output:

The script will perform the following steps:
Translate the DNA sequences to protein sequences and save them in a new file with a ".protein.fasta" extension.
Perform a multiple sequence alignment using MAFFT on the protein sequences.
Create an alignment output file in the same directory as the input file, with a ".align.fasta" extension.
Display a completion message.

Check Output: 
You will find a new file in the same directory as your input file ending with the file extension ".protein.fasta" containing the translated protein sequences. 
