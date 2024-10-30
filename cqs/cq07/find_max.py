"""Find max function and remove from list!"""

__author__ = "730660179"


# Finds and removes max
def find_and_remove_max(elem: list[int]) -> int:
    if len(elem) == 0:
        return -1  # return -1 if the list is empty

    max_value = elem[0]  # assume the first element is the max
    for num in elem:
        if num > max_value:
            max_value = num  # update max_value if a bigger number is found

    i = 0
    while i < len(elem):
        if elem[i] == max_value:
            elem.pop(i)  # remove the max value
        else:
            i += 1  # increment index only if no element is removed

    return max_value  # return the maximum value
