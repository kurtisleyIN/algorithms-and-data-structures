# python3
# Input: Two integers (n for the number of items, capacity for the capacity of the knapsack)
#        n lines to follow with two integers (values for the value of the item, weights for the weight of the item)
# Output: The maximum value that can fit inside of the knapsack (float for fractional cases)

import sys

def get_optimal_value(capacity, weights, values):
    
    # Calculate the unit value for each item and sort their indexes in decreasing order
    PerUnit = [i/j for i, j in zip(values, weights)]
    IndexLookup = sorted(range(len(PerUnit)), key = lambda k: PerUnit[k], reverse = True)
    
    # Initialize MaxValue as a float
    MaxValue = 0.
    
    # Find the limit of each item that can be taken, take as much as possible, and update the capacity
    for i in IndexLookup:
        LootPickup = min(capacity, weights[i])
        MaxValue += LootPickup*PerUnit[i]
        capacity -= LootPickup
        
    return MaxValue

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))