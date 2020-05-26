# python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    LeftSide = get_majority_element(a, left, (left + right - 1)//2 + 1)
    RightSide = get_majority_element(a, (left + right - 1)//2 + 1, right)
    
    LeftCount = 0
    for i in range(left, right):
        if a[i] == LeftSide:
            LeftCount = LeftCount + 1
    if LeftCount > (right-left)//2:
        return LeftSide

    RightCount = 0
    for i in range(left, right):
        if a[i] == RightSide:
            RightCount = RightCount + 1
    if RightCount > (right-left)//2:
        return RightSide
    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
