# python3
# Input: A match score (m)
#        A mismatch penalty (mu)
#        A gap penalty (sigma)
#        Two strings (string1 and string2)
# Output: The maximum alignment score of a fitting alignment
#         The corresponding alignment

import sys

def fitting_alignment(m,mu,sigma,string1,string2):

    S = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]
    backtrack = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]

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
            
    # Get the position of the highest scoring cell corresponding to the end of string2.
    row = len(string2)
    col = len(string1) - max(enumerate([S[row][col] for col in range(len(string1), len(string2)-1, -1)]), key=lambda x: x[1])[0]
    max_score = str(S[row][col])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    string1_aligned, string2_aligned = string1[:col], string2[:row]

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to start of the fitting alignment.
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

    # Cut off v at the ending point of the backtrack.
    string1_aligned = string1_aligned[col:]

    return max_score, string1_aligned, string2_aligned

if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    string1, string2 = [sys.stdin.readline().strip() for _ in range(2)]
    alignment = fitting_alignment(m,mu,sigma,string1,string2)
    print('\n'.join(alignment))