# ALU Interview - Minimum Operations

## Project Overview

This repository contains the solution to the "Minimum Operations" coding interview problem, which calculates the fewest number of operations needed to achieve exactly `n` 'H' characters in a text file using only two operations: Copy All and Paste.

## Problem Description

Given a text file containing a single character 'H', determine the minimum number of operations to result in exactly `n` 'H' characters using only:
- **Copy All**: Copies all characters currently in the file
- **Paste**: Pastes the previously copied characters

## Solution

The solution uses the mathematical insight that this problem is equivalent to finding the **sum of all prime factors** of `n`. This is because the optimal strategy involves factorizing `n` and using the most efficient copying patterns.

### Example (n = 9)
```
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```
Operations: 6 (since 9 = 3 × 3, and 3 + 3 = 6)

## Files Structure

```
minimum_operations/
├── 0-minoperations.py     # Main solution with tests
├── minoperations.py       # Clean importable version
├── test_minoperations.py  # Comprehensive test suite
└── README.md             # Detailed explanation
```

## Algorithm Complexity

- **Time Complexity**: O(√n) - only checks factors up to √n
- **Space Complexity**: O(1) - constant space usage

## Usage

```python
from minimum_operations.minoperations import minOperations

# Example usage
result = minOperations(9)  # Returns 6
print(f"Minimum operations for n=9: {result}")
```

## Testing

The solution has been thoroughly tested with various edge cases and examples, all passing successfully.