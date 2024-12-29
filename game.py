#Importing random module
import random

#Selecting a random word from the word bank
def randomWord(wordList):
    return random.choice(wordList)

#Displaying hangman and word
def updateDisplayWord(word, guessed, lives):
    if lives == 6:
        print("\n   ___")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("______|___")
    elif lives == 5:
        print("\n   ___")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("______|___")
    elif lives == 4:
        print("\n   ___")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("______|___")
    elif lives == 3:
        print("\n   ___")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("______|___")
    elif lives == 2:
        print("\n   ___")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("______|___")
    else:
        print("\n   ___")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("______|___")
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

#Main game loop
def playHangman():
    wordList = ["serendipitiously", "exacerbate", "jazz", "xylophone", "zygote", "jubilant", "denouement", "penultimate", "hippopotomonstrosesquippedaliophobia", "zeal"]

    word = randomWord(wordList)

    guessed = set()
    livesRemaining = 6
    guesses = 0

    print("\nWelcome to Hangman!")

    while livesRemaining > 0:
        displayWord = updateDisplayWord(word, guessed, livesRemaining)
        print("\nWord:", displayWord)
        print("Attempts Remaining:", livesRemaining)
        print("Guessed Letters:", ", ".join(sorted(guessed)))

        guess = input("Enter a letter: ").lower()
        
        #Checking for invalid inputs
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)
        guesses += 1

        #Correct guess
        if guess in word:
            print("Good guess!")
            if all(letter in guessed for letter in word):
                print("\nCongratulations! You guessed the word '" + word + "' in", guesses, "guesses with " + str(livesRemaining) + " lives remaining! :D")
                break

        #Incorrect guess
        else:
            print("Sorry, incorrect guess!")
            livesRemaining -= 1
    
    #Lose
    if livesRemaining == 0:
        print("\n   ___")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("______|___")
        print("\nGame over! The word was:", word)

#Run game loop
playHangman()