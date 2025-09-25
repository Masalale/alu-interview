#!/usr/bin/python3
"""
Simple version of the minOperations function for easy import
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.
    
    Args:
        n (int): Target number of H characters
        
    Returns:
        int: Minimum number of operations needed, or 0 if impossible
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    # Find all prime factors and sum them
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        operations += n
    
    return operations