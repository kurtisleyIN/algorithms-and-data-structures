# python3
# Input: An integer (n)
#        A sequence of integers (PartArray)
# Output: 1 if possible to partition A into three subsets of equal sums (0 otherwise)

import sys

def partition3(PartArray):
    
    # If the array length is less than 3, or SumArray is not divisible by 3, return 0
    ArraySum = sum(PartArray)
    if len(PartArray) < 3 or ArraySum % 3:
        return 0
    
    # Calculate the third and create a grid with the PartArray length as the rows and range of Third as the cols
    Third = ArraySum // 3
    Grid = [[0] * (len(PartArray) + 1) for _ in range(Third + 1)]
 
    # Loop through every row and column
    for row in range(1, Third + 1):
        for col in range(1, len(PartArray) + 1):
            # 
            ii = row - PartArray[col - 1]
            if PartArray[col - 1] == row or (ii > 0 and Grid[ii][col - 1]):
                Grid[row][col] = 1 if Grid[row][col - 1] == 0 else 2
            else:
                Grid[row][col] = Grid[row][col - 1]
 
    return 1 if Grid[-1][-1] == 2 else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *PartArray = list(map(int, input.split()))
    print(partition3(PartArray))

