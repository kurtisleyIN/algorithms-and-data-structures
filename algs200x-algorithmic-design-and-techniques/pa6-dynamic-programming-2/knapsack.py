# python3
# Input: The capacity of the knapsack (capacity) and the number of gold bars in the next line (n)
#        The sequence of integers defining the weights for each gold bar (weights)
# Output: The maximum weight of gold that can fit inside the knapsack
import sys

def optimal_weight(capacity, weights):
    
    # Create a grid for the capacities and the weights of each gold bar
    Grid = [[0] * (capacity + 1) for x in range(len(weights))]
    Grid[0] = [weights[0] if weights[0] <= x else 0 for x in range(capacity + 1)]
    
    # Loop through every weight and capacity
    for row in range(1, len(weights)):
        for col in range(1, capacity + 1):
            
            # Assign the previous value as the value above the current one
            PrevVal = Grid[row - 1][col]
            if weights[row] <= col:
                BetterVal = (Grid[row - 1][col - weights[row]]) + weights[row]
                # If the better value is higher than the previous value, assign it to the current position
                # If not, assign the previous value to the current position
                if BetterVal < PrevVal:
                    Grid[row][col] = BetterVal
                else:
                    Grid[row][col] = PrevVal
            else:
                Grid[row][col] = PrevVal

    return Grid[-1][-1]
   
if __name__ == '__main__':
    input = sys.stdin.read()
    capacity, n, *weights = list(map(int, input.split()))
    print(optimal_weight(capacity, weights))