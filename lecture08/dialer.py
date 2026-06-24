#!/usr/bin/env python3

# Example: Knight's Dialer (Dynamic Programming)

import sys

# Type Aliases

Pair = tuple[int, int]

# Constants

NEIGHBORS = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (0, 3, 9),
    5: [],
    6: (0, 1, 7),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}

# Functions

def dial_numbers_count1(start: int, length: int) -> int:
    ''' Version 1: Recursive

    >>> dial_numbers_count1(7, 3)
    4
    '''
    # Base case
    if length <= 1:
        return 1

    # Recursive step
    count = 0
    for neighbor in NEIGHBORS[start]:
        count += dial_numbers_count1(neighbor, length - 1)

    return count

def dial_numbers_count2(start: int, length: int, cache: dict[Pair, int]={}) -> int:
    ''' Version 2: Recursive with Memoization (Cache) '''
    # Base case
    if length <= 1:
        return 1

    # Recursive step (memoized)
    args = (start, length)
    if not args in cache:
        cache[args] = sum(
            dial_numbers_count2(n, length - 1) for n in NEIGHBORS[start]
        )

    return cache[args]

# Main Execution

def main():
    for line in sys.stdin:
        start, length = map(int, line.split())
        print(dial_numbers_count2(start, length))

if __name__ == '__main__':
    main()
