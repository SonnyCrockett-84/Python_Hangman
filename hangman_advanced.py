import random
import os
from tkinter import *
from tkinter import messagebox

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


###
#
# GUI setup
#
###


root = Tk()
title = Label(root, text="Hangman Game")
title.pack()
root.geometry("400x600")

# Main function
def main():
    letter = letter_var.get()
    letter = letter.upper()
    alreadyGuessed = alreadyGuessed_var.get()
    correctLetter = correctLetter_var.get()
    errors = errors_var.get()
    correctGuess = correctGuess_var.get()
  
   # Only continue if the user type a single letter
    if(len(letter) > 1 or not letter.isalpha()):
      messagebox.showinfo("Incorrect input", "Please type in only a single letter (a - z)!")

    else:

      # Check if letter has been guessed already
      for d in guessedLetters:
        if(letter == d):
          messagebox.showinfo("Letter already guessed", "This letter has already been guessed!")
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

# List of words to choose from
secretWords = ["WATER", "GUITAR", "CAT", "SCHOOL", "MOTORCYCLE", "COMPUTER", "CARAMEL", "COWS", "HUMOR", "CAMPBOARD"]
numWords = len(secretWords)

clear = lambda: os.system("cls")

# Variable to check if the player wants to play again
play = 'y'

while(play == 'y'):
  # Select a random word
  word = secretWords[random.randint(0, numWords - 1)]

  # Array for blanks
  blanks = []

  # List for already guessed letters
  guessedLetters = {0}

  # Number of correctly guessed letter
  correctGuess_var = IntVar(root, value=0)

  # Bool to check if player won
  win = False

  # Create blanks to show the player and prints them
  for i in range(len(word)):
      blanks.append("_")

  # Number of errors
  errors_var = IntVar(root, value=0)

  # Player has 5 tries to find the correct word
  while(errors_var.get() < 6 and not win):
      alreadyGuessed_var = BooleanVar(root, value=False)        # Bool to check if letter has been guessed already
      correctLetter_var = BooleanVar(root, value=False)         # Bool to check if letter is in word

      # print the current hangman pic
      hangman_label =  Label(root,
                             text=HANGMANPICS[errors_var.get()],
                             anchor=CENTER,
                             justify=CENTER)
      
      hangman_label.pack(pady=20)

      # Used for debugging
      # print(word)
      
      # Show the blanks and the letters that the player already found
      for i in range(len(blanks)):
        print(blanks[i], end=" ")

      blanks_label = Label(root,
                           text = blanks,
                           anchor=CENTER,
                           justify=CENTER)
      
      blanks_label.pack()

      letter_var = StringVar()

      # Get letter from user
      letter_entry = Entry(root,
                     text="Enter a letter > ",
                     justify=CENTER,
                     textvariable=letter_var)
      
      letter_entry.pack(pady=50)

      check_button = Button(text="Check letter", command = main)
      check_button.pack()

      root.mainloop()

      


  # Print winning screen
  if(win):
    print("Congratulations, you found the word!")

  # Print last hangman pic and show the word to the player 
  else:
    print(HANGMANPICS[6])
    print("You loose. The word would have been", word)

  print("Do you want to play again?")
  play = input("Type y for yes or any other character to quit > ")