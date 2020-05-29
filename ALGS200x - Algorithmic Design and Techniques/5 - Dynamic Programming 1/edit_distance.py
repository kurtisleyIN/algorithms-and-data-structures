# python3
# Input: Two strings of lowercase letters (s and t)
# Output: The edit distance between s and t

def edit_distance(string1, string2):

    # Create matrix where the first row/col are the indexes for each character in both strings
    DistanceMatrix = [[x] + [0] * (len(string2)) for x in range(len(string1) + 1)]
    DistanceMatrix[0] = [x for x in range(len(string2) + 1)]

    # Loop through all character positions
    for row in range(1, len(string1) + 1):
        for col in range(1, len(string2) + 1):
            # If the letters match, copy the diagonal over
            if string1[row - 1] == string2[col - 1]:
                DistanceMatrix[row][col] = DistanceMatrix[row - 1][col - 1]
            # If the letters don't match, copy over the minimum adajcent value and add 1
            else:
                DistanceMatrix[row][col] = min(DistanceMatrix[row][col - 1], 
                                               DistanceMatrix[row - 1][col], 
                                               DistanceMatrix[row - 1][col - 1]) + 1
    return DistanceMatrix[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
