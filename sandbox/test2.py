word: str = input("enter a word: ")

output = ""

for x in word:
    if x not in output:
        output += x

if output == word:
    print(False)
else:
    print(True)
