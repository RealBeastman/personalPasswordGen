import random
import string
from random import choice

# Dictionary to reference and change letters in a string.
lettersToSymbols = {
    'S': '$',
    'O': '0',
    'G': '8',
    'I': 'i',
    'E': '3',
    'A': '@'
}

# Loop to randomly choose 2 strings to be formatted and added to masterList.
def wordGen():
    global masterList
    masterList = [] 
    while len(masterList) < 2:
        # randomly selects string and remove punctuation. Than make sure string is greater than 4 characters to be formatted.
        wordSelect = random.choice(open("sampleText.txt").read().split())
        wordSelectPunc = wordSelect.translate(str.maketrans('','', string.punctuation))
        if len(wordSelectPunc) <= 4:
            print("String too short.")
        elif len(wordSelectPunc) > 4:
            # formats wordSelectPunc to randomize casing, and replace letters with symbols.
            wordSelectPunc = (''.join(choice((str.upper, str.lower))(c) for c in wordSelectPunc))
            wordSelectFinal = wordSelectPunc
            for letter, symbol in lettersToSymbols.items():
                wordSelectFinal = wordSelectFinal.replace(letter, symbol)
                wordSelectFinal = wordSelectFinal.replace(letter.lower(), symbol)
            masterList += [wordSelectFinal]
        
# Creates random integer variable and converts to string.
def numbGen():
    global intStr
    intGen = random.randint(10000, 100000)
    intStr = str(intGen)

# Calls wordGen and numbGen functions.
wordGen()
numbGen()

# Adds numbGen returned variable to masterList
masterList += [intStr]

# Shuffles list and returns joined string.
random.shuffle(masterList)
password = ''.join(masterList)

# Prints final result to user.
print(password)




