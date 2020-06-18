# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected and the weight/cost of each edge
#        Last integer is the vertex in question
# Output: '*' if no path, '-' if path exists but it's -Infinity, or the length of the shortest path for every vertex

import sys

def explore(AdjacentList,x,visited,shortest):
    for i in AdjacentList[x]:
        if not visited[i]:
            visited[i] = True
            shortest[i] = 0
            explore(AdjacentList,i,visited,shortest)
    return


def innerLoop(s,AdjacentList,dist,prev):
    
    for j in range(len(AdjacentList)):
        for ind,k in enumerate(AdjacentList[j]):
            jkCost = cost[j][ind]
            if dist[k] > dist[j] + jkCost:
                dist[k] = dist[j] + jkCost
                prev[k] = j    

def shortet_paths(AdjacentList, cost, s, dist, reachable, shortest, prev):
    dist[s] = 0
    
    for i in range(len(AdjacentList)-1):
        innerLoop(s,AdjacentList,dist,prev)
    dist_Vminus1 = list(dist)

    innerLoop(s,AdjacentList,dist,prev)     

    dist_V = list(dist)
             
    changed = [i for i,val in enumerate(dist_Vminus1) if val != dist_V[i]]   

    for i in changed:
        nextV = i

        shortest[nextV] = 0

        for j in range(len(AdjacentList)):
            nextV = prev[nextV]
        shortest[nextV] = 0
        
        visited = [False] * len(AdjacentList)        
        explore(AdjacentList,nextV,visited,shortest)
                    
    for ind,i in enumerate(dist):
        if i == float('inf'):
            reachable[ind] = 0
        else:
            reachable[ind] = 1
    pass

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
    s = data[0]
    s -= 1
    dist = [float('inf')] * vert
    reachable = [0] * vert
    prev      = [-1] * vert
    shortest = [1] * vert
    shortet_paths(AdjacentList, cost, s, dist, reachable, shortest, prev)

    
    for x in range(vert):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(dist[x])