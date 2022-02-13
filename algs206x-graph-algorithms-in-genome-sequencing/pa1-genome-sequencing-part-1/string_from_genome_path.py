# python3
import sys

def reconstruct_string(kmers):
    genomePath = kmers[0]
    for i in range(1, len(kmers)):
        genomePath += kmers[i][-1]
    return genomePath

if __name__ == "__main__":
    kmers = sys.stdin.read().strip().splitlines()
    print(reconstruct_string(kmers))