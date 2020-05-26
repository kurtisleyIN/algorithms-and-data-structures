# python3
import sys

def max_dot_product(a, b):
    IndexLookupA = sorted(range(len(a)), key = lambda k: a[k], reverse = True)
    IndexLookupB = sorted(range(len(b)), key = lambda k: b[k], reverse = True)
    
    res = 0
    for i, j in zip(IndexLookupA, IndexLookupB):
        res =  res + a[i]*b[j]
        
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))