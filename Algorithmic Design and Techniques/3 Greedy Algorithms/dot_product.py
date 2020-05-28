# python3
# Input: An integer (n) that denotes length of the following sequences
#        Sequence of integers (PPC) that denotes profit-per-click of the ith ad
#        Sequence of integers (ANC) that denotes average number of clicks of the ith day
# Output: The maximum value that can attained by dot product

import sys

def max_dot_product(PPC, ANC):
    
    # Sort the indexes of the PPC and ANC arrays in decreasing order based on their values
    IndexLookupA = sorted(range(len(PPC)), key = lambda k: PPC[k], reverse = True)
    IndexLookupB = sorted(range(len(ANC)), key = lambda k: ANC[k], reverse = True)
    
    # Initilize the dot product as 0
    DP = 0
    
    # Loop through both array and add their product to DP
    for i, j in zip(IndexLookupA, IndexLookupB):
        DP += PPC[i]*ANC[j]
        
    return DP

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    PPC = data[1:(n + 1)]
    ANC = data[(n + 1):]
    print(max_dot_product(PPC, ANC))