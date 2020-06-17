# python3

import sys

def align(string1, string2, string3):
    '''Returns the alignment of three sequences v, w, and u.'''
    # Initialize the matrices.
    S = [[[0 for k in range(len(string3)+1)] for j in range(len(string2)+1)] for i in range(len(string1)+1)]
    backtrack = [[[0 for k in range(len(string3)+1)] for j in range(len(string2)+1)] for i in range(len(string1)+1)]

    # Fill in the Score and Backtrack matrices.
    for i in range(1, len(string1)+1):
        for j in range(1, len(string2)+1):
            for k in range(1, len(string3)+1):
                scores = [S[i-1][j-1][k-1] + int(string1[i-1] == string2[j-1] == string3[k-1]), S[i-1][j][k], S[i][j-1][k], S[i][j][k-1], S[i-1][j][k-1], S[i][j-1][k-1]]
                backtrack[i][j][k], S[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    string1_aligned, string2_aligned, string3_aligned = string1, string2, string3

    # Get the position of the highest scoring cell in the matrix and the high score.
    i, j, k = len(string1), len(string2), len(string3)
    max_score = S[i][j][k]

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j*k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            string2_aligned = insert_indel(string2_aligned, j)
            string3_aligned = insert_indel(string3_aligned, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            string1_aligned = insert_indel(string1_aligned, i)
            string3_aligned = insert_indel(string3_aligned, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            string1_aligned = insert_indel(string1_aligned, i)
            string2_aligned = insert_indel(string2_aligned, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            string3_aligned = insert_indel(string3_aligned, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            string2_aligned = insert_indel(string2_aligned, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            string1_aligned = insert_indel(string1_aligned, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    # Prepend the necessary preceeding indels to get match lengths.
    while len(string1_aligned) != max(len(string1_aligned),len(string2_aligned),len(string3_aligned)):
        string1_aligned = insert_indel(string1_aligned, 0)
    while len(string2_aligned) != max(len(string1_aligned),len(string2_aligned),len(string3_aligned)):
        string2_aligned = insert_indel(string2_aligned, 0)
    while len(string3_aligned) != max(len(string1_aligned),len(string2_aligned),len(string3_aligned)):
        string3_aligned = insert_indel(string3_aligned, 0)

    return str(max_score), string1_aligned, string2_aligned, string3_aligned

if __name__ == "__main__":
    string1,string2,string3 = [sys.stdin.readline().strip() for _ in range(3)]
    MaxScore, FirstString, SecondString, ThirdString = align(string1,string2,string3)
    print(MaxScore)
    print(FirstString)
    print(SecondString)
    print(ThirdString)