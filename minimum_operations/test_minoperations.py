#!/usr/bin/python3
"""
Test file for minimum operations solution
"""

import sys
import os

# Import the minOperations function from the module
def import_minoperations():
    """Import minOperations from the 0-minoperations.py file"""
    module_path = os.path.join(os.path.dirname(__file__), '0-minoperations.py')
    with open(module_path, 'r') as f:
        exec(f.read(), globals())

import_minoperations()


def test_minOperations():
    """Test the minOperations function with various test cases"""
    
    test_cases = [
        # (input, expected_output, description)
        (1, 0, "n=1: Already have 1 H, no operations needed"),
        (2, 2, "n=2: Copy All, Paste"),
        (3, 3, "n=3: Copy All, Paste, Paste (3 is prime)"),
        (4, 4, "n=4: Copy All, Paste (HH), Copy All, Paste (HHHH)"),
        (5, 5, "n=5: 5 is prime, so Copy All + 4 Pastes"),
        (6, 5, "n=6: 6 = 2×3, so 2+3 = 5 operations"),
        (9, 6, "n=9: 9 = 3×3, so 3+3 = 6 operations"),
        (12, 7, "n=12: 12 = 2×2×3, so 2+2+3 = 7 operations"),
        (15, 8, "n=15: 15 = 3×5, so 3+5 = 8 operations"),
        (21, 10, "n=21: 21 = 3×7, so 3+7 = 10 operations"),
        (0, 0, "n=0: Edge case, impossible"),
        (-1, 0, "n=-1: Edge case, impossible"),
    ]
    
    print("Testing minOperations function...")
    print("=" * 50)
    
    all_passed = True
    for n, expected, description in test_cases:
        result = minOperations(n)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result != expected:
            all_passed = False
            
        print(f"{status} | {description}")
        print(f"      Input: n={n}, Expected: {expected}, Got: {result}")
        print()
    
    if all_passed:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed!")
    
    return all_passed


def manual_verification():
    """Manually verify the n=9 example from the problem"""
    print("\nManual verification for n=9:")
    print("=" * 30)
    
    steps = [
        "Start: H (1 character)",
        "Copy All (1 op): clipboard = H",
        "Paste (2 ops): HH (2 characters)",
        "Paste (3 ops): HHH (3 characters)",
        "Copy All (4 ops): clipboard = HHH",
        "Paste (5 ops): HHHHHH (6 characters)",
        "Paste (6 ops): HHHHHHHHH (9 characters)"
    ]
    
    for i, step in enumerate(steps):
        print(f"Step {i}: {step}")
    
    print(f"\nTotal operations: 6")
    print(f"Function result: {minOperations(9)}")
    print(f"Match: {'✓' if minOperations(9) == 6 else '✗'}")


if __name__ == "__main__":
    test_minOperations()
    manual_verification()