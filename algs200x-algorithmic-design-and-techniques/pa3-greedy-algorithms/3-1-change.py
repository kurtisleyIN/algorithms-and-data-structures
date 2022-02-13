#! python3
import sys


def get_change(money):
    """ Calculate the minimum number of coins (denominations of 1,5,10) to make change for money """

    coin_counter = 0

    # Take as many 10s as possible
    while money >= 10:
        money -= 10
        coin_counter += 1

    # Take as many 5s as possible
    while money >= 5:
        money -= 5
        coin_counter += 1

    # Take as many 1s as possible
    while money >= 1:
        money -= 1
        coin_counter += 1
        
    return coin_counter


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
