"""Unit tests for list utility functions in EX05."""

__author__ = "730660179"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_basic():
    """Tests only_evens with a mix of even and odd numbers."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_all_even():
    """Tests only_evens when all numbers are even."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_only_evens_no_even():
    """Tests only_evens when there are no even numbers."""
    assert only_evens([1, 3, 5]) == []


def test_sub_standard_range():
    """Tests sub with standard in-bounds start and end indices."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_out_of_bounds():
    """Tests sub with start and end indices out of bounds."""
    assert sub([10, 20, 30, 40], -1, 6) == [10, 20, 30, 40]


def test_sub_empty_list():
    """Tests sub when the input list is empty."""
    assert sub([], 1, 3) == []


def test_add_at_index_standard():
    """Tests add_at_index with standard index within bounds."""
    list_1 = [1, 2, 3, 5]
    add_at_index(list_1, 4, 3)
    assert list_1 == [1, 2, 3, 4, 5]


def test_add_at_index_end():
    """Tests add_at_index with adding element at the end of the list."""
    list_2 = [1]
    add_at_index(list_2, 2, 1)
    assert list_2 == [1, 2]


def test_add_at_index_invalid_index():
    """Tests that add_at_index raises an IndexError for an invalid index."""
    list_3 = []
    with pytest.raises(IndexError):
        add_at_index(list_3, 1, 1)
