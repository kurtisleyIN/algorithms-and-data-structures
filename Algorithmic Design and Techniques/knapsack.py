# python3
import sys

def optimal_weight(W, wt):
    Grid = [[0] * (W + 1) for x in range(len(wt))]
    Grid[0] = [wt[0] if wt[0] <= j else 0 for j in range(W + 1)]
    
    for row in range(1, len(wt)):
        for col in range(1, W + 1):
            value = Grid[row - 1][col]
            if wt[row] <= col:
                val = (Grid[row - 1][col - wt[row]]) + wt[row]
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
    W, n, *wt = list(map(int, input.split()))
    print(optimal_weight(W, wt))