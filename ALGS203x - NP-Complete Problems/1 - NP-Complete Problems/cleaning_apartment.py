# python3
# Input:
# Output:

import itertools

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

def printEquisatisfiableSatFormula():
    list_formulas = ['']
    var_map = {}
    counter = 1
    vars = []

    for vertex in range(1, n+1):
        for position in range(1, n+1):
            vertex_var = str(vertex) * 2 + str(position)
            var_map[vertex_var] = counter
            counter += 1
            vars.append(str(var_map[vertex_var]))
    list_formulas.append(' '.join(vars + ['0']))

    for pos1, pos2 in itertools.combinations([pos for pos in range(1,n+1)], 2):
        for vertex in range(1, n+1):
            vertex_var = str(vertex) * 2 + str(pos1)

            adjacent_var = str(vertex) * 2 + str(pos2)
            list_formulas.append('-{} -{} 0'.format(var_map[vertex_var], var_map[adjacent_var]))

    for position in range(1, n+1):
        same_position_vertices = [str(var_map[str(vertex) * 2 + str(position)]) for vertex in range(1, n+1)]
        list_formulas += exactly_one_of(same_position_vertices)

    for vertex1, vertex2 in itertools.combinations([vertex for vertex in range(1,n+1)], 2):
        if [vertex1, vertex2] not in edges and [vertex2, vertex1] not in edges:
            for i in range(1, n):
                vertex_var = str(vertex1) * 2 + str(i)
                adjacent_var = str(vertex2) * 2 + str(i+1)
                list_formulas.append('-{} -{} 0'.format(var_map[vertex_var], var_map[adjacent_var]))
                
                vertex_var = str(vertex1) * 2 + str(i+1)
                adjacent_var = str(vertex2) * 2 + str(i)
                list_formulas.append('-{} -{} 0'.format(var_map[vertex_var], var_map[adjacent_var]))

    list_formulas[0] = '{} {}'.format(len(list_formulas)-1, len(var_map))
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
    return list_expressions

def sat_solve(list_formulas):
    import pycosat
    solve = pycosat.solve(pycosat_input(list_formulas))
    if type(solve) == list:
        print(list(filter(lambda x: x > 0, solve)))
    else:
        print(solve)

def write_file(list_formulas):
    f = open('output.cnf', 'w')
    f.write('\n'.join(list_formulas))
    f.close()

printEquisatisfiableSatFormula()