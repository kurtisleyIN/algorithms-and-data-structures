#! python3
import sys


def get_majority_element(majority_list, left_index, right_index):
    """ Determine whether the sequence contains an element that appears > n/2 times, -1 if otherwise """
    
    # Exit statement for recursive calls
    if left_index == right_index - 1:
        return majority_list[left_index]
    
    # Recursively splitting MajArray into a tree of sub-arrays
    majority_left = get_majority_element(majority_list, left_index, (left_index+right_index-1)//2 + 1)
    majority_right = get_majority_element(majority_list, (left_index+right_index-1)//2 + 1, right_index)
    
    # Determines if the majority element is on the left/right side for each sub-array, -1 if it doesn't exist
    left_count = 0
    for i in range(left_index, right_index):
        if majority_list[i] == majority_left:
            left_count += 1
    if left_count > (right_index-left_index)//2:
        return majority_left
    
    right_count = 0
    for i in range(left_index, right_index):
        if majority_list[i] == majority_right:
            right_count += 1
    if right_count > (right_index-left_index)//2:
        return majority_right
    
    return -1


if __name__ == '__main__':
    integers = sys.stdin.read()
    n, *m = list(map(int, integers.split()))            # A sequence of non-negative integers (majority_list)
    if get_majority_element(majority_list=m, left_index=0, right_index=n) != -1:
        print(1)
    else:
        print(0)
