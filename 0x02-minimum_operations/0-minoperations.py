#!/usr/bin/python3
""" Calculates the fewest number of operations needed to
result in exactly n H characters in the file"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters"""

    str = 'H'  # Character to be created
    operations = 0  # The operations needed
    factor = 2  # The starting factor

    if n < 0:
        return 0  # Return 0 if n is negative

    while n > 1:
        while n % factor == 0:
            operations += factor  # The increment operations
            n //= factor  # Divide n by factor
        factor += 1  # Increment factor

    return operations  # Return total number of operations
