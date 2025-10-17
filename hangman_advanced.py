import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# List of words to choose from
secretWords = ["WATER", "GUITAR", "CAT", "SCHOOL", "MOTORCYCLE", "COMPUTER"]
numWords = len(secretWords)

# Select a random word
word = secretWords[random.randint(0, numWords - 1)]

# Array for blanks
blanks = []

# List for already guessed letters
guessedLetters = []

# Create blanks to show the player and show them
for i in range(len(word)):
    blanks.append("_")

for i in range(len(blanks)):
    print(blanks[i], end=" ")

print()

for i in range(2):
    print(word)
    
    for i in range(len(blanks)):
      print(blanks[i], end=" ")

    letter = input("Enter a letter > ")
    letter = letter.upper()

    for c in range(len(word)):
        if word[c] == letter:
            blanks[c] = letter