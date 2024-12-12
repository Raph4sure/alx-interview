#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


# def isWinner(x, nums):
#     """x - rounds
#     nums - numbers list
#     """
#     if x <= 0 or nums is None:
#         return None
#     if x != len(nums):
#         return None

#     ben = 0
#     maria = 0

#     a = [1 for x in range(sorted(nums)[-1] + 1)]
#     a[0], a[1] = 0, 0
#     for i in range(2, len(a)):
#         rm_multiples(a, i)

#     for i in nums:
#         if sum(a[0:i + 1]) % 2 == 0:
#             ben += 1
#         else:
#             maria += 1
#     if ben > maria:
#         return "Ben"
#     if maria > ben:
#         return "Maria"
#     return None


# def rm_multiples(ls, x):
#     """removes multiple
#     of primes
#     """
#     for i in range(2, len(ls)):
#         try:
#             ls[i * x] = 0
#         except (ValueError, IndexError):
#             break





#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'