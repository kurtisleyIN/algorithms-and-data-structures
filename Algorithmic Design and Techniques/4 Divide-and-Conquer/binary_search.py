# python3
# Input: An integer (n) and a sequence of positive integers in increasing order (SearchArray)
#        A sequence of positive integers
# Output: Each index of m that matches each element of a (-1 if no match)
import sys

def binary_search(SearchArray, x):
    left, right = 0, len(SearchArray)-1
    
    while left <= right:
        mid = left + ((right-left)//2)
        if x == SearchArray[mid]:
            return mid
        if x < SearchArray[mid]:
            right = mid - 1
        if x > SearchArray[mid]:
            left = mid + 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    SearchArray = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(SearchArray, x), end = ' ')