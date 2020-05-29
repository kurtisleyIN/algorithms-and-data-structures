# python3
# Input:
# Output:

from itertools import permutations
INF = 10 ** 9

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.best_weight = INF
        self.best_path = []

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return Graph(graph)

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def optimal_path(graph):
    n = len(graph.graph)
    best_ans = INF
    best_path = []

    find_optimal_path(graph, 0, 0, set(), 0, [])
    
    if graph.best_weight == INF:
        return (-1, [])
    return (graph.best_weight, [x + 1 for x in graph.best_path])

def find_optimal_path(graph, from_vertex, to_vertex, explored, cur_weight, cur_path):
    """ solves TSPs using the branch and bound technique. Unfortunately still too slow. """
    if from_vertex != to_vertex:
        cur_weight += graph.graph[from_vertex][to_vertex]
    explored.add(to_vertex)
    cur_path.append(to_vertex)

    if len(explored) == len(graph.graph) and graph.graph[to_vertex][0] != INF:
        cur_weight += graph.graph[to_vertex][0]
        if cur_weight < graph.best_weight:
            graph.best_weight = cur_weight
            graph.best_path = cur_path
            return
        
    if cur_weight > graph.best_weight:
        return

    weights_list = [i for i in range(len(graph.graph)) if i not in explored]

    for unexplored_vertex in weights_list:
        find_optimal_path(graph, to_vertex, unexplored_vertex, explored.copy(), cur_weight, cur_path[:])

if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))