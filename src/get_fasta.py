from Bio import Entrez, SeqIO
Entrez.email = 'gratirodrigues.gdr@gmail.com'

handle = Entrez.esearch(db='nucleotide', term = ['(("Babesia"[Organism] OR Babesia[All Fields]) AND 18s[All Fields]) AND "Babesia microti"[porgn]'], retmax=20)
record = Entrez.read(handle)
handle.close()
print (record["IdList"])

handle = Entrez.efetch(db='nucleotide', id = record["IdList"], rettype = 'fasta')
record=SeqIO.parse(handle, 'fasta')
outputname = 'new_fasta/teste.fasta'

SeqIO.write(record, outputname, 'fasta')
