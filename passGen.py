import random

# Randomizes word selection from attached .txt file and applies it to a global variable. Loops until selected string is greater than 4 characters.
def wordGen():   
    while True:
        global wordSelect
        wordSelect = random.choice(open("sampleText.txt").read().split())
        if len(wordSelect) <= 4:
            print(wordSelect + " is too short, trying again")
        elif len(wordSelect) > 4:
            break

# Randomizes capitalization for selected string.
def capsGen():
    from random import choice
    global capChaStr
    capChaStr = (''.join(choice((str.upper, str.lower))(c) for c in wordSelect))

# Creates random integer variable and converts to string.
def numbGen():
    intGen = random.randint(10000, 100000)
    global intStr
    intStr = str(intGen)

# Dictionary to reference and change letters in a string.
lettersToSymbols = {
    'S': '$',
    'O': '0',
    'G': '8',
    'I': 'i',
    'E': '3',
    'A': '@'
}

# Calls lengthCheck for a word, and replaces certain letters with symbols.
wordGen()
capsGen()
finWord1 = capChaStr
for letter, symbol in lettersToSymbols.items():
    finWord1 = finWord1.replace(letter, symbol)
    finWord1 = finWord1.replace(letter.lower(), symbol)

# Calls lengthCheck for a second word, and replaces certain letters with symbols.
wordGen()
capsGen()
finWord2 = capChaStr
for letter, symbol in lettersToSymbols.items():
    finWord2 = finWord2.replace(letter, symbol)
    finWord2 = finWord2.replace(letter.lower(), symbol)

# Calls numbGen function to create a random integer.
numbGen()

# Creates list containing final variables, shuffles order and converts to joined string.
passList = list([finWord1, finWord2, intStr])
random.shuffle(passList)
strList = ''.join(passList)

# Prints out final password.
print(strList)




