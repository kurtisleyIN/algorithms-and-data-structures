# python3

import sys
from collections import defaultdict

def deBruijnGraph(kmers):
    k = len(kmers[0])
    graph = {}
    for i in range(len(kmers)):
        try:
            graph[kmers[i][:-1]].append(kmers[i][1:])
        except:
            graph[kmers[i][:-1]] = [kmers[i][1:]]
    return graph


def traverse(tree, root):
    out = []
    for r in tree[root]:
        if r != root and r in tree:
            out += traverse(tree, r)
        else:
            out.append(r)
    return out

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    kmers = [line.strip() for line in sys.stdin if line.strip()]
    
    graph = deBruijnGraph(kmers)

    degrees = defaultdict(int)
    for k in graph:
        for v in graph[k]:
            degrees[k] += 1
            degrees[v] -= 1
    source = [k for k, v in degrees.items() if v == 1][0]
    sinc = [k for k, v in degrees.items() if v == -1][0]
    list(graph)
    start = list(graph)[0]
    # not sure what to do with this start = graph.keys()[0]
    #print 'source: %s, sinc: %s' % (source, sinc)
    
    if sinc in graph.keys():
        graph[sinc].append(source)
    else:
        graph[sinc] = [source]
    
    cycles = {}
    while graph:
        current = next(iter(graph))
        cycle = [current]
        cycles[current] = cycle
        while current in graph:
            _next = graph[current][0]
            del graph[current][0]
            if len(graph[current]) == 0:
                del graph[current]
            current = _next
            cycle.append(_next)
    
    cycle = traverse(cycles, start)
    for i in range(1, len(cycle)):
        if cycle[i-1] == sinc and cycle[i] == source:
            boarder = i
    path = cycle[boarder:]+cycle[1:boarder]
    print (*((([s[0] for s in list(path)]) + list(path[-1][1:]))),sep = '')
