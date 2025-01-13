#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

# Check if the user provided a command-line argument
if len(sys.argv) > 1:
    try:
        # Convert the first argument to an integer
        number = int(sys.argv[1])
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calculate the factorial and print the result
            print(factorial(number))
    except ValueError:
        print("Please provide a valid integer.")
else:
    print("Usage: python3 script.py <non-negative integer>")
