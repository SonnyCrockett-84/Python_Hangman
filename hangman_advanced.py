import random
import os

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
secretWords = ["WATER", "GUITAR", "CAT", "SCHOOL", "MOTORCYCLE", "COMPUTER", "CARAMEL", "COWS", "HUMOR", "CAMPBOARD"]
numWords = len(secretWords)

clear = lambda: os.system("cls")
clear()

print("\n")
print(" ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ ")
print("▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ")
print("▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒")
print("░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒")
print("░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░")
print(" ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ")
print(" ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░")
print(" ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ ")
print(" ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ ")
print("\n")
input("Press any key to start > ")
                                                                     
clear()

# Variable to check if the player wants to play again
play = 'y'

while(play == 'y'):

  # Clear console
  clear()

  # Select a random word
  word = secretWords[random.randint(0, numWords - 1)]

  # Array for blanks
  blanks = []

  # List for already guessed letters
  guessedLetters = {0}

  # Number of correctly guessed letter
  correctGuess = 0

  # Bool to check if player won
  win = False

  # Create blanks to show the player and prints them
  for i in range(len(word)):
      blanks.append("_")

  # Number of errors
  errors = 0

  # Player has 5 tries to find the correct word
  while(errors < 6 and not win):
      alreadyGuessed = False        # Bool to check if letter has been guessed already
      correctLetter = False         # Bool to check if letter is in word

      # print the current hangman pic
      print(HANGMANPICS[errors])

      # Used for debugging
      # print(word)
      
      # Show the blanks and the letters that the player already found
      for i in range(len(blanks)):
        print(blanks[i], end=" ")

      print("\n")

      # Get letter from user
      letter = input("Enter a letter > ")
      letter = letter.upper()

      # Only continue if the user type a single letter
      if(len(letter) > 1 or not letter.isalpha()):
        print()
        print("Please type in only a single letter (a - z)!")

      else:

        # Check if letter has been guessed already
        for d in guessedLetters:
            if(letter == d):
              print("This letter has already been guessed!")
              alreadyGuessed = True

        if not(alreadyGuessed):
            guessedLetters.add(letter)
            for c in range(len(word)):
              if word[c] == letter:
                blanks[c] = letter
                correctGuess += 1
                correctLetter = True

            if not(correctLetter):
              errors += 1

        if(correctGuess == len(word)):
          win = True


  # Print winning screen
  if(win):
    print("Congratulations, you found the word!")

  # Print last hangman pic and show the word to the player 
  else:
    print(HANGMANPICS[6])
    print("You loose. The word would have been", word)

  print("Do you want to play again?")
  play = input("Type y for yes or any other character to quit > ")