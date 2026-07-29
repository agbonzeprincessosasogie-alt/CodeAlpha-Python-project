import random

words = ["python", "computer", "banana", "backend", "github"]

word = random.choice(words)

guessed_letters = []

attempts = 6

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess.")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The word was:", word)