from textwrap import wrap
def formatTextFunc(text):       # these lines format the text by removing all spaces and making letters capital
    textBuild = ""
    for letter in text:
        if letter.upper() != " ": textBuild = textBuild + letter.upper()
    return textBuild

def formatKeyFunc(key):     # these lines format the key into a 3x3x3 matrix
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "#"]
    matrixOne, matrixTwo, matrixThree = [], [], []
    for letter in key:              # these lines format the key by removing spaces and making uppercase
        if letter.upper() not in matrixOne and letter != " ": matrixOne.append(letter.upper())
    for letter in matrixOne:        # these lines create the first 3x3 matrix
        place = alphabet.index(letter.upper())
        del alphabet[place]
    while len(matrixOne) < 9:
        matrixOne.append(alphabet[0])
        del alphabet[0]
    for i in range(3):  # these lines make the second 3x3 matrix
        matrixTwo.append([alphabet[0], alphabet[1], alphabet[2]])
        for x in range(3): del alphabet[0]
    for i in range(3):  # these lines make the third 3x3 matrix
        matrixThree.append([alphabet[0], alphabet[1], alphabet[2]])
        for x in range(3): del alphabet[0]
    matrixOne = [[matrixOne[0], matrixOne[1], matrixOne[2]], [matrixOne[3], matrixOne[4], matrixOne[5]], [matrixOne[6], matrixOne[7], matrixOne[8]]] # this lines formats the first 3x3 matrix
    return [matrixOne, matrixTwo, matrixThree]      # this line returns the 3x3x3 matrix


def encrypt(text, key):
    text = formatTextFunc(text)     # these lines format the text and the key
    key = formatKeyFunc(key)
    co, period, textBuild, textFinal = [], 5, "", ""
    for letter in text:         # these lines create a list of 3d coordinates for each letter
        for pl, table in enumerate(key):
            for pl2, keySet in enumerate(table):
                for pl3, coordinate in enumerate(keySet):
                    if letter == coordinate: co.append([pl, pl2, pl3])
    rowOne, rowTwo, rowThree = "", "", ""
    for coordinate in co:       # these lines manipulate the matrix to create new coordinates
        rowOne = rowOne + str(coordinate[0])
        rowTwo = rowTwo + str(coordinate[1])
        rowThree = rowThree + str(coordinate[2])
    rowOne = wrap(rowOne, period)
    rowTwo = wrap(rowTwo, period)
    rowThree = wrap(rowThree, period)
    new = ""
    for pl, keySet in enumerate(rowOne):
        for letter in keySet: new = new + letter
        for letter in rowTwo[pl]: new = new + letter
        for letter in rowThree[pl]: new = new + letter
    new = wrap(new, 3)
    for coordinate in new:          # these lines build the cipher text from the new coordinates
        textBuild = textBuild + key[int(coordinate[0])][int(coordinate[1])][int(coordinate[2])]
    textBuild = wrap(textBuild, period)         # these lines format the text returned
    for i in textBuild: textFinal = textFinal + i + " "
    return textFinal[:-1]


def decrypt(text, key):
    text = formatTextFunc(text)     # these lines format the text and the key
    key = formatKeyFunc(key)
    co, period, textBuild = "", 5, ""
    for letter in text:         # these lines create a list of 3d coordinates for each letter
        for pl, table in enumerate(key):
            for pl2, keySet in enumerate(table):
                for pl3, coordinate in enumerate(keySet):
                    if letter == coordinate: co = co + str(pl) + str(pl2) + str(pl3)
    def chunk_split(lst, size):  # these lines split a list up into "size" chunks
        for i in range(0, len(lst), size):  
            yield lst[i:i + size]
    co = list(chunk_split(co, 15))  # these lines manipulate the co-ordinates
    rowOne, rowTwo, rowThree = [], [], []
    for coSet in co:
        newCo = list(chunk_split(coSet, int(len(coSet) / 3)))
        rowOne.append(newCo[0])
        rowTwo.append(newCo[1])
        rowThree.append(newCo[2])
    finalCo = [rowOne, rowTwo, rowThree]
    for pl, word in enumerate(finalCo[0]):      # these lines find the new co-ordinates in the key
        for pl2, letter in enumerate(word):
            textBuild = textBuild + key[int(finalCo[0][pl][pl2])][int(finalCo[1][pl][pl2])][int(finalCo[2][pl][pl2])]
    return textBuild
