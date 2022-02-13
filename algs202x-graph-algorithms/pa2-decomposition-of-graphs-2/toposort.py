# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
# Output: Any topological ordering of its vertices

import sys

def dfs(AdjacentList, UsedList, order, x):
    UsedList[x] = 1
    for i in AdjacentList[x]:
        if not UsedList[i]:
            dfs(AdjacentList,UsedList,order,i)
    order.insert(0,x)
    return

def toposort(AdjacentList):
    UsedList = [0] * len(AdjacentList)
    order = []

    for i in range(len(AdjacentList)):
        if not UsedList[i]:
            dfs(AdjacentList,UsedList,order,i)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*edge):2], data[1:(2*edge):2]))
    AdjacentList = [[] for _ in range(vert)]
    for (a, b) in edges:
        AdjacentList[a - 1].append(b - 1)
    order = toposort(AdjacentList)
    for x in order:
        print(x + 1, end=' ')

