"""Mutating functions."""

__author__ = "730660179"


def manual_append(nums: list[int], digit: int) -> None:
    nums.append(digit)


def double(tally: list[int]) -> None:
    idx = 0
    while idx < len(tally):
        print(tally[idx] * 2)
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
