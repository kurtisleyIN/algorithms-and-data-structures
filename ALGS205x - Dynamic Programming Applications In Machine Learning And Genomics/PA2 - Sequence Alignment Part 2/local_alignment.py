# python3

import sys

def local_alignment(m,mu,sigma,string1,string2):

    # Initialize the matrices.
    S = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]
    backtrack = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]
    max_score, max_row, max_col = 0, 0, 0

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

            if S[row][col] > max_score:
                max_score, max_row, max_col = S[row][col], row, col

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Get the position of the highest scoring cell in the matrix.
    row,col = max_row, max_col

    # Initialize the aligned strings as the input strings up to the position of the high score.
    string1_aligned, string2_aligned = string1[:col], string2[:row]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    while row*col != 0:
        if backtrack[row][col] == 0:
            row -= 1
            string1_aligned = insert_indel(string1_aligned, col)
        elif backtrack[row][col] == 1:
            col -= 1
            string2_aligned = insert_indel(string2_aligned, row)
        elif backtrack[row][col] == 2:
            row -= 1
            col -= 1

    # Cut the strings at the ending point of the backtrack.
    string1_aligned = string1_aligned[col:]
    string2_aligned = string2_aligned[row:]

    return str(max_score), string1_aligned, string2_aligned

alignment = local_alignment(3,2,1,'CAGAGATGGCCG','ACG')
print('\n'.join(alignment))

if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    string1,string2 = [sys.stdin.readline().strip() for _ in range(2)]
    alignment = local_alignment(m,mu,sigma,string1,string2)
    print('\n'.join(alignment))
    
    
    