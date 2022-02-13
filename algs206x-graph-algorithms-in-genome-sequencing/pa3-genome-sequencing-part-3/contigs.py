#python3
import sys
from functools import reduce

def string_suffix(s):
    return s[1:]

def string_prefix(s):
    return s[:-1]

def generate_contigs_from_reads(k_mers):
    graph = de_bruijn_from_k_mers(k_mers)
    if not graph:
        raise Exception("Empty graph")

    degrees = graph_degrees(graph)
    contigs = []

    for v in graph.keys():

        # we want maximal non-branching path
        if degrees[v] == [1,1]:
            continue

        for u in graph[v]:
            contig = v
            w = u

            while True:
                contig += w[-1]
                w_degree = degrees[w]

                if w_degree == [1,1]:
                    w = graph[w][0]
                else:
                    break

            contigs.append(contig)

    return sorted(contigs)

def de_bruijn_from_k_mers(k_mers):
    k_mers = list(k_mers)

    graph = {}

    for mer in k_mers:
        suffix = string_suffix(mer)
        prefix = string_prefix(mer)

        if prefix in graph.keys():
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]

    return graph

def graph_degrees(graph):
    if not graph:
        raise Exception("Empty graph")

    # degrees[u] = [in(u),out(u)]
    degrees = {}

    for v in graph.keys():
        neighbors = graph[v]
        out_degree = len(neighbors)

        if v in degrees:
            degrees[v][1] = out_degree
        else:
            degrees[v] = [0, out_degree]

        for u in neighbors:
            if u in degrees:
                degrees[u][0] += 1
            else:
                degrees[u] = [1,0]

    return degrees


if __name__ == "__main__":
    kmers = [line.strip() for line in sys.stdin if line.strip()]

    contigs = generate_contigs_from_reads(kmers)
    sol = "\n".join(contigs)
    print(sol)
    

