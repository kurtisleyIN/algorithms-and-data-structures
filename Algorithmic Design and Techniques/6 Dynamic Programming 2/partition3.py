# python3
import sys

def partition3(A):
    total = sum(A)
    if len(A) < 3 or total % 3:  # 1
        return 0
    third = total // 3
    table = [[0] * (len(A) + 1) for _ in range(third + 1)]  # 2
 
    for i in range(1, third + 1):
        for j in range(1, len(A) + 1):  # 3
            ii = i - A[j - 1]  # 4
            if A[j - 1] == i or (ii > 0 and table[ii][j - 1]):  # 5
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]  # 6
 
    return 1 if table[-1][-1] == 2 else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

