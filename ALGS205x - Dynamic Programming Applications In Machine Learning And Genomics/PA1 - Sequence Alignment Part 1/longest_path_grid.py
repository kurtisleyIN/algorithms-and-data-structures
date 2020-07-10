# python3
# Input: An integer (n) for the number of rows
#        An integer (m) for the number of columns
#        A matrix (down) for the down weights
#        A matrix (right) for the right weights
# Output: The length of the longest path from the source (0,0) to the sink (n,m)

import sys

def longest_path(n, m, down, right):

    S = [[0]*(m+1) for i in range(n+1)]

    # Compute the first row and column.
    for i in range(1,n+1):
        S[i][0] = S[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        S[0][j] = S[0][j-1] + right[0][j-1]

    # Compute the interior values.
    for i in range(1,n+1):
        for j in range(1,m+1):
            S[i][j] = max(S[i-1][j]+down[i-1][j], S[i][j-1] + right[i][j-1])

    return S[n][m]

if __name__ == "__main__":
    n,m = map(int, sys.stdin.readline().strip().split())
    down = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(n)]
    sys.stdin.readline()
    right = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(n+1)]

    print(longest_path(n,m,down,right))