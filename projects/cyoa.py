"""Allows for the use of the randint function."""
from random import randint

"""Stock Market Game!"""
__author__ = 730412366

"""Global variables."""
player: str = ""
points: int = 500
NAMED_CONSTANT = "\U0001F44D"


def greet() -> None:
    """Greets the players and asks their name."""
    global player
    print("Hello stranger welcome to XXXXXX")
    player = input("May I ask your name? ")


def intro() -> None:
    """Gives the the player the option to start the game, check their money, or simply exit the game."""
    global points
    choice_one: int = int(input(f"Hello {player} welcome to the stock market your goal is to make as much money as you can.\nYou start this game with a starter investment of {points} dollars\nEnter 1 to start the game, 2 to check your money, or 3 to exit the game: "))
    if choice_one == 1:
        start()
    elif choice_one == 2:
        print(f"You are starting the game with {points} dollars")
        intro()
    elif choice_one == 3:
        print(f"Goodbye {player}")
    else:
        print("invalid answer you lose :(")


def start() -> None:
    """Loop that will run through all the 5 investments!"""
    if points > 0:
        i: int = 1
        while i <= 5:
            print(f"this is investment number {i}/5")
            choice_two: int = int(input("Enter 1 for a low risk investment or enter 2 for a high risk investment, or press 3 to stop investing: "))
            if choice_two == 1:
                low_risk()
                i += 1
            elif choice_two == 2:
                high_risk()
                i += 1
            elif choice_two == 3:
                i = 6
            else:
                print("invalid command try again")
    

def high_risk() -> None:
    """Bets your money in a high risk way."""  
    global points
    bet: int = int(input(f"So {player} You choose a high risk investment, How much would you like to invest: "))
    if bet <= points:
        points = points - bet
        winnings: int = randint(0, bet * 2)
        points = points + winnings
        print(f"Your high risk investment left you with a total of {points} dollars")
    else:
        print("Dont lie about your money the irs will get ya")


def low_risk() -> None:
    """Bets your money in a much lower risk way."""
    global points
    bet: int = int(input(f"So {player} You choose a low risk investment, How much would you like to invest: "))
    if bet <= points:
        points = points - bet
        winnings: int = randint(bet // 2, (bet * 2) - (bet // 2))
        points = points + winnings
        print(f"Your low risk investment left you with a total of {points} dollars")
    else:
        print("Dont lie about your money the irs will get ya")


def main() -> None:
    """Main function that starts all comands."""
    greet()
    intro()
    print(f"The game is over you, {player} you finised with {points} dollars {NAMED_CONSTANT}")

 
"""Is always true for our scope and will start the program."""
if __name__ == "__main__":
    main()