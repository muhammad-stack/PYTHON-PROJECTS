"""Bagels, by Al Sweigart al@inventwithpython.com
 2. A deductive logic game where you must guess a number based on clues.
 3. View this code at https://nostarch.com/big-book-small-python-projects
 4. A version of this game is featured in the book "Invent Your Own
 5. Computer Games with Python" https://nostarch.com/inventwithpython
 6. Tags: short, game, puzzle"""

import random


NUM_DIGITS: int = 3

MAX_GUESSES: int = 10


def main():
    print("""Bagels a deductive logic game BY AI Sweigart
     I am thinking of a {}-digit number with no repeated digits. Try to guess what it is. Here are some clues:
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
    For example, if the secret number was 248 and your guess was 843 , the clues would be Fermi
    Pico .""".format(NUM_DIGITS))

    while True:  # Main Loop
        # This stores the secret number the player needs to guess
        secret_number = getSecretNum()
        print("I have thought of a number. You have {} guesses to get it .".format(
            MAX_GUESSES))

        numGuesses: int = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdigit():
                print("Guess #{}: ".format(numGuesses))
                guess = input('>')
            clues = getClues(guess=guess, secret_num=secret_number)
            print(clues)
            numGuesses += 1

            if guess == secret_number:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print("You've run out of guesses. The number was{}.".format(
                    secret_number))
        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y' or 'yes'):
            break  # They don't want to play again, so break out of the main loop.
        print("Thanks for playing !")


def getSecretNum() -> str:
    """Returns a string made up of  NUM_DIGITS  unique random digits."""
    numbers: list[str] = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def getClues(guess: str, secret_num: str) -> str:
    if guess == secret_num:
        return " You got it!"
    clues: list[str] = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.

        # clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


if __name__ == '__main__':
    main()

