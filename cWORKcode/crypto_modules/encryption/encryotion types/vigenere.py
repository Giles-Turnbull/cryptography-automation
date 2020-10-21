from textwrap import wrap
def formatKeyFunc(key):     # these lines format the key into a list of places in the alphabet
    keyBuild, keyNum = "", []
    for letter in key:
        if letter.upper() != " ": keyBuild = keyBuild + letter.upper()
    for letter in keyBuild: keyNum.append(ord(letter) - 65)
    return keyNum


def formatTextFunc(text):       # these lines format the text by removing all spaces and making letters capital
    textBuild = ""
    for letter in text:
        if letter.upper() != " ": textBuild = textBuild + letter.upper()
    return textBuild


def encrypt(text, key):         # this function encrypts the text
    text = formatTextFunc(text) # these lines format the info being passed to the function
    key = formatKeyFunc(key)
    count  = -1
    textBuild, period, finalBuild = "", 5, ""
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for letter in text:         # these lines encrypt the text by using the key to move places along the alphabet
        count += 1
        if count > (len(key)-1): count = 0
        move = alphabet.index(letter) + int(key[count])
        if move > (len(alphabet)- 1): move = move - 26
        textBuild = textBuild + alphabet[move]
    textBuild = wrap(textBuild, period)     # these lines format the result
    for i in textBuild: finalBuild = finalBuild + i + " "
    return finalBuild[:-1]

def decrypt(text, key):         # this function decrypts the text
    text = formatTextFunc(text) # these lines format the info being passed to the function
    key = formatKeyFunc(key)
    count  = -1
    textBuild, period, finalBuild = "", 5, ""
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for letter in text:         # these lines reverse the process in the encryption process
        count += 1
        if count > (len(key)-1): count = 0
        move = alphabet.index(letter) - int(key[count])
        if move < 0: move = move + 26
        textBuild = textBuild + alphabet[move]
    return textBuild
