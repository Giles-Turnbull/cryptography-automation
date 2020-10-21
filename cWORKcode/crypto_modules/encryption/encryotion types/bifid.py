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
    results, textBuild = [], ""
    for letter in text:
        if letter.upper() != " " and letter.upper != "J":
            if letter.upper() != "J": results.append(letter.upper())
            else: results.append("I")
    for letter in results: textBuild = textBuild + letter
    if (len(textBuild) % 2) == 1: textBuild = textBuild + "X"    # this line adds and x to the end if the text has off letters
    return textBuild



def encrypt(text, key):
    matrix = formatKeyFunc(key)
    text = formatTextFunc(text)
    period = 5
    numbers, resultBuild = [], ""
    first, second, pairs, final = [], [], "", ""
    def findIndex(letter, matrix): # find the location in the matrix of each character
        for ply, y in enumerate(matrix):
            for plx, x in enumerate(y):
                if letter == x:
                    return [ply, plx]
    for letter in text: numbers.append(findIndex(letter, matrix))   # these lines collate the indexes
    for i in numbers:
        first.append(i[0])
        second.append(i[1])
    for i in first: pairs = pairs + str(i)
    for i in second: pairs = pairs + str(i)
    pairs = wrap(pairs, 2) 
    for co in pairs: resultBuild = resultBuild + matrix[int(co[0])][int(co[1])]     # these lines find the letter assigned to the new indexes
    resultBuild  = wrap(resultBuild, period)
    for i in resultBuild: final = final + i + " "           # these lines create the final string with desired period
    return final[:-1]




def decrypt(text, key):
    matrix = formatKeyFunc(key)
    text = formatTextFunc(text)
    places, final, textBuild = [], [], ""
    def findIndex(letter, matrix): # find the location in the matrix of each character
        for ply, y in enumerate(matrix):
            for plx, x in enumerate(y):
                if letter == x:
                    return [ply, plx]
    for letter in text: places.append(findIndex(letter, matrix))
    split = len(places)//2          # these lines split the list of indexes in two
    first = places[:split]
    second = places[split:]
    for pl, co in enumerate(first):
        final.append([co[0], second[pl][0]])
        final.append([co[1], second[pl][1]])
    for build in final: textBuild = textBuild + matrix[build[0]][build[1]]
    return textBuild


