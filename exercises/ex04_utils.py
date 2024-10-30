"""List Utilities"""

__author__ = "730660179"


# This function checks if all elements in the list are equal to the given number.
def all(lst: list[int], number: int) -> bool:
    if len(lst) == 0:
        return False
    for elem in lst:
        if elem != number:
            return False
    return True


# This function finds the maximum value in the list and raises Error if list is empty.
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    max_value = input[0]
    for num in input:
        if num > max_value:
            max_value = num
    return max_value


# This function checks if two lists are deeply equal
def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


# This function extends the first list by appending all elements from the second list
def extend(list1: list[int], list2: list[int]) -> None:
    for elem in list2:
        list1.append(elem)
