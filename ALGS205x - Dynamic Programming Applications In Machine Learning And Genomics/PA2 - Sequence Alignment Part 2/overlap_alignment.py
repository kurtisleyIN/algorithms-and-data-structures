# python3
# Input: A match score (m)
#        A mismatch penalty (mu)
#        A gap penalty (sigma)
#        Two strings (string1 and string2)
# Output: The maximum alignment score of an overlap alignment
#         The corresponding alignment

import sys

def overlap_alignment(m,mu,sigma,string1,string2):

    S = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]
    backtrack = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]
    
    # Initialize the max score.
    max_score = -3*(len(string1) + len(string2))

    # Fill in the Score and Backtrack arrays.
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

            # Check if we have a new maximum along the last row or column and update accordingly.
            if col == len(string1) or row == len(string2):
                if S[row][col] > max_score:
                    max_score = S[row][col]
                    max_indices = (row, col)

    # Initialize i and j as their corresponding index of the maximum score.
    row, col = max_indices

    # Initialize the aligned strings as the input strings, removing the unused tails.
    string1_aligned, string2_aligned = string1[:col], string2[:row]

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to the first row or column from the highest score in the last row or column.
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

    # Remove the unused head the aligned strings.
    string1_aligned, string2_aligned = string1_aligned[col:], string2_aligned[row:]

    return str(max_score), string1_aligned, string2_aligned

alignment = overlap_alignment(1,1,5,'ATCACT','ATG')
print('\n'.join(alignment))

if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]
    alignment = overlap_alignment(m,mu,sigma,s,t)
    print('\n'.join(alignment))