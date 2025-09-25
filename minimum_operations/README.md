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
- `n ≤ 1`: Return 0 (impossible or already achieved)
- `n` is prime: Return `n` (copy 1, paste n-1 times)
- `n` is composite: Sum of all prime factors