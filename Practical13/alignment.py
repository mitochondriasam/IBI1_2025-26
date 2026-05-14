# test
# seq1 = "MLSRAVCGT"
# seq2 = "MLCRAACST"
# edit_distance = 0
# for i in range(len(seq1)):
#     if seq1[i] != seq2[i]:
#         edit_distance += 1
        
# print("Edit distance:", edit_distance)

# three pairwise combinations of the sequences
    
def postprocess(seq: list) -> str: 
    for line in seq:
        output = ''
        if line.startswith('>'):
            continue
        else:
           output += line.strip()
    return output

def edit_distance(seq1: str, seq2: str) -> int:
    distance = 0
    min_len = min(len(seq1), len(seq2))
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            distance += 1
    distance += abs(len(seq1) - len(seq2))
    return distance

if __name__ == "__main__":
    
    with open('human.fasta') as f:
        human_seq = postprocess(f.read().splitlines())
    with open('mouse.fasta') as f:
        mouse_seq = postprocess(f.read().splitlines())   
    with open('seq.fasta') as f:
        target_seq = postprocess(f.read().splitlines())
    
    print("Edit distance between human and mouse:", edit_distance(human_seq, mouse_seq))
    print("Edit distance between human and target:", edit_distance(human_seq, target_seq))
    print("Edit distance between mouse and target:", edit_distance(mouse_seq, target_seq))
        
        