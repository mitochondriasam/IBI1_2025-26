import re

class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
    
    def __repr__(self):
        return f'{self.name}: {self.sequence}'
    
    def find_orfs(self):
        orfs = []
        for i in range(len(self.sequence)-2):
            codon = self.sequence[i:i+3]
            if codon == 'AUG':
                for j in range(i+3, len(self.sequence)-2, 3):
                    stop_codon = self.sequence[j:j+3]
                    if stop_codon in ['UAA', 'UAG', 'UGA']:
                        orfs.append(self.sequence[i:j+3])
                        break
        return orfs
    
    
def parse_genes(filename):
    pattern = re.compile(r'\bgene:([^\s]+)')
    genes = []
    name = None
    sequence = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('>'):
                if name is not None:
                    genes.append(Gene(name, ''.join(sequence)))
                m = pattern.search(line)
                name = m.group(1) if m else None
                sequence = []
            else:
                sequence.append(line.strip())

    if name is not None:
        genes.append(Gene(name, ''.join(sequence)))

    return genes


if __name__ == "__main__":
    genes = parse_genes('Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
    # print(genes[0])
    for gene in genes:
        orfs = gene.find_orfs()
        largest_orf = max(orfs, key=len) if orfs else None
        print(f'{gene.name}: largest_orf: {largest_orf}, all_orfs: {orfs}')
    # orfs = genes[0].find_orfs()
    # largest_orf = max(orfs, key=len) if orfs else None
    # print(f'largest_orf: {largest_orf}')
    # print(f'all_orfs: {orfs}')