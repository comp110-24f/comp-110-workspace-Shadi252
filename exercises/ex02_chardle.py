__author__ = "730660179"


def input_word() -> str:
    """Prompts the user to input a 5-character word."""
    word: str = input("Enter a 5-character word: ")  # Asking user to enter a word
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """Prompts the user to input a single character."""
    letter: str = input(
        "Enter a single character: "
    )  # Asks user to enter a single character
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """Checks if a letter is in the word and how many times."""
    count: int = 0
    print("Searching for " + letter + " in " + word)

    # Check each index in the word and print if letter is found
    for i in range(len(word)):
        if letter == word[i]:
            print(letter + " found at index " + str(i))
            count += 1

    # Print the number of occurrences
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Main function to tie input and check functions together."""
    word: str = input_word()  # Prompt for a 5-character word
    letter: str = input_letter()  # Prompt for a single character
    contains_char(word, letter)  # Check if the letter is in the word


if __name__ == "__main__":
    main()
