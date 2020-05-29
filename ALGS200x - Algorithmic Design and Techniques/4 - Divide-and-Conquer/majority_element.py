# python3
# Input: An integer (n)
#        A sequence of non-negative integers (MajArray)
# Output: 1 if the sequence contains an element that appears strictly more than n/2 times (0 if otherwise)

import sys

def get_majority_element(MajArray, LI, RI):
    
    # Exit statement for recursive calls
    if LI == RI - 1:
        return MajArray[LI]
    
    # Recursively splitting MajArray into a tree of sub-arrays
    LeftMajority = get_majority_element(MajArray, LI, (LI + RI - 1)//2 + 1)
    RightMajority = get_majority_element(MajArray, (LI + RI - 1)//2 + 1, RI)
    
    # Determines if the majority element is on the left/right side for each sub-array, -1 if it doesn't exist
    LeftCount = 0
    for i in range(LI, RI):
        if MajArray[i] == LeftMajority:
            LeftCount += 1
    if LeftCount > (RI-LI)//2:
        return LeftMajority
    
    RightCount = 0
    for i in range(LI, RI):
        if MajArray[i] == RightMajority:
            RightCount += 1
    if RightCount > (RI-LI)//2:
        return RightMajority
    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *MajArray = list(map(int, input.split()))
    if get_majority_element(MajArray, 0, n) != -1:
        print(1)
    else:
        print(0)
