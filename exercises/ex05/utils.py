"""List utility functions for EX05 exercise."""

__author__ = "730660179"


def only_evens(nums: list[int]) -> list[int]:
    """Returns a list containing only the even numbers from nums."""
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of nums from start index up to but not including end index."""
    subset = []
    if start < 0:
        start = 0
    if end > len(nums):
        end = len(nums)
    if len(nums) == 0 or start >= len(nums) or end <= 0:
        return subset
    for i in range(start, end):
        subset.append(nums[i])
    return subset


def add_at_index(nums: list[int], elem: int, index: int) -> None:
    """Inserts elem at the specified index in nums. Raises IndexError if index is invalid."""
    if index < 0 or index > len(nums):
        raise IndexError("Index is out of bounds for the input list")

    # Append a placeholder to extend the list, then shift elements
    nums.append(0)  # Temporary space for the new element
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = elem
