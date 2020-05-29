# python3
# Input: An integer (n)
#        A sequence of integers (PartArray)
# Output: PartArray in increasing order

import sys
import random

def partition3(PartArray, LI, RI):
    
    # Initialize the pivot, i, and the left/right bounds
    Pivot = PartArray[LI]
    i = LI
    LeftBound = LI
    RightBound = RI
    
    # Only proceed with the swaps if i meets RightBound
    while i <= RightBound:
        
        # If the current element is less than the pivot element, swap the elements at i and LeftBound
        # Increase i, increase LeftBound
        if PartArray[i] < Pivot:
            PartArray[LeftBound], PartArray[i] = PartArray[i], PartArray[LeftBound]
            LeftBound += 1
            
        # If the current element is more than the pivot element, swap the elements at i and RightBound
        # Keep i the same, decrease RightBound
        elif PartArray[i] > Pivot:
            PartArray[RightBound], PartArray[i] = PartArray[i], PartArray[RightBound]
            RightBound -= 1
            i -= 1
        i += 1
    return LeftBound, RightBound

def randomized_quick_sort(PartArray, LI, RI):
    
    # Exit statement for the recursive calls
    if LI >= RI:
        return
    
    # Selects a random index between the left and right index
    # Element at the random index switches places with the left index
    Rand = random.randint(LI, RI)
    PartArray[LI], PartArray[Rand] = PartArray[Rand], PartArray[LI]

    # Determine two split points and recursively split the array into sub-arrays
    MI1, MI2 = partition3(PartArray, LI, RI)
    randomized_quick_sort(PartArray, LI, MI1 - 1);
    randomized_quick_sort(PartArray, MI2 + 1, RI);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *PartArray = list(map(int, input.split()))
    randomized_quick_sort(PartArray, 0, n - 1)
    for x in PartArray:
        print(x, end=' ')
