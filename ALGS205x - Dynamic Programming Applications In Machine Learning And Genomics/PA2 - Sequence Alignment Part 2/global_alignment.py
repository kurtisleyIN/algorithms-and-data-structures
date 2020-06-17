# python3

import sys

def global_alignment(m,mu,sigma,string1,string2):

    # Initialize the matrices.
    S = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]
    backtrack = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]

    # Initialize the edges with the given penalties.
    for col in range(1, len(string1)+1):
        S[0][col] = col*-sigma
    for row in range(1, len(string2)+1):
        S[row][0] = row*-sigma

    # Fill in the Score and Backtrack matrices.
    for col in range(1, len(string1)+1):
        for row in range(1, len(string2)+1):
            FromTheTop = (S[row-1][col] - sigma, S[row-1][col], 0)
            FromTheLeft = (S[row][col-1] - sigma, S[row][col-1], 1)
            if string1[col-1] == string2[row-1]:
                Diagonal = (S[row-1][col-1] + m, S[row-1][col-1], 2)
            else:
                Diagonal = (S[row-1][col-1] - mu, S[row-1][col-1], 2)
                
            Candidates = [FromTheTop, FromTheLeft, Diagonal]
            Candidates = sorted(Candidates, reverse = True, key = lambda x: (x[0], x[1]))
            S[row][col] = Candidates[0][0]
            backtrack[row][col] = Candidates[0][2]
            
    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    string1_aligned, string2_aligned = string1, string2

    # Get the position of the highest scoring cell in the matrix and the high score.
    col, row = len(string1), len(string2)
    max_score = str(S[row][col])

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while row*col != 0:
        if backtrack[row][col] == 0:
            row -= 1
            string1_aligned = insert_indel(string1_aligned, col)
        elif backtrack[row][col] == 1:
            col -= 1
            string2_aligned = insert_indel(string2_aligned, row)
        else:
            row -= 1
            col -= 1

    # Prepend the necessary preceeding indels to get to (0,0).
    for _ in range(row):
        string1_aligned = insert_indel(string1_aligned, 0)
    for _ in range(col):
        string2_aligned = insert_indel(string2_aligned, 0)

    return max_score, string1_aligned, string2_aligned

if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    string1,string2 = [sys.stdin.readline().strip() for _ in range(2)]
    alignment = global_alignment(m,mu,sigma,string1,string2)
    print('\n'.join(alignment))





