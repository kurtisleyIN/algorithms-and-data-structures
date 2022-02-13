#! python3
import sys


def max_dot_product(ppc, anc):
    """ Calculate the maximum value that can be attained by dot product """

    # Initialize the dot product as 0
    dot_product = 0
    
    # Sort the indexes of the PPC and ANC arrays in decreasing order based on their values
    ppc_indexes = sorted(range(len(ppc)), key=lambda x: ppc[x], reverse = True)
    anc_indexes = sorted(range(len(anc)), key=lambda x: anc[x], reverse = True)

    # Loop through both array and add their product to DP
    for ppc_index, anc_index in zip(ppc_indexes, anc_indexes):
        dot_product += ppc[ppc_index]*anc[anc_index]
        
    return dot_product


if __name__ == '__main__':
    numbers = sys.stdin.read()
    data = list(map(int, numbers.split()))
    n = data[0]                             # n is length of the following sequences
    p = data[1:(n+1)]                       # Profit-per-click
    a = data[(n+1):]                        # Average number of clicks
    print(max_dot_product(p, a))
