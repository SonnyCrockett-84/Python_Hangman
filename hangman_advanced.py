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
guessedLetters = {0}

# Boolean to check if letter was already guessed
alreadyGuessed = False

# Boolean to check if letter is in word
correctLetter = False

# Create blanks to show the player and show them
for i in range(len(word)):
    blanks.append("_")

# Number of errors
errors = 0

print()

while(errors < 6):
    alreadyGuessed = False
    correctLetter = False

    print(HANGMANPICS[errors])

    print(word)
    
    for i in range(len(blanks)):
      print(blanks[i], end=" ")

    letter = input("Enter a letter > ")
    letter = letter.upper()

    for d in guessedLetters:
        if(letter == d):
            print("This letter has already been guessed!")
            alreadyGuessed = True

    if not(alreadyGuessed):
        guessedLetters.add(letter)
        for c in range(len(word)):
          if word[c] == letter:
            blanks[c] = letter
            correctLetter = True

        if not(correctLetter):
          errors += 1