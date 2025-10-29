def getLetter():
    letter = input("Enter a letter > ")
    letter = letter.upper()
    return letter


def checkInput(letter):
   if(len(letter) > 1 or not letter.isalpha()):
        print("Please type in only a single letter (a - z)!")
        return False
   
   return True