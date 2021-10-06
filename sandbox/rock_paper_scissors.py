from random import randint

def game() -> None:
    guess: int = int((input("Enter 1 for Rock, 2 for paper, or 3 Scissors: ")))
    if guess == 1:
        print("You chhose Rock.")
    elif guess == 2:
        print("You Choose Paper")
    else:
        print("You Choose scissors")

    op: int = randint(1,3)
    if op == 1:
        print("Your Opponont Choose Rock.")
    elif op == 2:
        print("Your Opponont Choose Paper")
    else:
        print("Your Opponont Choose scissors")

    if guess == op:
        print("Its a tie")
        game()
    elif guess == 1:
        if op == 2:
            print("You Lose")
        else:
            print("You Win")
    elif guess == 2:
        if op == 1:
            print("You Win")
        else:
            print("You Lose")
    elif guess == 3:
        if op == 1:
            print("You Lose")
        else:
            print("You lose")

game()




