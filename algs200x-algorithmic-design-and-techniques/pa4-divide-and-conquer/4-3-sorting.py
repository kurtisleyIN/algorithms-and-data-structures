#! python3
# Output: PartArray in increasing order

import random
import sys


def partition3(partition_list, left_index, right_index):
    
    # Initialize pivots, indexes, and bounds
    pivot_element = partition_list[left_index]
    working_index = left_index
    left_bound = left_index
    right_bound = right_index
    
    # Only proceed with the swaps if it falls below the right bound
    while working_index <= right_bound:
        
        # If the current element is less than the pivot element, swap elements at left bound and working index
        # Increment left bound
        if partition_list[working_index] < pivot_element:
            partition_list[left_bound], partition_list[working_index] = partition_list[working_index], partition_list[left_bound]
            left_bound += 1
            
        # If the current element is more than the pivot element, swap elements at right bound and working index
        # Decrement right bound, keep working index the same
        elif partition_list[working_index] > pivot_element:
            partition_list[right_bound], partition_list[working_index] = partition_list[working_index], partition_list[right_bound]
            right_bound -= 1
            working_index -= 1

        # Increment working index
        working_index += 1

    return left_bound, right_bound


def randomized_quick_sort(partition_list, left_index, right_index):
    """ Sort the partition list """
    
    # Exit statement for the recursive calls
    if left_index >= right_index:
        return
    
    # Selects a random index between the left and right index, swap elements at left and random index
    random_index = random.randint(left_index, right_index)
    partition_list[left_index], partition_list[random_index] = partition_list[random_index], partition_list[left_index]

    # Determine two split points and recursively split the array into sub-arrays
    middle_left_index, middle_right_index = partition3(partition_list, left_index, right_index)
    randomized_quick_sort(partition_list, left_index, middle_left_index - 1)
    randomized_quick_sort(partition_list, middle_right_index + 1, right_index)


if __name__ == '__main__':
    integers = sys.stdin.read()
    n, *p = list(map(int, integers.split()))        # Sequence of integers
    randomized_quick_sort(p, 0, n-1)
    for x in p:
        print(x, end=' ')
