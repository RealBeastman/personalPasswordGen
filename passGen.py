import random
import string
import os
import time
from random import choice

# Function to check for required file types/paths used by passGen function.
def fileCheck():
    # check for passwords.txt
    if os.path.exists('passwords.txt'):
        print("Passwords file exists.")
    else:
        i = open('passwords.txt', 'w')
        i.close()
    # check for sampleText.txt and write sample text if file does not already exist
    if os.path.exists('sampleText.txt'):
        # checks for sample text to read from if .txt file is empty
        if os.stat('sampleText.txt').st_size == 0:
            f = open('sampleText.txt', 'w')
            print("Sample Text file is empty, adding generic text for use in generating password.")
            f.write("This is sample text. Change this to the text of your choice for added complexity.")
            f.close()
        else:
            print("Sample text file exists.")
    else:
        f = open('sampleText.txt', 'w')
        f.write("This is sample text. Change this to the text of your choice for added complexity.")
        f.close()

# Function to randomize password generation to be appended to user info and written to passwords.txt to save all passwords
def passGen():
    passList = []
    accountName = input("What account is this password for? ")
    username = input("What is your username/email for this account? ")
    # Loop to randomly choose 2 strings from referenced .txt file, and 2 integers both to be added to masterList.
    while len(passList) < 4:
        # randomly selects string and removes punctuation. Than makes sure string is greater than 4 characters to be formatted
        wordSelect = random.choice(open('sampleText.txt').read().split())
        wordSelectPunc = wordSelect.translate(str.maketrans('','', string.punctuation))
        if len(wordSelectPunc) <= 4:
            print("String too short.")
        elif len(wordSelectPunc) > 4:
            # creates random integer as a string
            intGen = str(random.randint(99, 9999))
            # formats wordSelectPunc to randomize casing, and replace letters with symbols
            wordSelectPunc = (''.join(choice((str.upper, str.lower))(c) for c in wordSelectPunc))
            wordSelectFinal = wordSelectPunc
            lettersToSymbols = {'S': '$', 'O': '0', 'G': '8', 'I': '!', 'E': '3', 'A': '@'}
            for letter, symbol in lettersToSymbols.items():
                wordSelectFinal = wordSelectFinal.replace(letter, symbol)
                wordSelectFinal = wordSelectFinal.replace(letter.lower(), symbol)
            # adds formatted text and numbers as strings to passList
            passList += [wordSelectFinal]
            passList += [intGen]
            # shuffles order or variable in list, and removes list formatting
            random.shuffle(passList)
            password = ''.join(passList)

    # Creates final variable containg all info in a single string.
    print("Your password has been saved: " + password)
    finalInfo = (accountName + "\n    " + username + "\n    " + password)

    # Checks for text in designated .txt file. Appends finalInfo to file and closes file.
    if os.stat('passwords.txt').st_size == 0:
        passInfo = open('passwords.txt', 'a')
        passInfo.write(finalInfo)
        passInfo.close()
    else:
        passInfo = open('passwords.txt', 'a')
        passInfo.writelines("\n\n" + finalInfo)
        passInfo.close() 

# Either calls for fileCheck and passGen functions to create new password or closes script based on user input.
def userCheck():
    startGen = input("Would you like to create a new password? (Y/N) ")
    if startGen in ("Y", "y"):
        fileCheck()
        passGen()
    elif startGen in ("N", "n"):
        print("Terminating script\nGoodbye!")
        time.sleep(5)
        exit()
    else:
        print("Input not recognized.")

print("Welcome to the secure password generator!\n")
# Loop to call userCheck function until user input determines an exit
while True:
    userCheck()