from random import randint

points: int = 10

# A casino game that didnt make it into my choose your own adventure project
def casino() -> None:
    global points
    print(f"Welcome to the casino you have {points} points to spend")
    bet: int = int(input("how many points would you like to bet?: "))
    if bet <= points:
        points = points - bet
        winnings: int = randint(0, bet * 2)
        points = points + winnings
        print(f"You won {winnings} coins")
    else:
        points = 0
        print("Dont lie the casino always wins.")

casino()
print(f"You came out with {points} coins")
