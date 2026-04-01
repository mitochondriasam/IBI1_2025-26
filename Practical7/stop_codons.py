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
            if codon == 'ATG':
                for j in range(i+3, len(self.sequence)-2, 3):
                    stop_codon = self.sequence[j:j+3]
                    if stop_codon in ['TAA', 'TAG', 'TGA']:
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

def in_frame_stop_codons(seq):
    stop_codons = set()
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if codon in ['TAA', 'TAG', 'TGA']:
            stop_codons.add(codon)
    return stop_codons

def write_gene(filename, gene, stop_codons):
    with open(filename, 'a') as f:
        f.write(f'>{gene.name}_mRNA; {stop_codons}\n')
        f.write(f'{gene.sequence}\n')
        

if __name__ == "__main__":
    genes_path = 'Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_path = 'Practical7/stop_codons.fa'

    open(output_path, 'w').close()  # Clear the output file before writing
    genes = parse_genes(genes_path)
    for gene in genes:
        orfs = gene.find_orfs()
        if not orfs:
            continue
        stop_codons = set()
        for orf in orfs:
            stop_codons.update(in_frame_stop_codons(orf))
        write_gene(output_path, gene, stop_codons)
