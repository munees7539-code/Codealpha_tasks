import random

# List of predefined words
words = ["python", "java", "cloud", "docker", "linux"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")

while attempts > 0:
    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print("Guessed Letters:", guessed_letters)
    print("Attempts Left:", attempts)

    # Check if player has won
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Guess a letter: ").lower()

    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess!\n")
    else:
        print("✅ Correct guess!\n")

# If player loses
if attempts == 0:
    print("\n😢 Game Over! The word was:", word)
