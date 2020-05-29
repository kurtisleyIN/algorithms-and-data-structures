# python3
# Input:
# Output:

import sys
import math

def distance(v1,v2,x,y):
    return math.sqrt((x[v1]-x[v2])**2 +  (y[v1]-y[v2])**2) 
    

def clustering(x, y, k):
    edges = []
    for i in range(len(x)):
        for j in range(i,len(x)):
            if i != j:
                edges.append([i,j,distance(i,j,x,y)])

    sorted_Edges = sorted(edges, key=lambda tup: tup[2])
    
    for i in sorted_Edges:
        pass
       
    membership = range(n)

    MST = []
    minDist = 0
    for i in sorted_Edges:
        if membership[i[0]] != membership[i[1]]:
            if len(set(membership)) == k:
                nextEdge = i
                break
            MST.append(i)
            minDist += i[2]
            membership = list(map(lambda x: membership[i[0]] if x == membership[i[1]] else x, membership))
    return nextEdge[2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))