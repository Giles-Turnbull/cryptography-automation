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


def create_matrix():        # these lines create a matrix (tableau) to encrypt the text
    rowOneAlphabet = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    rowTwoAlphabet = ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "M", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    rowThreeAlphabet = ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "L", "M", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    rowFourAlphabet = ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "K", "L", "M", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    rowFiveAlphabet = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "J", "K", "L", "M", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
    rowSixAlphabet = ["S", "T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "I", "J", "K", "L", "M", "A", "B", "C", "D", "E", "F", "G", "H"]
    rowSevenAlphabet = ["T", "U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R","S", "H", "I", "J", "K", "L", "M", "A", "B", "C", "D", "E", "F", "G"]
    rowEightAlphabet = ["U", "V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "G", "H", "I", "J", "K", "L", "M", "A", "B", "C", "D", "E", "F"]
    rowNineAlphabet = ["V", "W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "F", "G", "H", "I", "J", "K", "L", "M", "A", "B", "C", "D", "E"]
    rowTenAlphabet = ["W", "X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "E", "F", "G", "H", "I", "J", "K", "L", "M", "A", "B", "C", "D"]
    rowElevenAlphabet = ["X", "Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "A", "B", "C"]
    rowTwelveAlphabet = ["Y", "Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "A", "B"]
    rowThirteenAlphabet = ["Z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "A"]
    matrix, textBuild = [rowOneAlphabet, rowTwoAlphabet, rowThreeAlphabet, rowFourAlphabet, rowFiveAlphabet, rowSixAlphabet, rowSevenAlphabet, rowEightAlphabet, rowNineAlphabet, rowTenAlphabet, rowElevenAlphabet, rowTwelveAlphabet, rowThirteenAlphabet], ""
    return matrix


def encrypt(text, key):         # these lines encrypt the given text using the given key
    text = formatTextFunc(text)
    key = formatKeyFunc(text, key)
    period, textFinal, textBuild = 5, "", ""
    matrix = create_matrix()
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keyCol = ["AB", "CD", "EF", "GH", "IJ", "KL", "MN", "OP", "QR", "ST", "UV", "WX", "YZ"]
    for pl, letter in enumerate(text):              # these lines carry out the encryption process
        for pl2, keySet in enumerate(keyCol):
            if key[pl] in keySet: place = pl2
        find = matrix[place].index(letter)
        textBuild = textBuild + alphabet[find]
    textBuild = wrap(textBuild, period)         # these lines format the return
    for i in textBuild: textFinal = textFinal + i + " "
    return textFinal

def decrypt(text, key):         # these lines decrypt the given text using the given key
    text = formatTextFunc(text)
    key = formatKeyFunc(text, key)
    period, textFinal, textBuild = 5, "", ""
    matrix = create_matrix()
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    keyCol = ["AB", "CD", "EF", "GH", "IJ", "KL", "MN", "OP", "QR", "ST", "UV", "WX", "YZ"]
    for pl, letter in enumerate(text):              # these lines carry out the encryption process
        for pl2, keySet in enumerate(keyCol):
            if key[pl] in keySet: place = pl2
        textBuild = textBuild + matrix[place][alphabet.index(letter)]
    return textBuild
