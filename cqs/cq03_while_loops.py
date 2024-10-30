"""Trying to code my first Loop!"""

__author__ = "730660179"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        else:
            count = count
        index += 1
    return count
