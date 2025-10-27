
"""Calculate how much rainwater is retained between walls.

Prototype: def rain(walls)
walls is a list of non-negative integers.
Return: Integer indicating total amount of rainwater retained.

This implementation uses the two-pointer technique with O(n) time and O(1) extra space.
"""

from typing import List


def rain(walls: List[int]) -> int:
	"""Return amount of rainwater retained given wall heights list.

	Args:
		walls: list of non-negative integers

	Returns:
		int: total units of water retained
	"""
	if not walls:
		return 0

	left, right = 0, len(walls) - 1
	left_max, right_max = 0, 0
	water = 0

	while left < right:
		if walls[left] <= walls[right]:
			if walls[left] >= left_max:
				left_max = walls[left]
			else:
				water += left_max - walls[left]
			left += 1
		else:
			if walls[right] >= right_max:
				right_max = walls[right]
			else:
				water += right_max - walls[right]
			right -= 1

	return water


if __name__ == "__main__":
	# Quick manual tests
	tests = [
		([], 0),
		([0], 0),
		([1, 1, 1], 0),
		([3, 0, 0, 2, 0, 4], 10),
		([0, 3, 0, 1, 0, 2], 5),
		([4, 2, 0, 3, 2, 5], 9),
		([5, 4, 1, 2], 1),
	]

	for i, (inp, expected) in enumerate(tests, 1):
		out = rain(inp)
		ok = out == expected
		print(f"Test {i}: input={inp} -> expected={expected}, got={out} -> {'PASS' if ok else 'FAIL'}")
