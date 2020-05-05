# python3
import sys

def optimal_sequence(n):
    hop_count = [0] * (n + 1)
    hop_count[1] = 1
    
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i//2)
        if i % 3 == 0:
            indices.append(i//3)
        
        min_hops = min([hop_count[x] for x in indices])
        hop_count[i] = min_hops + 1

    pointer = n
    optimal_seq = [pointer]
    while pointer != 1:
        candidates = [pointer - 1]
        if pointer % 2 == 0:
            candidates.append(pointer//2)
        if pointer % 3 == 0:
            candidates.append(pointer//3)

        pointer  = min([(c, hop_count[c]) for c in candidates], key=lambda x: x[1])[0]
        optimal_seq.append(pointer)

    return reversed(optimal_seq)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
