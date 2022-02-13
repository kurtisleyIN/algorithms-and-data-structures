#! python3
import sys


def get_optimal_value(capacity, weights, values):
    """ Calculate the maximum value that can fit inside the knapsack (float for fractional cases) """

    # Initialize max_value as a float
    max_value = 0.
    
    # Calculate the unit value for each item and sort their indexes in decreasing order
    unit_values = [i/j for i, j in zip(values, weights)]
    unit_value_indexes = sorted(range(len(unit_values)), key=lambda x: unit_values[x], reverse=True)
    
    # Find the limit of each item that can be taken, take as much as possible, and update the capacity
    for index in unit_value_indexes:
        loot_pickup = min(capacity, weights[index])
        max_value += loot_pickup*unit_values[index]
        capacity -= loot_pickup
        
    return max_value


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]                                         # n for the number of items
    c = data[1]                                         # capacity for the capacity of the knapsack
    v = data[2:(2*n + 2):2]                             # list of values for the value of the item
    w = data[3:(2*n + 2):2]                             # list of weights for the weight of the items
    print(get_optimal_value(c, w, v))
