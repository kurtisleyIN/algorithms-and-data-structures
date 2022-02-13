# python3
# Input: A match score (m)
#        A mismatch penalty (mu)
#        A gap penalty (sigma)
#        A gap extension penalty (epsilon)
#        Two strings (string1 and string2)
# Output: The maximum alignment score using affine gap penalites
#         The corresponding alignment

import sys


def global_alignment_affine_gap_penalty(m, mu, sigma, epsilon, string1, string2):
    
    S = [[[0]*(len(string1)+1) for _ in range(len(string2)+1)] for k in range(3)]
    backtrack = [[[0]*(len(string1)+1) for _ in range(len(string2)+1)] for k in range(3)]

    # Initialize the edges with the given penalties.
    for i in range(1, len(string1)+1):
        S[0][i][0] = -sigma - (i-1)*epsilon
        S[1][i][0] = -sigma - (i-1)*epsilon
        S[2][i][0] = -10*sigma
    for j in range(1, len(string2)+1):
        S[2][0][j] = -sigma - (j-1)*epsilon
        S[1][0][j] = -sigma - (j-1)*epsilon
        S[0][0][j] = -10*sigma

    # Fill in the scores for the lower, middle, upper, and backtrack matrices.
    for i in range(1, len(string1)+1):
        for j in range(1, len(string2)+1):
            lower_scores = [S[0][i-1][j] - epsilon, S[1][i-1][j] - sigma]
            S[0][i][j] = max(lower_scores)
            backtrack[0][i][j] = lower_scores.index(S[0][i][j])

            upper_scores = [S[2][i][j-1] - epsilon, S[1][i][j-1] - sigma]
            S[2][i][j] = max(upper_scores)
            backtrack[2][i][j] = upper_scores.index(S[2][i][j])

            middle_scores = [S[0][i][j], S[1][i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], S[2][i][j]]
            S[1][i][j] = max(middle_scores)
            backtrack[1][i][j] = middle_scores.index(S[1][i][j])

   # Initialize the values of i, j and the aligned sequences.
    i,j = len(string1), len(string2)
    string1_aligned, string2_aligned = string1, string2

    # Get the maximum score, and the corresponding backtrack starting position.
    matrix_scores = [S[0][i][j], S[1][i][j], S[2][i][j]]
    max_score = max(matrix_scores)
    backtrack_matrix = matrix_scores.index(max_score)

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to the edge of the matrix starting bottom right.
    while i*j != 0:
        if backtrack_matrix == 0:  # Lower backtrack matrix conditions.
            if backtrack[0][i][j] == 1:
                backtrack_matrix = 1
            i -= 1
            string2_aligned = insert_indel(string2_aligned, j)

        elif backtrack_matrix == 1:  # Middle backtrack matrix conditions.
            if backtrack[1][i][j] == 0:
                backtrack_matrix = 0
            elif backtrack[1][i][j] == 2:
                backtrack_matrix = 2
            else:
                i -= 1
                j -= 1

        else:  # Upper backtrack matrix conditions.
            if backtrack[2][i][j] == 1:
                backtrack_matrix = 1
            j -= 1
            string1_aligned = insert_indel(string1_aligned, i)

    # Prepend the necessary preceeding indels to get to (0,0).
    for _ in range(i):
        string2_aligned = insert_indel(string2_aligned, 0)
    for _ in range(j):
        string1_aligned = insert_indel(string1_aligned, 0)

    return str(max_score), string1_aligned, string2_aligned


if __name__ == "__main__":
    m,mu,sigma,epsilon = map(int,sys.stdin.readline().strip().split())
    string1,string2 = [sys.stdin.readline().strip() for _ in range(2)]
    score = global_alignment_affine_gap_penalty(m,mu,sigma,epsilon,string1,string2)
    print('\n'.join(score))
    
