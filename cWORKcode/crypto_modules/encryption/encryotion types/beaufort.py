from textwrap import wrap

def formatKeyFunc(text, key):   # these lines format the key so it is repeated as many times as the text
    count, keyBuild = -1, ""
    for i in range(len(text)):
        count += 1
        if count > (len(key) - 1): count = 0
        keyBuild = keyBuild + key[count].upper()
    return keyBuild


def formatTextFunc(text):       # these lines format the text by removing all spaces and making letters capital
    textBuild = ""
    for letter in text:
        if letter.upper() != " ": textBuild = textBuild + letter.upper()
    return textBuild

def encrypt(text, key):         # these lines encrypt the given text using the given key
    text = formatTextFunc(text)
    key = formatKeyFunc(text, key)
    period, textFinal = 5, ""
    alphabet, matrix, textBuild = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], [], ""
    count = -1
    for i in range(26):     # these lines create a matrix of the alphabet
        count += 1
        matrix.append(alphabet[count:] + alphabet[:count])
    for pl, letter in enumerate(text):              # these lines carry out the encryption
        place = matrix[0].index(letter)
        for row in matrix:
            if row[place] == key[pl]: textBuild = textBuild + row[0]
    textBuild = wrap(textBuild, period)             # these line format the output
    for i in textBuild: textFinal = textFinal + i + " "
    return textFinal[:-1]

def decrypt(text, key):         # these lines encrypt the given text using the given key
    text = formatTextFunc(text)
    key = formatKeyFunc(text, key)
    alphabet, matrix, textBuild = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], [], ""
    count = -1
    for i in range(26):     # these lines create a matrix of the alphabet
        count += 1
        matrix.append(alphabet[count:] + alphabet[:count])
    for pl, letter in enumerate(text):              # these lines carry out the encryption
        for row in matrix:
            if row[0] == letter:
                place = row.index(key[pl])
                textBuild = textBuild + matrix[0][place]
    return textBuild

