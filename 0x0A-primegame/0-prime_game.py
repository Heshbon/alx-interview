#!/usr/bin/python3
""" The prime game module"""


def isWinner(x, nums):
    """ Determine the winner of a prime game with `x` rounds"""
    if x == 0 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes up to the maximum number in nums.
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for a, is_prime in enumerate(primes, 1):
        if a == 1 or not is_prime:
            continue
        for b in range(a + a, n + 1, a):
            primes[b - 1] = False

    # Count primes for each round in nums.
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
