# python3
# Input: Two integers (n for the number of items, capacity for the capacity of the knapsack)
#        n lines to follow with two integers (values for the value of the item, weights for the weight of the item)
# Output: The maximum value that can fit inside of the knapsack (float for fractional cases)
import sys

def get_optimal_value(capacity, weights, values):
    PerUnit = [i/j for i, j in zip(values, weights)]
    IndexLookup = sorted(range(len(PerUnit)), key = lambda k: PerUnit[k], reverse = True)
    MaxValue = 0.
    
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