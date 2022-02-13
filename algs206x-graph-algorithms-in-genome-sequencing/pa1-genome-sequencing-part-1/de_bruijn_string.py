# python3
import sys
from collections import defaultdict

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    print (text)
    tuples = []
    for i in range(0, len(text) - k+1):
        tuples.append((text[i: i+k-1], text[i+1: i+k]))
    dd = defaultdict(set)
    for t in tuples:
        dd[t[0]].add(t[1])
    
    print (*(sorted([key + ' -> ' + ','.join([v for v in value])
                           for key, value in dd.items()])),sep = '\n')
