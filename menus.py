from hangmanpics import HANGMANPICS
import os

clear = lambda: os.system("cls")

# Start screen
def startScreen():
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

# Print blanks
def printBlanks(blanks):
   for i in range(len(blanks)):
        print(blanks[i], end=" ")
   
   print("\n")

# Print winning/loose screen
def endScreen(win, word):

   # Print winning screen
  if(win):
    print("Congratulations, you found the word!")

  # Print last hangman pic and show the word to the player 
  else:
    print(HANGMANPICS[6])
    print("You loose. The word would have been", word)


# Print play again screen
def playAgain():
   print("Do you want to play again?")
   choice = input("Type y for yes or any other character to quit > ")
   return choice