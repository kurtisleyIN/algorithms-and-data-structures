# python3
# Input: The capacity of the knapsack (capacity) and the number of gold bars in the next line (n)
#        The sequence of integers defining the weights for each gold bar (weights)
# Output: The maximum weight of gold that can fit inside the knapsack
import sys

def optimal_weight(capacity, weights):
    Grid = [[0] * (capacity + 1) for x in range(len(weights))]
    Grid[0] = [weights[0] if weights[0] <= j else 0 for j in range(capacity + 1)]
    
    for row in range(1, len(weights)):
        for col in range(1, capacity + 1):
            value = Grid[row - 1][col]
            if weights[row] <= col:
                val = (Grid[row - 1][col - weights[row]]) + weights[row]
                if value < val:
                    value = val
                    Grid[row][col] = value
                else:
                    Grid[row][col] = value
            else:
                Grid[row][col] = value

    return Grid[-1][-1]
   
if __name__ == '__main__':
    input = sys.stdin.read()
    capacity, n, *weights = list(map(int, input.split()))
    print(optimal_weight(capacity, weights))