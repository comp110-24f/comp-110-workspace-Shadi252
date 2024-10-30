"""My first challenge question in COMP110!"""

__author__ = "730660179"


# Function Definitnion
def mimic(message: str) -> str:
    """Return input value back to me."""
    return message


def main() -> None:
    """Pull function together."""
    print(mimic(message=input("What is your message?")))


# Function Call
if __name__ == "__main__":
    main()
