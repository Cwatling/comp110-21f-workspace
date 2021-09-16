"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("depth: "))

i: int = 0

while i < depth:
    print(TREE * (i + 1))
    i += 1