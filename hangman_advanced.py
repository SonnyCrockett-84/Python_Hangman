import random
import tkinter as tk
import os
from hangmanpics import HANGMANPICS
from randomWords import randomWord
from menus import *
from userInput import *

clear = lambda: os.system("cls")

startScreen()

# Variable to check if the player wants to play again
play = 'y'

while(play == 'y'):
  # Select a random word
  word = randomWord()

  # Array for blanks
  blanks = []

  # List for already guessed letters
  guessedLetters = {0}

  # Number of correctly guessed letter
  correctGuess_var = IntVar(root, value=0)

  # Bool to check if player won
  win = False

  # Create blanks for the secret word
  for i in range(len(word)):
      blanks.append("_")

  # Number of errors
  errors_var = IntVar(root, value=0)

  # Player has 5 tries to find the correct word
  while(errors_var.get() < 6 and not win):
      alreadyGuessed_var = BooleanVar(root, value=False)        # Bool to check if letter has been guessed already
      correctLetter_var = BooleanVar(root, value=False)         # Bool to check if letter is in word

      # print the current hangman pic
      print(HANGMANPICS[errors])
      
      # Show the blanks and the letters that the player already found
      printBlanks(blanks)

      blanks_label = Label(root,
                           text = blanks,
                           anchor=CENTER,
                           justify=CENTER)
      
      blanks_label.pack()

      letter_var = StringVar()

      # Get letter from user
      letter = getLetter()

      if(checkInput(letter)):

        # Check if letter has been guessed already
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