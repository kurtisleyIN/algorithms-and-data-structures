# python3
# Input: An integer (n)
#        A sequence of integers (PartArray)
# Output: 1 if possible to partition A into three subsets of equal sums (0 otherwise)
import sys

def partition3(PartArray):
    total = sum(PartArray)
    if len(PartArray) < 3 or total % 3:  # 1
        return 0
    third = total // 3
    table = [[0] * (len(PartArray) + 1) for _ in range(third + 1)]  # 2
 
    for i in range(1, third + 1):
        for j in range(1, len(PartArray) + 1):  # 3
            ii = i - PartArray[j - 1]  # 4
            if PartArray[j - 1] == i or (ii > 0 and table[ii][j - 1]):  # 5
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]  # 6
 
    return 1 if table[-1][-1] == 2 else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *PartArray = list(map(int, input.split()))
    print(partition3(PartArray))

