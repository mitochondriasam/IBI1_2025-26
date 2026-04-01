import matplotlib.pyplot as plt
import re
from collections import Counter
from stop_codons import Gene

class newGene(Gene):
    def find_longest_orf(self, stop_codon):
        longest_codons = []

        for start_index in range(len(self.sequence) - 2):
            if self.sequence[start_index:start_index + 3] != 'ATG':
                continue

            for codon_index in range(start_index + 3, len(self.sequence) - 2, 3):
                codon = self.sequence[codon_index:codon_index + 3]
                if codon in ['TAA', 'TAG', 'TGA']:
                    if codon == stop_codon:
                        orf_codons = [
                            self.sequence[index:index + 3]
                            for index in range(start_index, codon_index + 3, 3)
                        ]
                        if len(orf_codons) > len(longest_codons):
                            longest_codons = orf_codons
                    break

        return longest_codons
    
def parse_genes(filename):
    pattern = re.compile(r'>([^\s]+)\s')
    genes = []
    name = None
    sequence = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip( '\n')
            if line.startswith('>'):
                if name is not None:
                    genes.append(newGene(name, ''.join(sequence)))
                m = pattern.search(line)
                name = m.group(1) if m else None
                sequence = []
            else:
                sequence.append(line.strip())

    if name is not None:
        genes.append(Gene(name, ''.join(sequence)))

    return genes

def make_pie_chart(counts, stop_codon, output_path):
    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure(figsize=(12, 12))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'In-frame codon usage upstream of {stop_codon}')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    
if __name__ == "__main__":
    genes = parse_genes('Practical7/stop_codons.fa')
    stop_codon = input("Enter a stop codon (TAA, TAG, TGA): ").strip().upper()
    while stop_codon not in ['TAA', 'TAG', 'TGA']:
        print("Invalid stop codon. Please enter TAA, TAG, or TGA.")
        stop_codon = input("Enter a stop codon (TAA, TAG, TGA): ").strip().upper()

    longest_orfs = []
    for gene in genes:
        new_gene = newGene(gene.name, gene.sequence)
        longest_orf = new_gene.find_longest_orf(stop_codon)
        longest_orfs.append((gene.name, longest_orf))
    
    codon_counts = Counter()
    for name, orf in longest_orfs:
        if orf:
            codon_counts.update(orf[:-1])  # Exclude the stop codon
    make_pie_chart(codon_counts, stop_codon, f'Practical7/codon_usage_pie_chart_{stop_codon}.png')
    print(f'Codon counts upstream of {stop_codon}:\n{codon_counts}')      
