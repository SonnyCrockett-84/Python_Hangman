from tkinter import *
import random
import os
from hangmanpics import HANGMANPICS
from randomWords import randomWord
from menus import *
from userInput import *
import time

# Global variables used for the game

errors = 0
win = False
blanks = []
correctGuess = 0
word = randomWord()
guessedLetters = {0}

for i in range(len(word)):
    blanks.append("_")

# Used to reset the game for another round

def setupGame():
   global errors
   global win
   global blanks
   global correctGuess
   global word
   global guessedLetters

   errors = 0
   win = False
   blanks = []
   correctGuess = 0
   word = randomWord()
   guessedLetters = {0}

   for i in range(len(word)):
        blanks.append("_")

   hangmanLabel.config(text=HANGMANPICS[errors])
   blanksLabel.config(text=blanks)
   hintLabel.config(text="")
   checkLetterButton.config(command=getLetter)

   root.update_idletasks()
   root.update()

# Validate user input
def validateLetter(userInput):
   if len(userInput) == 1 and userInput.isalpha():
      return True
   
   else:
      return False

# Checks if the letter is in the word and updates the labels
def getLetter():
   alreadyGuessed = False        # Bool to check if letter has been guessed already
   correctLetter = False         # Bool to check if letter is in word

   global correctGuess
   global errors
   global win
   global word
   global blanks
   global guessedLetters
   
   entryLetter = entry.get()
   entryLetter = entryLetter.upper()
   alreadyGuessed = letterAlreadyGuessed(guessedLetters, entryLetter)

   if(not validateLetter(entryLetter)):
      hintLabel.config(text="Type in only a single character (a - z)!")
      entry.delete(0, END)

   elif alreadyGuessed:
      hintLabel.config(text="Letter was already guessed")

   elif not(alreadyGuessed):
    guessedLetters.add(entryLetter)
    for c in range(len(word)):
        if word[c] == entryLetter:
            blanks[c] = entryLetter
            correctGuess += 1
            correctLetter = True

    if not(correctLetter):
        errors += 1
        hintLabel.config(text="Letter is not in word")
        hangmanLabel.config(text=HANGMANPICS[errors])
        blanksLabel.config(text=blanks)
        entry.delete(0, END)

    else:
       hangmanLabel.config(text=HANGMANPICS[errors])
       blanksLabel.config(text=blanks)
       hintLabel.config(text="Letter is in the word")
       entry.delete(0, END)

    if(correctGuess == len(word)):
       win = True
       hintLabel.config(text="Word found!")

# Main window for the game
root = Tk()
root.title("Hangman Game")
root.minsize(400, 400)

# Label to print the hangman graphic
hangmanLabel = Label(root, text=HANGMANPICS[errors])
      
# Tells the user if the letter is in the word or not
hintLabel = Label(root, text="")

# Show the blanks and the letters that the player already found
blanksLabel = Label(root, text=blanks)

# Get letter from entry field
entry = Entry(root)

# Button to check the letter the user typed in
checkLetterButton = Button(
    root,
    text="Check letter",
    command=getLetter
)

# Button to play again and reload the game
newGameButton = Button(
   root,
   text="New Game",
   command=setupGame
)

# Button to quit the game
quitHangmanButton = Button(
   root,
   text="Quit",
   command=root.destroy
)

hangmanLabel.pack()
blanksLabel.pack(pady=(5, 10))
hintLabel.pack(pady=(10, 10))
entry.pack(pady=(10, 10))
checkLetterButton.pack(pady=(10, 10))
newGameButton.pack(pady=(10, 10))
quitHangmanButton.pack(pady=(10, 10))

while True:
    while(errors < 6 and not win):
        root.update_idletasks()
        root.update()

    if(win):
        checkLetterButton.config(command="")
        root.update_idletasks()
        root.update()

    else:
        checkLetterButton.config(command="")
        hintLabel.configure(text="You ran out of lives!\nThe word would have been: " + word)
        root.update_idletasks()
        root.update()