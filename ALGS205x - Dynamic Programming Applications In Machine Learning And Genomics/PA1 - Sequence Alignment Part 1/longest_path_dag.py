# python3
# Input: An integer (source) for the source node
#        An integer (sink) for the sink node
#        A directed acyclic graph with the edges and edge weights
# Output: The length of the longest path from the source node to the sink node

import sys

def topological_ordering(graph):
    graph = set(graph)
    ordering = []
    candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})

    while len(candidates) != 0:
        ordering.append(candidates[0])

        temp_nodes = []
        EdgeIteration = list(filter(lambda e: e[0] == candidates[0], graph))
        for edge in EdgeIteration:
            graph.remove(edge)
            temp_nodes.append(edge[1])

        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                candidates.append(node)

        candidates = candidates[1:]

    return ordering


def longest_path(graph, edges, source, sink):

    top_order = topological_ordering(graph.keys())
    top_order = top_order[top_order.index(source)+1:top_order.index(sink)+1]

    S = {node:-100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}
    S[source] = 0
    backtrack = {node:None for node in top_order}

    for node in top_order:
        try:
            S[node], backtrack[node] = max(map(lambda e: [S[e[0]] + graph[e], e[0]], filter(lambda e: e[1] == node, graph.keys())), key=lambda p:p[0])

        except ValueError:
            pass

    path = [sink]
    while path[0] != source:
        path = [backtrack[path[0]]] + path

    return S[sink], path   
    

if __name__ == "__main__":
    source = int(sys.stdin.readline().strip())
    sink = int(sys.stdin.readline().strip())
    edges = {}
    edge_weight = {}
    
    for pair in [line.strip().split('->') for line in sys.stdin.readlines()]:
        if int(pair[0]) not in edges:
            edges[int(pair[0])] = [int(pair[1].split(':')[0])]
        else:
            edges[int(pair[0])].append(int(pair[1].split(':')[0]))

        edge_weight[int(pair[0]), int(pair[1].split(':')[0])] = int(pair[1].split(':')[1])
    
    length, path = longest_path(edge_weight, edges, source, sink)
    print(length)
    print('->'.join(map(str, path)))