"""An exercise in remainders and boolean logic."""

__author__ = "730412366"


number: int = int(input("Enter an int: "))

if number % 7 == 0 and number % 2 == 0:
    print("TAR HEELS")
elif number % 7 == 0:
    print("HEELS")
elif number % 2 == 0:
    print("TAR")