# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
# Output: A boolean formula in conjunctive normal form (CNF). 
#         Satisfiable if it is possible to color the vertices of the graph in 3 colors such that any two vertices connected by an edge are different colors
#         Unsatisfiable if not

import itertools

vert, edge = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(edge)]

def printEquisatisfiableSatFormula():
    list_formulas = ['']
    var_map = {}
    counter = 1
    for vertex in range(1, vert+1):
        vars = []
        for i in range(1,4):
            vertex_var = str(vertex) + str(i)
            var_map[vertex_var] = counter
            counter += 1
            vars.append(str(var_map[vertex_var]))
        list_formulas += exactly_one_of(vars)
    for source, sink in edges:
        for i in range(1,4):
            source_var = str(source) + str(i)
            sink_var = str(sink) + str(i)
            list_formulas.append('-{} -{} 0'.format(var_map[source_var], var_map[sink_var]))
    list_formulas[0] = '{} {}'.format(len(list_formulas)-1, 3*vert)
    print('\n'.join(list_formulas))

def exactly_one_of(iterable):
    new_iterable = []
    new_iterable.append(' '.join(iterable + ['0']))
    for var1, var2 in itertools.combinations(iterable, 2):
        new_iterable.append('-{} -{} 0'.format(var1, var2))
    return new_iterable

def pycosat_input(list_formulas):
    list_expressions = []
    list_expressions = [[int(i) for i in (formula[:-2].split(' '))] for formula in list_formulas[1:]]
    print(list_expressions)
    return list_expressions


printEquisatisfiableSatFormula()