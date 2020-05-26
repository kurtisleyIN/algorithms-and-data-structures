# python3
# Input: An integer (n) that denotes length of the following sequences
#        Sequence of integers (PPC) that denotes profit-per-click of the ith ad
#        Sequence of integers (ANC) that denotes average number of clicks of the ith day
# Output: The maximum value that can attained by dot product
import sys

def max_dot_product(PPC, ANC):
    IndexLookupA = sorted(range(len(PPC)), key = lambda k: PPC[k], reverse = True)
    IndexLookupB = sorted(range(len(ANC)), key = lambda k: ANC[k], reverse = True)
    
    DP = 0
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