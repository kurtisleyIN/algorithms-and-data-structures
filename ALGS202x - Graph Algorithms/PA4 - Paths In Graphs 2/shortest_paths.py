# python3
# Input:
# Output:

import sys

def explore(adj,x,visited,shortest):
    for i in adj[x]:
        if not visited[i]:
            visited[i] = True
            shortest[i] = 0
            explore(adj,i,visited,shortest)
    return


def innerLoop(s,adj,dist,prev):
    
    for j in range(len(adj)):
        for ind,k in enumerate(adj[j]):
            jkCost = cost[j][ind]
            if dist[k] > dist[j] + jkCost:
                dist[k] = dist[j] + jkCost
                prev[k] = j    

def shortet_paths(adj, cost, s, dist, reachable, shortest, prev):
    dist[s] = 0
    
    for i in range(len(adj)-1):
        innerLoop(s,adj,dist,prev)
    dist_Vminus1 = list(dist)

    innerLoop(s,adj,dist,prev)     

    dist_V = list(dist)
             
    changed = [i for i,val in enumerate(dist_Vminus1) if val != dist_V[i]]   

    for i in changed:
        nextV = i

        shortest[nextV] = 0

        for j in range(len(adj)):
            nextV = prev[nextV]
        shortest[nextV] = 0
        
        visited = [False] * len(adj)        
        explore(adj,nextV,visited,shortest)
                    
    for ind,i in enumerate(dist):
        if i == float('inf'):
            reachable[ind] = 0
        else:
            reachable[ind] = 1
    pass

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    dist = [float('inf')] * n
    reachable = [0] * n
    prev      = [-1] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, dist, reachable, shortest, prev)

    
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(dist[x])