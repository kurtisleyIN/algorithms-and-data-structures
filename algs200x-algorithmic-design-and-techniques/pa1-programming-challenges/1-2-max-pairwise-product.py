#! python3

def main(numbers):
    """ Find maximum value that can be obtained by multiplying two integers from the sequence """

    largest_number = max(numbers)
    numbers.remove(largest_number)
    next_largest_number = max(numbers)

    return largest_number*next_largest_number


if __name__ == '__main__':

    n = int(input())                                # Length of the following sequence
    sequence = [int(x) for x in input().split()]    # Sequence of integers
    assert(n == len(sequence))

    print(main(sequence))
