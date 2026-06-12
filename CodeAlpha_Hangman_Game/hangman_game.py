import random
import time

print("=" * 50)
print("        ADVANCED HANGMAN GAME")
print("=" * 50)

easy_words = ["cat", "dog", "sun", "pen", "book"]
medium_words = ["python", "coding", "laptop", "mobile", "school"]
hard_words = ["algorithm", "database", "developer", "artificial", "technology"]

print("\nSelect Difficulty Level")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    word = random.choice(easy_words)
elif choice == "2":
    word = random.choice(medium_words)
elif choice == "3":
    word = random.choice(hard_words)
else:
    print("Invalid Choice. Medium level selected.")
    word = random.choice(medium_words)

display = []

for letter in word:
    display.append("_")

attempts = 8
score = 0
guessed_letters = []

stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

while attempts > 0:

    print("\nCurrent Word :", " ".join(display))
    print("Attempts Left :", attempts)
    print("Score :", score)
    print("Used Letters :", guessed_letters)

    guess = input("Enter a Letter : ").lower()

    if guess in guessed_letters:
        print("Letter already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
                score += 10

    else:
        print("Wrong Guess!")
        attempts -= 1

        stage_index = min(6, 8 - attempts)
        print(stages[stage_index - 1])

    if "_" not in display:
        print("\nCongratulations!")
        print("You Guessed the Word :", word)
        print("Final Score :", score)
        break

if "_" in display:
    print("\nGame Over!")
    print("Correct Word Was :", word)
    print("Your Score :", score)

print("\nThank You For Playing Advanced Hangman Game")
print("=" * 50)