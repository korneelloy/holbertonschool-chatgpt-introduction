#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of n. If n is 0, returns 1.

    Note:
        This function assumes that the input n is a non-negative integer.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)

# Convert the first command-line argument to an integer and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
