seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

def find_orfs(seq):
    orfs = []
    for i in range(len(seq)-2):
        codon = seq[i:i+3]
        if codon == 'AUG':
            for j in range(i+3, len(seq)-2, 3):
                stop_codon = seq[j:j+3]
                if stop_codon in ['UAA', 'UAG', 'UGA']:
                    orfs.append(seq[i:j+3])
                    break
    return orfs

orfs = find_orfs(seq)
largest_orf = max(orfs, key=len) if orfs else None
print(f'largest_orf: {largest_orf}, length: {len(largest_orf)}')
print(f'all_orfs: {orfs}')
