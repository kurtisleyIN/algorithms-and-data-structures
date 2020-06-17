# python3
import sys

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    print (*(sorted([text[i:i+k] for i in range(len(text) - k + 1)])), sep = '\n')
