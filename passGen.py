import random
import string
from random import choice

# Dictionary to reference and change letters in a string.
lettersToSymbols = {
    'S': '$',
    'O': '0',
    'G': '8',
    'I': '!',
    'E': '3',
    'A': '@'
}

# Loop to randomly choose 2 strings from referenced .txt file, and 2 integers both to be added to masterList.
def passGen():
    global masterList
    masterList = [] 
    while len(masterList) < 4:
        # randomly selects string and removes punctuation. Than makes sure string is greater than 4 characters to be formatted.
        wordSelect = random.choice(open("sampleText.txt").read().split())
        wordSelectPunc = wordSelect.translate(str.maketrans('','', string.punctuation))
        if len(wordSelectPunc) <= 4:
            print("String too short.")
        elif len(wordSelectPunc) > 4:
            # creates random integer and converts to string.
            intGen = random.randint(99, 9999)
            intStr = str(intGen)
            # formats wordSelectPunc to randomize casing, and replace letters with symbols.
            wordSelectPunc = (''.join(choice((str.upper, str.lower))(c) for c in wordSelectPunc))
            wordSelectFinal = wordSelectPunc
            for letter, symbol in lettersToSymbols.items():
                wordSelectFinal = wordSelectFinal.replace(letter, symbol)
                wordSelectFinal = wordSelectFinal.replace(letter.lower(), symbol)
            masterList += [wordSelectFinal]
            masterList += [intStr]

# Calls passGen function
passGen()

# Shuffles list and returns joined string.
random.shuffle(masterList)
password = ''.join(masterList)

# Prints final result to user.
print(password)




