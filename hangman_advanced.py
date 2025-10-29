import random
import os
from hangmanpics import HANGMANPICS
from randomWords import randomWord
from menus import *
from userInput import getLetter, checkInput

def checkInput(letter):
   if(len(letter) > 1 or not letter.isalpha()):
        print("Please type in only a single letter (a - z)!")
        return False
   
   return True

clear = lambda: os.system("cls")

startScreen()
                                                                     
clear()

# Variable to check if the player wants to play again
play = 'y'

while(play == 'y'):

  # Clear console
  clear()

  # Select a random word
  word = randomWord()

  # Array for blanks
  blanks = []

  # List for already guessed letters
  guessedLetters = {0}

  # Number of correctly guessed letter
  correctGuess = 0

  # Bool to check if player won
  win = False

  # Create blanks for the secret word
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
      
      # Show the blanks and the letters that the player already found
      printBlanks(blanks)

      # Get letter from user
      letter = getLetter()

      if(checkInput(letter)):

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

  endScreen(win)

  play = playAgain()