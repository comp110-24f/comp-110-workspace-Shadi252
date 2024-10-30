"""My first cq04 file"""

__author__ = "730660179"


def concat(str1: str, str2: str) -> str:
    """Concatenates two input strings and returns result."""
    return str1 + str2


# Global
word1: str = "happy"
word2: str = "tuesday"

# Print the result of calling concat with word1 and word2
if __name__ == "__main__":
    print(concat(word1, word2))
# Only if main function is called
