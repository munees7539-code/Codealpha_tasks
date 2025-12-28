import random

# List of predefined words
words = ["python", "coding", "alpha", "intern", "program"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("\n😢 Game Over")
    print("The word was:", word)
