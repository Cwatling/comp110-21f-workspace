word: str = input("enter a word: ")
output: bool = False

i: int = 0

while i < len(word):
    j: int = i + 1
    hold: str = word[i]
    while j < len(word):
        if word[j] == word[i]:
            output = True
            
        j +=1
    i += 1 

print(output)


