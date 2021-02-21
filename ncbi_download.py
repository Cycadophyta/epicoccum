from Bio import Entrez

Entrez.email = "HamishMcLean@gmail.com"
handle = Entrez.esearch("nucleotide", "Epicoccum nigrum", retmax=10) 
record = Entrez.read(handle)
handle.close()
print(record)

