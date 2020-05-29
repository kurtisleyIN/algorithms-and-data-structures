# python3

import itertools
import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

class Vertex:
    def __init__(self,u):
        self.index = u
        self.value = -1
        self.out_neighbors = [] 
        self.in_neighbors = [] 
        self.scc = set() 
        self.root = False 

        self.lowlink = -1
        self.discovered = -1
        self.on_stack = False

def isSatisfiable():
    graph = construct_implication_graph(clauses)
    roots = find_SCCs(graph, tarjans)

    for vertex in roots:
        if -vertex in graph[vertex].scc:
            return None
        for literal in graph[vertex].scc:
            if -literal in graph[vertex].scc:
                return None
    
    result = [None] * n
    for scc_root in roots:

        for literal in graph[scc_root].scc:
            if graph[literal].value == -1:
                graph[literal].value = 1

                result[abs(literal) - 1] = literal

                graph[-literal].value = 0

    return result

def construct_implication_graph(clauses):
    graph = {}
    for i in range(1,n+1):
        graph[i] = Vertex(i)
        graph[-i] = Vertex(-i)
    for clause in clauses:
        u = clause[0]
        if len(clause) == 1:

            graph[-u].out_neighbors.append(u)
            graph[u].in_neighbors.append(-u)

        elif len(clause) == 2:
            v = clause[1]

            graph[-u].out_neighbors.append(v)
            graph[v].in_neighbors.append(-u)
            graph[-v].out_neighbors.append(u)
            graph[u].in_neighbors.append(-v)
    return graph

def find_SCCs(graph, function):
    return function(graph)

def kosaraju(graph):
    L = []
    explored = set()
    for vertex in graph.keys():
        visit(vertex, graph, explored, L)
    assigned = set()
    roots = []
    for vertex in L:
        assign(vertex, vertex, graph, assigned, roots)

    return roots

def tarjans(graph):
    
    index = 0
    stack = []
    roots = []
    for vertex in graph.keys():
        if graph[vertex].discovered == -1:
            strongconnect(graph[vertex], stack, index, graph, roots)
    return roots

def strongconnect(vertex, stack, index, graph, roots):
    
    vertex.discovered = index
    vertex.lowlink = index
    index += 1
    stack.append(vertex)
    vertex.on_stack = True

    for out_vertex_index in vertex.out_neighbors:
        if graph[out_vertex_index].discovered == -1:

            strongconnect(graph[out_vertex_index], stack, index, graph, roots)
            vertex.lowlink = min(vertex.lowlink, graph[out_vertex_index].lowlink)
        elif graph[out_vertex_index].on_stack:
            vertex.lowlink = min(vertex.lowlink, graph[out_vertex_index].discovered)

    if vertex.discovered == vertex.lowlink:
        while len(stack) != 0:
            v = stack.pop(-1)
            vertex.scc.add(v.index)
            v.on_stack = False

            if v == vertex:
                break

        roots.append(vertex.index)

def visit(u, graph, explored, L):
    if u not in explored:
        explored.add(u)
        L.insert(0, u)
        for v in graph[u].out_neighbors:
            visit(v, graph, explored, L)

def assign(u, root, graph, assigned, roots):
    if u not in assigned:
        graph[root].scc.add(u)
        assigned.add(u)
        if u == root:
            graph[u].root = True
            roots.append(u)
        for v in graph[u].in_neighbors:
            assign(v, root, graph, assigned, roots)

def main():
    result = isSatisfiable()
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");
        print(" ".join([str(i) for i in result]))

threading.Thread(target=main).start()