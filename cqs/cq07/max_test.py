from cqs.cq07.find_max import find_and_remove_max

"""Max Function Test"""

__author__ = "730660179"


# Test for finding and removing max in a list with two elements
def test_find_and_remove_max_basic() -> None:
    elem2: list[int] = [1, 10]
    assert find_and_remove_max(elem2) == 10  # passes if true
    assert elem2 == [1]  # after removing max, only 1 should remain


# Test for mutating the list correctly by removing all instances of the max value
def test_find_and_remove_max_mutate() -> None:
    elem3: list[int] = [1, 8, 8, 2]
    find_and_remove_max(elem3)
    assert elem3 == [1, 2]  # passes if true, all 8s should be removed


# Test for empty input
def test_find_and_remove_max_empty() -> None:
    elem4: list[int] = []
    assert (
        find_and_remove_max(elem4) == -1
    )  # passes if true, should return -1 for empty list


# Test for a list with all the same values
def test_find_and_remove_max_same_values() -> None:
    elem5: list[int] = [5, 5, 5, 5]
    assert find_and_remove_max(elem5) == 5  # max value is 5
    assert elem5 == []  # after removing max, list should be empty


# Test for a large list with multiple max values
def test_find_and_remove_max_large() -> None:
    elem6: list[int] = [3, 6, 9, 9, 7, 6, 9]
    assert find_and_remove_max(elem6) == 9  # max value is 9
    assert elem6 == [3, 6, 7, 6]  # all 9s should be removed
