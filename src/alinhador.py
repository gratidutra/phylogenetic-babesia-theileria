from Bio import SeqIO
from Bio import AlignIO
from Bio import Seq
import os
import sys

def align_sequences(path_fasta) :
    input_file = path_fasta
    records = SeqIO.parse(input_file, 'fasta')
    records = list(records) # make a copy, otherwise our generator
                        # is exhausted after calculating maxlen
    maxlen = max(len(record.seq) for record in records)

    # pad sequences so that they all have the same length
    for record in records:
        if len(record.seq) != maxlen:
            sequence = str(record.seq).ljust(maxlen, '.')
            record.seq = Seq.Seq(sequence)
    assert all(len(record.seq) == maxlen for record in records)
    
    # write to temporary file and do alignment
    output_file = '{}_padded.fasta'.format(os.path.splitext(input_file)[0])
    with open(output_file, 'w') as f:
        SeqIO.write(records, f, 'fasta')
    alignment = AlignIO.read(output_file, "fasta")
    return alignment

def main():
        print('Iniciando o Alinhamento pro meu amorzinh')
        file_name = sys.argv[1]
        align_sequences(file_name)
        print('Buenissimo agora use e abuse do arquivo fasta e seja feliz com suas arvres')    
	
if __name__ == "__main__":
    main()