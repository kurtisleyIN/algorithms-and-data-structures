# python3
import sys

def get_optimal_value(capacity, weights, values):
    PerUnit = [i/j for i, j in zip(values, weights)]
    IndexLookup = sorted(range(len(PerUnit)), key = lambda k: PerUnit[k], reverse = True)
    value = 0.
    
    for i in IndexLookup:
        LootPickup = min(capacity, weights[i])
        value = value + LootPickup*PerUnit[i]
        capacity = capacity - LootPickup
        
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))