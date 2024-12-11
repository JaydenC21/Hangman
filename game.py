import random

def pick_random_word(word_list):
    return random.choice(word_list)

def update_display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    word_list = ["serendipitiously", "jazz", "xylophone", "zygote", "jubilant"]

    secret_word = pick_random_word(word_list)

    guessed_letters = set()
    attempts_remaining = 6
    guesses = 0

    print("Welcome to Hangman!")

    while attempts_remaining > 0:
        display_word = update_display_word(secret_word, guessed_letters)
        print("\nWord:", display_word)
        print("Attempts remaining:", attempts_remaining)
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        guesses += 1

        if guess in secret_word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print("\nCongratulations! You guessed the word '" + secret_word + "' in", guesses, "guesses!")
                break
        else:
            print("Wrong guess.")
            attempts_remaining -= 1

    if attempts_remaining == 0:
        print("\nGame over! The word was:", secret_word)

if __name__ == "__main__":
    play_hangman()
