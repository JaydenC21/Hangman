import random

def randomWord(wordList):
    return random.choice(wordList)

def updateDisplayWord(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def playHangman():
    wordList = ["serendipitiously", "exacerbate", "jazz", "xylophone", "zygote", "jubilant", "denouement", "penultimate", "hippopotomonstrosesquippedaliophobia", "zeal"]

    word = randomWord(wordList)

    guessed = set()
    livesRemaining = 6
    guesses = 0

    print("Welcome to Hangman!")

    while livesRemaining > 0:
        displayWord = updateDisplayWord(word, guessed)
        print("\nWord:", displayWord)
        print("Attempts Remaining:", livesRemaining)
        print("Guessed Letters:", ", ".join(sorted(guessed)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)
        guesses += 1

        if guess in word:
            print("Good guess!")
            if all(letter in guessed for letter in word):
                print("\nCongratulations! You guessed the word '" + word + "' in", guesses, "guesses!")
                break
        else:
            print("Sorry, incorrect guess!")
            livesRemaining -= 1

    if livesRemaining == 0:
        print("\nGame over! The word was:", word)

playHangman()