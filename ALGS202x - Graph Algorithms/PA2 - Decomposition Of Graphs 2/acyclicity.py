# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
# Output: 1 if the graph contains a cycle, 0 if not

import sys

def explore(AdjacentList, x, VisitedList):
    for i in AdjacentList[x]:
        if not VisitedList[i]:
            VisitedList[i] = True
            explore(AdjacentList, i, VisitedList)
    return

def acyclic(AdjacentList):
    acyclic = 0
    for i in range(len(AdjacentList)):
        VisitedList = [False] * len(AdjacentList)
        explore(AdjacentList, i, VisitedList)
        if VisitedList[i]:
            acyclic = 1
            break
    return acyclic

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 *edge):2], data[1:(2 *edge):2]))
    AdjacentList = [[] for _ in range(vert)]
    for (a, b) in edges:
        AdjacentList[a - 1].append(b - 1)
    print(acyclic(AdjacentList))
