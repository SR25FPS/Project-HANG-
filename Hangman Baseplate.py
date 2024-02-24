import random

# List of words
words = ["programming","python","hangman","sr25","sir clyde"]

def select_word(words):
    return random.choice(words)

def get_hangman_stage(remaining_attempts):
    max_attempts = 5
    stages = [
        """
        ------
        |    |
        |    |
        |    |
        |    |
        |    |
        ------------
        """,
        """
        ------
        |    |
        |    O
        |    |
        |    |
        |    |
        ------------
        """,
        """
        ------
        |    |
        |    O
        |    | ]
        |    |
        |    |
        ------------
        """,
        """
        ------
        |    |
        |    O
        |  [ | ]
        |    |
        |    |
        ------------
        """,
        """
        ------
        |    |
        |    O
        |  [ | ]
        |    |
        |    | ]
        ------------
        """,
        """
        THE MAN WAS HANGED
        """
        
    ]
    return stages[max_attempts - remaining_attempts]


secret_word = select_word(words)
guessed_letters = ""
remaining_attempts = 5

print("Welcome to Hangman!")
print(get_hangman_stage(remaining_attempts))

while remaining_attempts > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
            print("You already guessed that letter.")
    elif guess in secret_word:
            guessed_letters += guess
            print("Correct guess!")
    else:
        guessed_letters += guess
        remaining_attempts -= 1
        print(f"Wrong guess! {remaining_attempts} attempts remaining.")

# Word Checker

    if all(letter in guessed_letters for letter in secret_word):
        print(f"Congratulations! You guessed the word: {secret_word}")
        break

    print(get_hangman_stage(remaining_attempts))

    if remaining_attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was: {secret_word}")