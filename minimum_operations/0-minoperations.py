#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.
    
    Starting with a single character H in a text file, we can perform only two operations:
    - Copy All: copies all characters currently in the file
    - Paste: pastes the copied characters
    
    Args:
        n (int): Target number of H characters
        
    Returns:
        int: Minimum number of operations needed, or 0 if impossible
        
    Example:
        n = 9
        H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
        Operations: 6 (Copy All, Paste, Paste, Copy All, Paste, Paste)
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


# Test cases to verify the solution
if __name__ == "__main__":
    # Test the example from the problem
    print(f"n = 9: {minOperations(9)} operations")  # Expected: 6
    
    # Additional test cases
    print(f"n = 1: {minOperations(1)} operations")  # Expected: 0
    print(f"n = 2: {minOperations(2)} operations")  # Expected: 2
    print(f"n = 3: {minOperations(3)} operations")  # Expected: 3
    print(f"n = 4: {minOperations(4)} operations")  # Expected: 4
    print(f"n = 6: {minOperations(6)} operations")  # Expected: 5
    print(f"n = 12: {minOperations(12)} operations")  # Expected: 7
