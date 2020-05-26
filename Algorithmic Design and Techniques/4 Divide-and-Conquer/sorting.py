# python3
# Input: An integer (n)
#        A sequence of integers (Part)
# Output: Part in increasing order
import sys
import random

def partition3(Part, l, r):
    Pivot = Part[l]
    i, j, t = l, l, r
    
    while i <= t:
        if Part[i] < Pivot:
            Part[j], Part[i] = Part[i], Part[j]
            j = j + 1
        elif Part[i] > Pivot:
            Part[t], Part[i] = Part[i], Part[t]
            t = t - 1
            i = i - 1
        i = i + 1
    return j, t

def partition2(Part, l, r):
    x = Part[l]
    j = l;
    for i in range(l + 1, r + 1):
        if Part[i] <= x:
            j += 1
            Part[i], Part[j] = Part[j], Part[i]
    Part[l], Part[j] = Part[j], Part[l]
    return j

def randomized_quick_sort(Part, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    Part[l], Part[k] = Part[k], Part[l]
    #use partition3
    m1, m2 = partition3(Part, l, r)
    randomized_quick_sort(Part, l, m1 - 1);
    randomized_quick_sort(Part, m2 + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *Part = list(map(int, input.split()))
    randomized_quick_sort(Part, 0, n - 1)
    for x in Part:
        print(x, end=' ')
