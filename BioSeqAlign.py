import sys
import requests
import subprocess
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def translate_dna_to_protein(dna_sequence):
    return Seq(dna_sequence).translate()

def align_protein_sequences(input_file):
    protein_records = []
    
    for record in SeqIO.parse(input_file, "fasta"):
        dna_sequence = str(record.seq)
        protein_seq = translate_dna_to_protein(dna_sequence)
        protein_record = SeqRecord(protein_seq, id=record.id, description="")
        protein_records.append(protein_record)

    protein_output_file = input_file.replace('.fasta', '.protein.fasta')
    SeqIO.write(protein_records, protein_output_file, "fasta")

    # Specify the MAFFT command using wsl.exe
    aligned_output_file = input_file.replace('.fasta', '.align.fasta')  # Define the aligned output file
    mafft_cmd = ['wsl.exe', 'mafft', '--auto', protein_output_file]
    
    try:
        subprocess.run(mafft_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to perform alignment using MAFFT: {e}")
        sys.exit(1)

    print(f"Translation, alignment, and untranslation completed. Aligned sequences saved to {aligned_output_file}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file.fasta")
        sys.exit(1)

    input_file = sys.argv[1]
    align_protein_sequences(input_file)
