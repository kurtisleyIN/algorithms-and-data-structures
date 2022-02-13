# python3
import sys

def de_bruijn(kmers):
    graph = {}
    for i in range(len(kmers)):
        try:
            graph[kmers[i][:-1]].append(kmers[i][1:])
        except:
            graph[kmers[i][:-1]] = [kmers[i][1:]]
    return graph

if __name__ == "__main__":
    kmers = sys.stdin.read().strip().splitlines()
    graph = de_bruijn(kmers)
    print(*(sorted([key + ' -> ' + ','.join(sorted([v for v in value])) for key, value in graph.items()])),sep ='\n')

