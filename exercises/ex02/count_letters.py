"""Counting letters in a string."""

__author__ = "730412366"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

length: int = len(word)
i: int = 0
total: int = 0


while i < length:
    if word[i] == letter:
        total += 1
        i += 1
    else:
        i += 1

print(f"Count: {total}")
