# python3
def edit_distance(s, t):
    len_s = len(s) + 1
    len_t = len(t) + 1

    DistanceMatrix = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    DistanceMatrix[0] = [x for x in range(len_t)]

    for i in range(1, len_s):
        for j in range(1, len_t):
            
            if s[i - 1] == t[j - 1]:
                DistanceMatrix[i][j] = DistanceMatrix[i - 1][j - 1]
            else:
                DistanceMatrix[i][j] = min(DistanceMatrix[i][j - 1], 
                                           DistanceMatrix[i - 1][j], 
                                           DistanceMatrix[i - 1][j - 1]) + 1

    return DistanceMatrix[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
