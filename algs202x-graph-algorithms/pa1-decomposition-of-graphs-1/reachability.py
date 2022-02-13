# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
#        Last pair of vertices are the vertices in question
# Output: Output 1 if there is a path between this pair, 0 if not

import sys

# Recursively search
def explore(AdjacentList, x, VisitedList):
    for i in AdjacentList[x]:
        if not VisitedList[i]:
            VisitedList[i] = True
            explore(AdjacentList, i, VisitedList)
    return VisitedList

def reach(AdjacentList, x, y):
    # Initialize the visited list
    VisitedList = [False] * len(AdjacentList)
    
    # Explore all reachable vertices from x
    explore(AdjacentList, x, VisitedList)
    if VisitedList[y]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*edge):2], data[1:(2*edge):2]))
    
    # Assign last pair of vertices
    x, y = data[2*edge:]
    x -= 1
    y -= 1
    
    # Place edges into Adjacent list
    AdjacentList = [[] for _ in range(vert)]
    for (a, b) in edges:
        AdjacentList[a - 1].append(b - 1)
        AdjacentList[b - 1].append(a - 1)
    print(reach(AdjacentList, x, y))
