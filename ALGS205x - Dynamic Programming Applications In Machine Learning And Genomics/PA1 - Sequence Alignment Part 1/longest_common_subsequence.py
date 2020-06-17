# python3

import sys

def LCS(string1, string2):
    S = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                S[i+1][j+1] = S[i][j]+1
            else:
                S[i+1][j+1] = max(S[i+1][j],S[i][j+1])

    # Recover a maximum substring.
    longest_sseq = ''
    i,j = len(string1), len(string2)
    while i*j != 0:
        if S[i][j] == S[i-1][j]:
            i -= 1
        elif S[i][j] == S[i][j-1]:
            j -= 1
        else:
            longest_sseq = string1[i-1] + longest_sseq
            i -= 1
            j -= 1

    return longest_sseq


if __name__ == "__main__":
    string1, string2 = sys.stdin.read().strip().splitlines()
    print(LCS(string1, string2))