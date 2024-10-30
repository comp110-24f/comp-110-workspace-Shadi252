"""Summing the elements of a list using different loops"""

__author__ = "730660179"


def w_sum(vals: list[float]) -> float:
    sum = 0.0
    idx = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0.0
    for value in vals:
        sum += value
    return sum


def f_range(vals: list[float]) -> float:
    sum = 0.0
    for values in range(0, len(vals)):
        sum += values
    return sum
