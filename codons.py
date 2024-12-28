def create_codon_dict(file_path):
  file = open(file_path)
  rows = file.readlines()
  file.close()
  codons = {}
  for row in rows:
    cells = row.strip().split('\t')
    codon = cells[0]
    amino_acid = cells[2]
    codons[codon] = amino_acid
  return codons


