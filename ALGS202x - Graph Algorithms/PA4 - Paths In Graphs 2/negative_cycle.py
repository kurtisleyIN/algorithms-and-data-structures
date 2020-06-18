# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected and the weight/cost of each edge
# Output: 1 if it contains a negative cycle, 0 if not

import sys

def negative_cycle(AdjacentList, cost):
    dist = [-1] * len(AdjacentList)
    prev = [-1] * len(AdjacentList)

    dist[0] = 0

    for i in range(len(AdjacentList)):
        for j in range(len(AdjacentList)):
            for ind,k in enumerate(AdjacentList[j]):
                jkCost = cost[j][ind]
                if dist[k] > dist[j] + jkCost:
                    dist[k] = dist[j] + jkCost
                    prev[k] = j

        if i == len(AdjacentList)-2:
            dist_Vminus1 = list(dist)
        if i == len(AdjacentList)-1:
            dist_V = list(dist)

    if dist_Vminus1 == dist_V:
        return 0
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3*edge):3], data[1:(3*edge):3]), data[2:(3*edge):3]))
    data = data[3*edge:]
    AdjacentList = [[] for _ in range(vert)]
    cost = [[] for _ in range(vert)]
    for ((a, b), w) in edges:
        AdjacentList[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(AdjacentList, cost))