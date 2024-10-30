"""My second cq file"""

__author__ = "730660179"


# """Prints the formatted pairs of each character in the two input strings."""
def get_coords(xs: str, ys: str) -> None:
    i = 0
    # Outer loop index
    while i < len(xs):
        j = 0
        # inner loop index
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1
        i += 1
