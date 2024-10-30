"""Directory Practice Excersie six"""

__author__ = "730660179"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert keys and values of a dict."""
    inverted_dict = {}  # empty dictionary
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(
                "Duplicate value found, cannot invert dictionary."
            )  # raises error for duplicate values
        inverted_dict[value] = key  # inversion formula
    return inverted_dict


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Return the color that appears most frequently in the dictionary."""
    color_count = {}
    for name, color in fav_colors.items():
        if color in color_count:
            color_count[color] += 1  # counts colors
        else:
            color_count[color] = 1

    max_count = 0
    favorite = ""
    for color, count in color_count.items():
        if count > max_count or (count == max_count and color in fav_colors.values()):
            max_count = count
            favorite = color
    return favorite  # returning first color in addition to favorite


def count(items: list[str]) -> dict[str, int]:
    """Count occurrences of each unique item in the input list."""
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts  # returns count from each item


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by their starting letter into a dictionary."""
    categorized = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in categorized:
            categorized[first_letter] = []
        categorized[first_letter].append(word)
    return categorized


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance for a specific day by adding the student to the list."""
    if day in attendance:
        attendance[day].append(student)  # adds student to attendence
    else:
        attendance[day] = [student]
