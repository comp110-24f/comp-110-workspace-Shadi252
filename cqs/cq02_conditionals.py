"""My third challenge question in COMP110!"""

__author__ = "730660179"


def guess_a_number() -> None:
    """Input Function"""
    secret: int = 7
    x = str(input("Guess a number:"))
    print("Your guess was " + str(x))
    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
