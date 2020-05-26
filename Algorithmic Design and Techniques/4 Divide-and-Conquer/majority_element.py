# python3
# Input: An integer (n)
#        A sequence of non-negative integers (Maj)
# Output: 1 if the sequence contains an element that appears strictly more than n/2 times (0 if otherwise)
import sys

def get_majority_element(Maj, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return Maj[left]
    
    LeftSide = get_majority_element(Maj, left, (left + right - 1)//2 + 1)
    RightSide = get_majority_element(Maj, (left + right - 1)//2 + 1, right)
    
    LeftCount = 0
    for i in range(left, right):
        if Maj[i] == LeftSide:
            LeftCount += 1
    if LeftCount > (right-left)//2:
        return LeftSide

    RightCount = 0
    for i in range(left, right):
        if Maj[i] == RightSide:
            RightCount += 1
    if RightCount > (right-left)//2:
        return RightSide
    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *Maj = list(map(int, input.split()))
    if get_majority_element(Maj, 0, n) != -1:
        print(1)
    else:
        print(0)
