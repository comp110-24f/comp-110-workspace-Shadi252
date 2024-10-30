"""Wordle Game Excersise 2"""

__author__ = "730660179"


def input_guess(secret_len: int) -> str:
    guess: str = input(f"Enter a {secret_len} character word: ")
    while len(guess) != secret_len:  # Asking the player for input guess
        guess = input(f"That wasn't {secret_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, search_char: str) -> bool:
    assert len(search_char) == 1
    count: int = 0
    idx = 0
    while idx < len(secret_word):  # Funcrion to Search for character
        if secret_word[idx] == search_char:
            count += 1
        idx += 1
    if count != 0:
        return True
    else:
        return False


def emojified(player_guess: str, secret_word: str) -> str:
    assert len(player_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"  # These codes are emojis
    emoji_str: str = ""
    idx = 0
    while idx < len(secret_word):  # length of secret vs index
        if player_guess[idx] == secret_word[idx]:
            emoji_str += GREEN_BOX
        elif contains_char(secret_word, player_guess[idx]) == True:
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
        idx += 1
    return emoji_str


def main(secret: str) -> None:
    player_turn: int = 1
    while player_turn < 7:  # Evaluates which turn player is on
        print(f"=== Turn {player_turn}/6 ===")
        player_guess = input_guess(len(secret))
        print(emojified(player_guess, secret))
        if player_guess == secret:
            print(f" You won in {player_turn}/6 turns!")
            return
        player_turn += 1
    print("X/6 - Sorry, try again tomorrow!")  # End comment
    return


if __name__ == "__main__":
    main(secret="codes")
