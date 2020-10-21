from textwrap import wrap
def formatKeyFunc(key):
    matrix, formatKey, mainKey = [], [], []
    #=================================================================
    for i in range(5):      #these lines create a 5x5 matrix
        matrix.append([])
        for x in range(5): matrix[i].append(0)
    #=================================================================
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k',  'l',  'm', 'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']
    for letter in key:                          # these lines create put the key in a list
        if letter.upper() != "J": formatKey.append(letter.upper())
        else: formatKey.append("I")
    #=================================================================
    for letter in alphabet:                     # these lines fill the rest of the list with the alphabet
        if letter.upper() not in formatKey: formatKey.append(letter.upper())
    #=================================================================
    for letter in formatKey:                    # deletes repetitions
        if letter not in mainKey: mainKey.append(letter)
    #=================================================================
    county, countx = 0, -1          # these lines populate the matrix with the list
    for letter in mainKey:
        countx += 1
        matrix[county][countx] = letter
        if countx == 4: county += 1
        if countx == 4: countx = -1
    return matrix




def formatTextFunc(text):
    textBuild, textFormatSpaces, textFormatText = "", [], ""
    #=================================================================
    for letter in text:         # these lines put the text into upper and removes all spaces 
        if letter != " " and letter.upper() != "J":
            textFormatSpaces.append(letter.upper())
        elif letter.upper() == "J":
            textFormatSpaces.append("I")
    for letter in textFormatSpaces: textFormatText = textFormatText + letter 
    #=================================================================
    for pl, letter in enumerate(textFormatText):            # these lines add an X between double letters
        if pl != (len(textFormatText) - 1):
            if letter == textFormatText[pl + 1]: textBuild = textBuild + letter + "X"
            else: textBuild = textBuild + letter
        else: textBuild = textBuild + letter
    #=================================================================
    if (len(textBuild) % 2) == 1: textBuild = textBuild + "X"    # this line adds and x to the end if the text has off letters
    from textwrap import wrap
    text = wrap(textBuild, 2)
    return text


def encrypt(text, key):
    matrix = formatKeyFunc(key)
    text = formatTextFunc(text)
    result = ""
    def findIndex(letter, matrix): # find the location in the matrix of each character
        for ply, y in enumerate(matrix):
            for plx, x in enumerate(y):
                if letter == x:
                    return [ply, plx]
    for letterSet in text:      # these lines go through the sets of letters
        coOne = findIndex(letterSet[0], matrix)         # these lines find the co-ordinates of each letter
        coTwo = findIndex(letterSet[1], matrix)
        if coOne[0] == coTwo[0]:                        # these lines encrypt the pair if the x co-ordinates are the same
            if coOne[1] >= 4: yOne = -1
            else: yOne = coOne[1]
            if coTwo[1] >= 4: yTwo = -1
            else: yTwo = coTwo[1]
            result = result + (matrix[coOne[0]][yOne + 1])
            result = result + (matrix[coTwo[0]][yTwo + 1])
        elif coOne[1] == coTwo[1]:                      # these lines encrypt the pair if the y co-ordinates are the same
            if coOne[0] >= 4: yOne = -1
            else: yOne = coOne[0]
            if coTwo[0] >= 4: yTwo = -1
            else: yTwo = coTwo[0]
            result = result + (matrix[yOne + 1][coOne[1]])
            result = result + (matrix[yTwo + 1][coTwo[1]])
        else:                                           # these lines encrypt the rest by swapping the y co-ordinates of the pairs
            result = result + (matrix[coOne[0]][coTwo[1]])
            result = result + (matrix[coTwo[0]][coOne[1]])
    result, toReturn = wrap(result, 2), ""
    for i in result: toReturn = toReturn + i + " "
    return toReturn[:-1]


def decrypt(text, key):
    matrix = formatKeyFunc(key)
    text = formatTextFunc(text)
    result = ""
    def findIndex(letter, matrix): # find the location in the matrix of each character
        for ply, y in enumerate(matrix):
            for plx, x in enumerate(y):
                if letter == x:
                    return [ply, plx]
    for letterSet in text:      # these lines go through the sets of letters
        coOne = findIndex(letterSet[0], matrix)         # these lines find the co-ordinates of each letter
        coTwo = findIndex(letterSet[1], matrix)
        if coOne[0] == coTwo[0]:                        # these lines decrypt the pair if the x co-ordinates are the same
            if coOne[1] <= 0: yOne = 5
            else: yOne = coOne[1]
            if coTwo[1] <= 0: yTwo = 5
            else: yTwo = coTwo[1]

            result = result + (matrix[coOne[0]][yOne - 1])
            result = result + (matrix[coTwo[0]][yTwo - 1])
        elif coOne[1] == coTwo[1]:                      # these lines decrypt the pair if the y co-ordinates are the same
            if coOne[0] <= 0: yOne = 5
            else: yOne = coOne[0]
            if coTwo[0] <= 0: yTwo = 5
            else: yTwo = coTwo[0]

            result = result + (matrix[yOne - 1][coOne[1]])
            result = result + (matrix[yTwo - 1][coTwo[1]])
        else:                                           # these lines decrypt the rest by swapping the y co-ordinates of the pairs
            result = result + (matrix[coOne[0]][coTwo[1]])
            result = result + (matrix[coTwo[0]][coOne[1]])
    result, toReturn = wrap(result, 2), ""
    for i in result: toReturn = toReturn + i + " "
    return toReturn[:-1]

