# python3
import sys

def overlap_graph(kmers):
    graph={}
    for iterator1, kmer1 in enumerate(kmers):
        for iterator2, kmer2 in enumerate(kmers):
            if kmer1[1:] == kmer2[:len(kmer2) - 1]:
                if kmer1 in graph:
                    graph[kmer1].append(kmer2)
                    graph[kmer1] = list(set(graph[kmer1]))
                else:
                    graph[kmer1] = [kmer2]
            
    return graph

if __name__ == "__main__":
    kmers = sys.stdin.read().strip().splitlines()
    overlaps = overlap_graph(kmers)
    for key, value in overlaps.items():
        print(key + "->" + ','.join(value))