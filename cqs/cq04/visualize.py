"""My third cq file"""

__author__ = "730660179"

# Import from concatenation directory, then importing concat function
from cqs.cq04.concatenation import concat

# get_coords function import
from cqs.cq04.coordinates import get_coords

# Global Variables
x: str = "123"
y: str = "abc"

# Function Call
result: str = concat(x, y)
print(result)

# Get coords function call
get_coords(x, y)
