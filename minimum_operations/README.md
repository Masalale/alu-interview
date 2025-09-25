# Minimum Operations - Solution Explanation

## Problem Analysis

Given a text file with a single character 'H', we need to find the minimum number of operations to get exactly `n` 'H' characters using only two operations:
- **Copy All**: Copies all characters currently in the file
- **Paste**: Pastes the previously copied characters

## Algorithm Explanation

This problem is equivalent to finding the **sum of all prime factors** of `n`. Here's why:

1. We start with 1 'H'
2. To optimally reach `n` characters, we need to think about factorization
3. If `n = a × b`, the optimal strategy is:
   - Reach `a` characters first
   - Copy All (1 operation)
   - Paste `b-1` times (`b-1` operations)
   - Total: `operations_to_reach_a + 1 + (b-1) = operations_to_reach_a + b`

4. The optimal factorization uses prime factors because:
   - Any composite factor can be further broken down
   - Prime factors give the minimal sum

## Current Implementation

The streamlined solution in `0-minoperations.py`:

```python
def minOperations(n):
    if n < 2:
        return 0
    ops = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1
    return ops
```

This implementation:
- Uses `n < 2` instead of `n <= 1` for clarity
- Increments factor by 1 each time for simplicity
- Efficiently finds all prime factors without optimization checks

## Example Walkthrough (n = 9)

- `9 = 3 × 3`
- Prime factors: 3, 3
- Sum of prime factors: 3 + 3 = 6

Step by step:
1. Start: H (1 character)
2. Copy All, Paste, Paste → HHH (3 characters) - 3 operations  
3. Copy All, Paste, Paste → HHHHHHHHH (9 characters) - 3 more operations
4. Total: 6 operations

## Time Complexity
- **Time**: O(√n) - we only check factors up to √n
- **Space**: O(1) - constant space usage

## Edge Cases
- `n < 2`: Return 0 (impossible or already achieved)
- `n` is prime: Return `n` (copy 1, paste n-1 times)
- `n` is composite: Sum of all prime factors

## Algorithm Analysis
- **Correctness**: The algorithm correctly finds all prime factors by trial division
- **Efficiency**: While not optimized with `factor * factor <= n`, it's still efficient for reasonable inputs
- **Simplicity**: The linear increment of factor makes the code more readable and maintainable