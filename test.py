import random  # 'random' is Python's built-in module for generating random numbers


def play_game():
    """
    Main function that runs one full round of the guessing game.
    Everything happens inside here: setup, the guessing loop, and the result.
    """

    # --- INTRO ---
    print("=" * 40)  # "=" * 40 just repeats the "=" character 40 times to make a line
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)

    # --- DIFFICULTY SELECTION ---
    print("\nChoose a difficulty:")
    print("1. Easy   (1-50,  10 guesses)")
    print("2. Medium (1-100, 7 guesses)")
    print("3. Hard   (1-200, 5 guesses)")

    # A dictionary mapping each menu choice to a tuple of (max_number, max_attempts).
    # Using a dictionary here avoids writing a long chain of if/elif statements.
    difficulty_settings = {
        "1": (50, 10),
        "2": (100, 7),
        "3": (200, 5),
    }

    # input() always returns a string, so we .strip() it to remove
    # any accidental spaces or newline characters the user might type.
    choice = input("Enter 1, 2, or 3: ").strip()

    # .get(choice, (100, 7)) looks up the user's choice in the dictionary.
    # If the choice isn't found (e.g. they typed "5"), it falls back to Medium settings.
    max_number, max_attempts = difficulty_settings.get(choice, (100, 7))

    # --- GAME SETUP ---
    # random.randint(a, b) picks a random whole number between a and b, inclusive.
    secret_number = random.randint(1, max_number)
    attempts_left = max_attempts  # tracks how many guesses the player has remaining

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

    # --- MAIN GAME LOOP ---
    # This loop keeps running as long as the player still has attempts left.
    # It only stops early if they guess correctly (via 'break') or run out of attempts.
    while attempts_left > 0:
        guess_input = input(f"Attempts left: {attempts_left}. Your guess: ").strip()

        # .isdigit() checks whether the string is made up only of digits (0-9).
        # This protects the game from crashing if the user types letters or symbols.
        if not guess_input.isdigit():
            print("Please enter a valid whole number.\n")
            continue  # skip the rest of the loop and ask again, without using an attempt

        guess = int(guess_input)  # convert the validated string into an actual integer

        # Make sure the guess is within the allowed range for the chosen difficulty.
        if guess < 1 or guess > max_number:
            print(f"Please guess a number between 1 and {max_number}.\n")
            continue  # again, don't use up an attempt for an out-of-range guess

        # A valid, in-range guess was made, so now it costs the player an attempt.
        attempts_left -= 1

        # --- CHECK THE GUESS ---
        if guess == secret_number:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it with {attempts_left} attempt(s) to spare!")
            break  # exit the while loop immediately since the game is won
        elif guess < secret_number:
            print("Too low!\n")   # hint: the secret number is higher than the guess
        else:
            print("Too high!\n")  # hint: the secret number is lower than the guess

        # If this was their last attempt and they still didn't guess it, reveal the answer.
        if attempts_left == 0:
            print(f"\n💥 Out of attempts! The number was {secret_number}.")

    # After the loop ends (win or lose), ask if they want another round.
    play_again()


def play_again():
    """
    Asks the player if they want to play another round.
    If yes, it calls play_game() again, restarting the whole process (recursion).
    If no, it prints a goodbye message and the program ends naturally.
    """
    again = input("\nWould you like to play again? (y/n): ").strip().lower()
    # .lower() makes the comparison work whether they type "Y", "y", "Yes", etc.
    if again == "y":
        print()
        play_game()  # calling play_game() from within itself starts a fresh round
    else:
        print("\nThanks for playing! Goodbye.")


# This is a standard Python convention: the code inside this 'if' block only runs
# when the file is executed directly (not when it's imported as a module elsewhere).
if __name__ == "__main__":
    play_game()  # kick off the first round of the game
