#! python3
import sys


def optimal_summands(pieces):
    """ Output the maximum numbers that can be represented as a sum of distinct positive integers """

    # Initialize list of summands
    summand = 1
    summands = []

    # Increment summand and take the summand out if additional takes can be taken, or if the summand and pieces match
    while pieces > 0:
        if ((pieces-summand) > summand) or (summand == pieces):
            summands.append(summand)
            pieces -= summand
        summand += 1

    return summands


if __name__ == '__main__':
    n = int(sys.stdin.read())

    s_list = optimal_summands(n)
    print(len(s_list))
    for s in s_list:
        print(s, end=' ')
