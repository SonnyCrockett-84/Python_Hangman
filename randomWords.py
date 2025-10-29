import random

# List of words to choose from
secretWords = ["WATER", "GUITAR", "CAT", "SCHOOL", "MOTORCYCLE", "COMPUTER", "CARAMEL", "COWS", "HUMOR",
               "CAMPBOARD", "TELEVISION", "MUSIC", "CHOCOLATE", "TEA", "PYTHON", "ROCKABILLY"]

def randomWord():
    return secretWords[random.randint(0, len(secretWords) - 1)]