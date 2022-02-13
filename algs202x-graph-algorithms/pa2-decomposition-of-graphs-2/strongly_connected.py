# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
# Output: The number of strongly connected components

import sys
import numpy as np

sys.setrecursionlimit(200000)

def dfs(AdjacentList, visited, postOrder,clock, x):
    visited[x] = True
    for i in AdjacentList[x]:
        if not visited[i]:
            dfs(AdjacentList,visited,postOrder,clock,i)      
    clock[0] += 1
    postOrder[x] = clock[0]  
    return

def number_of_strongly_connected_components(AdjacentList,AdjacentReverse):
    result = 0
    #write your code here

    postOrder = [0] * len(AdjacentList)
    #initialize visited with removed list
    visited   =  [False] * len(AdjacentList)
    clock = [0]
    #find a sink by finding a source in the reverse graph
    #a vertex in the source compoenent will have a higher postorder than
    #those that are not sources
    for i in range(len(AdjacentReverse)):
        if not visited[i]:
            dfs(AdjacentReverse,visited,postOrder,clock,i)
    
    #get reverse post order
    reversePostOrder = np.argsort(postOrder)[::-1]

    #reinit visisted
    visited   =  [False] * len(AdjacentList)
    #run dfs on the real adjency list in reverse sort order.  count every time a dfs starts fresh from the top on an unvisited node
    for i in reversePostOrder:
        if not visited[i]:
            result += 1
            dfs(AdjacentList,visited,postOrder,clock,i)
        
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*edge):2], data[1:(2*edge):2]))
    AdjacentList = [[] for _ in range(vert)]
    for (a, b) in edges:
        AdjacentList[a - 1].append(b - 1)
    #reverse graph
    AdjacentReverse = [[] for _ in range(vert)]
    for (a, b) in edges:
        AdjacentReverse[b - 1].append(a - 1)

    print(number_of_strongly_connected_components(AdjacentList,AdjacentReverse))
