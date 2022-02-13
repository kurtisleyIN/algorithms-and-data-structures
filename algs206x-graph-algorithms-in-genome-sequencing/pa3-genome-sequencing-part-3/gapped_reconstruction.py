# python3
import sys
import codecs
import random

def construct_graph(pairs, k, d):
    graph = {}
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if i != j and pairs[i][0][1:] == pairs[j][0][:-1] and pairs[i][1][1:] == pairs[j][1][:-1]:
                try:
                    graph[pairs[i]].append(pairs[j])
                except:
                    graph[pairs[i]] = [pairs[j]]
    return graph

def recounstruct(pairs, k, d):
    out = pairs[0][0]
    for i in range(1, len(pairs)):
        out += pairs[i][0][-1]
    s = 0
    if len(out) - (2 * k + d) < 0:
        s = abs(len(out) - (2 * k + d))
    else:
        s = k
    j = max(len(out) - (2 * k + d), 0)

    out += pairs[j][1][:-s]
    for i in range(j + 2, len(pairs)):
        out += pairs[i][1][-1]
    return out

def construct_graph_new(pairs, k, d):
    graph = {}
    for pair in pairs:
        try:
            graph[(pair[0][:-1], pair[1][:-1])].append((pair[0][1:], pair[1][1:]))
        except:
            graph[(pair[0][:-1], pair[1][:-1])] = [(pair[0][1:], pair[1][1:])]
    return graph

def findCycle(graph, node, previous_path):
    path = []
    if len(previous_path) != 0:
        node_index = 0
        for i in range(len(previous_path)):
            if previous_path[i][0] == node:
                node_index = i
                break
        for i in reversed(range(len(previous_path))):
            path.append(previous_path[node_index - 1 - i])

    edge = (node, graph[node][random.randint(0, len(graph[node]) - 1)])

    while edge not in path and len(graph) != 0:
        path.append(edge)
        if len(graph[edge[0]]) > 1:
            graph[edge[0]].remove(edge[1])
        else:
            del graph[edge[0]]
        current_point = edge[1]
        if graph.get(current_point):
            edge = (current_point, graph[current_point][random.randint(0, len(graph[current_point]) - 1)])
    return len(graph), path


def detectStartAndEnd(graph):
    count_starts = {}
    count_ends = {}
    for key in graph:
        values = graph[key]
        for value in values:
            try:
                count_starts[key] += 1
            except:
                count_starts[key] = 1
            try:
                count_ends[key] += 0
            except:
                count_ends[key] = 0
            try:
                count_starts[value] += 0
            except:
                count_starts[value] = 0
            try:
                count_ends[value] += 1
            except:
                count_ends[value] = 1

    for key in count_starts:
        if count_starts[key] > count_ends[key]:
            start_point = key
        elif count_starts[key] < count_ends[key]:
            end_point = key
    return start_point, end_point


def findPath(graph):
    l = len(graph)
    start, end = detectStartAndEnd(graph)
    try:
        graph[end].append(start)
    except:
        graph[end] = [start]
    node = sorted(graph.keys())[random.randint(0, len(graph) - 1)]
    path = []
    while l != 0:
        l, path = findCycle(graph, node, path)
        nodes = []
        if l != 0 and len(path):
            for edge in path:
                if edge[0] in graph:
                    nodes.append(edge[0])
            node = nodes[random.randint(0, len(nodes) - 1)]
    return path, start, end

def reconstructGenome(pairs, k, d):
    graph = construct_graph_new(pairs, k, d)
    cycle, start, end = findPath(graph)
    pairs = constructOutput(cycle, start, end)
    out = recounstruct(pairs, k, d)
    return out

def constructOutput(cycle, start, end):
    pos = 0
    for i in range(0, len(cycle)):
        if cycle[i][0][1] == end[1] and cycle[i][1][0] == start[0]:
            pos = i
            break
    out = codecs.open('out.txt', 'w')
    for item in cycle[pos:]:
        out.write(item[1][0] + '\t' + item[1][1] + ' -> ')
    for item in cycle[:pos]:
        out.write(item[1][0] + '\t' + item[1][1] + ' -> ')
    out.close()

    pairs = [cycle[pos:][1][0]]
    for item in cycle[pos + 1:]:
        pairs.append(item[1])
    for item in cycle[:pos]:
        pairs.append(item[1])
    return pairs


if __name__ == "__main__":
    k, d = map(int, sys.stdin.readline().strip().split())
    input = [line.strip() for line in sys.stdin if line.strip()]
    
    pairs = [tuple(edge.split('|')) for edge in input if edge]

    print(reconstructGenome(pairs, k, d))
    



