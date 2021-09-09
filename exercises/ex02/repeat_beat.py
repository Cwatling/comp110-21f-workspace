"""Repeating a beat in a loop."""

__author__ = "730412366"


# Begin your solution here...
beat: str = input("what beat do you want to repeat? ")
num: int = int(input("How many times do you want to repeat it? "))

i: int = 1
repeat_beat: str = beat
if num > 0:
    while i < num:
        repeat_beat += " " + beat 
        i += 1
else:
    repeat_beat = "No beat..."

print(repeat_beat)