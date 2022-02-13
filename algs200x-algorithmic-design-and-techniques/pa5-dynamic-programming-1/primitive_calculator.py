# python3
# Input: An integer (n)
# Output: The minimum number of operations to get to n from 1 (can only multiply by 2 and 3 and add by 1)
#         The sequence of intermediary numbers

import sys

def optimal_sequence(n):
    
    # Initialize the number of hops for every integer <= n
    Hops = [0] * (n + 1)
    Hops[1] = 1
    
    # Loop through every integer from 2 to n
    for i in range(2, n + 1):
        # Creates list of integers that can be cleanly subtracted by 1, divided by 2, and divided by 3
        indexes = [i - 1]
        if i % 2 == 0:
            indexes.append(i//2)
        if i % 3 == 0:
            indexes.append(i//3)
        
        # Find the element with the least number of hops and add 1 hop
        MinHops = min([Hops[x] for x in indexes])
        Hops[i] = MinHops + 1

    # Reverse-engineer the steps it takes to match the number of hops
    Pointer = n
    OptimalArray = [Pointer]
    
    # Find all possible candidates
    while Pointer != 1:
        Candidates = [Pointer - 1]
        if Pointer % 2 == 0:
            Candidates.append(Pointer//2)
        if Pointer % 3 == 0:
            Candidates.append(Pointer//3)
        
        # Find the candidate that jumps to the lowest number of hops that it can
        # Reassign the pointer to that candidate
        Pointer  = min([(c, Hops[c]) for c in Candidates], key=lambda x: x[1])[0]
        OptimalArray.append(Pointer)

    return reversed(OptimalArray)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
