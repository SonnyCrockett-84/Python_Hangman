import random

dictionary = []

with open("dictionary.txt") as file:
    for x in file:
        dictionary.append(x)

# List of words to choose from
secretWords = ["WATER", "GUITAR", "CAT", "SCHOOL", "MOTORCYCLE", "COMPUTER", "CARAMEL", "COWS", "HUMOR",
               "CAMPBOARD", "TELEVISION", "MUSIC", "CHOCOLATE", "TEA", "PYTHON", "ROCKABILLY"]


def randomDictionaryWord():
    return dictionary[random.randint(0, len(dictionary) - 1)]

def randomWord():
    return secretWords[random.randint(0, len(secretWords) - 1)]