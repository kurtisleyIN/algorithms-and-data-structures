#! python3
import sys


def binary_search(search_list, search_element):
    """ Calculate each index of the search list that matches x, -1 if no match """
    
    # Initialize the left and right bounds as the first and last element of the array
    left_bound = 0
    right_bound = len(search_list)-1

    while left_bound <= right_bound:

        # Calculate the midpoint between the left and right bounds
        middle_point = left_bound + ((right_bound-left_bound)//2)

        # Reassign the left and right bounds (cutting in half) until the searched element is the middle point
        if search_element == search_list[middle_point]:
            return middle_point
        if search_element < search_list[middle_point]:
            right_bound = middle_point - 1
        if search_element > search_list[middle_point]:
            left_bound = middle_point + 1

    return -1


if __name__ == '__main__':
    integers = sys.stdin.read()
    data = list(map(int, integers.split()))
    n = data[0]                                 # Size of search list
    s = data[1: n+1]                            # Search list, a sequence of positive integers in increasing order
    for x in data[n+2:]:                        # Elements to search for
        print(binary_search(s, x), end = ' ')
