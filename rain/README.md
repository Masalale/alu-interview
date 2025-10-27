Rainwater retention
===================

This directory contains `0-rain.py`, which implements the function `rain(walls)`.

Problem
-------
Given a list of non-negative integers `walls` representing wall heights (unit width), determine how many square units of water are retained after it rains. The ends of the list are open (no implicit walls beyond the ends). If the list is empty, return 0.

Contract
--------
- Prototype: `def rain(walls)`
- Input: list of non-negative integers
- Output: integer — total units of water retained

Implementation details
----------------------
The implementation uses the two-pointer technique to compute retained water in O(n) time and O(1) additional space.

Idea (short):
- Keep two pointers `left` and `right` at the ends of the list.
- Track `left_max` (highest wall seen so far from the left) and `right_max` (highest from the right).
- Move the pointer with the smaller current wall inward. If the current wall is smaller than the corresponding max, it can hold `max - height` units of water; otherwise update the max.

Why this works
---------------
Water trapped at any position depends on the shorter of the highest wall to its left and the highest wall to its right. By maintaining `left_max` and `right_max` and moving the side with the smaller current height, we ensure the trapped water calculation at each step is correct without scanning either side repeatedly.

Time & Space complexity
-----------------------
- Time: O(n) — single pass through the list
- Space: O(1) — constant extra space (pointers and counters)

Edge cases
----------
- Empty list -> 0
- Lists with no pits (monotonic non-decreasing or non-increasing) -> 0
- Large lists work within linear time and constant extra memory

Examples
--------
- `rain([3, 0, 0, 2, 0, 4])` -> `10`
- `rain([])` -> `0`
- `rain([1,1,1])` -> `0`

Running the quick tests
-----------------------
The file `0-rain.py` contains a small `__main__` block with example tests. Run it with Python 3 to see PASS/FAIL for those cases:

```bash
python3 "rain/0-rain.py"
```

If your shell sources custom startup files that cause errors (for example a broken `.zshrc`), run the command under `bash -lc` to avoid sourcing zsh-specific startup files:

```bash
bash -lc 'python3 "rain/0-rain.py"'
```

Notes
-----
Small, self-contained implementation that matches the expected prototype. If you'd like, I can add unit tests (unittest or pytest) and a short README section describing how to run them in CI.

