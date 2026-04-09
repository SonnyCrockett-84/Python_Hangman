import random
import tkinter as tk
import os
from hangmanpics import HANGMANPICS
from randomWords import *
from menus import *
from userInput import *

clear = lambda: os.system("cls")

startScreen()

# Variable to check if the player wants to play again
play = 'y'

while(play == 'y'):
<<<<<<< HEAD

  # Clear console
  clear()

  # Select a random word from my list
=======
  # Select a random word
>>>>>>> gui
  word = randomWord()

  # Select a random word from the english dictionary
  # word = randomDictionaryWord()

  # Array for blanks
  blanks = []

  # List for already guessed letters
  guessedLetters = {0}

<<<<<<< HEAD
  # Number of correctly guessed letter
  correctGuess = 0

=======
  # Bool to check if player won
>>>>>>> gui
  win = False

  # Create blanks for the secret word
  for i in range(len(word)):
      blanks.append("_")

  errors = 0

  correctGuess = 0

  # Player has 5 tries to find the correct word
  while(errors < 6 and not win):
<<<<<<< HEAD
      alreadyGuessed = False
      correctLetter = False
=======
      alreadyGuessed = False       # Bool to check if letter has been guessed already
      correctLetter = False        # Bool to check if letter is in word
>>>>>>> gui

      print(HANGMANPICS[errors])
      
      printBlanks(blanks)

      letter = getLetter()

      # Check if input is 1 character and a letter
      if(checkInput(letter)):

        alreadyGuessed = letterAlreadyGuessed(guessedLetters, letter)

        if not(alreadyGuessed):
            guessedLetters.add(letter)
            for c in range(len(word)):
              if word[c] == letter:
                blanks[c] = letter
                correctGuess += 1
                correctLetter = True

            if not(correctLetter):
              errors += 1

        else:
           print("This letter has already been guessed!") 

        if(correctGuess == len(word)):
              win = True

  endScreen(win, word)

  play = playAgain()