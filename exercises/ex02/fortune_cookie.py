"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730412366"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
random: int = randint(1,4)

print("Your fortune cookie says...")

if random  <= 2:
    if random == 1:
        print("You are going to meet and amazing person today!")
    else:
        print("You will have the best day ever!")
elif random >= 3:
    if random == 3:
        print("Your life will change for the better today!!")
    else:
        print("Your lucky lottery numbers are 15 36 28 20 17!!!!")

print("Now, go spread positive vibes!")