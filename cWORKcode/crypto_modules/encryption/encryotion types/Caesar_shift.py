import random
def Ceasar_encrypt(text):
    text = text.lower()                                 # makes the text lower case
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    shifts, newText = random.randint(1, 26), ""         # these lines define the variables
    for letter in text:                                 # this line loops through the text
        try:
            finder = alphabet.index(letter) + shifts    # these lines find the equivalent letter
            if finder > 25: finder = finder - 26
            newText = newText + alphabet[finder]        # this line builds the new string
        except: newText = newText + letter              # this line adds any symbol in the text
    return newText                                      # this line returns the new function

def Ceasar_decrypt(text, shifts):
    text = text.lower()                                 # makes the text lower case
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    newText = ""                                        # these lines define the variables
    for letter in text:                                 # this line loops through the text
        try:
            finder = alphabet.index(letter) - shifts    # these lines find the equivalent letter
            if finder < 0: finder = finder + 26
            newText = newText + alphabet[finder]        # this line builds the new string
        except: newText = newText + letter              # this line adds any symbol in the text
    return newText                                      # this line returns the new function
