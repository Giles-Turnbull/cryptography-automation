def formatTextFunc(text):       # these lines format the text by removing all spaces and making letters capital
    textBuild = ""
    for letter in text:
        if letter.upper() != " ": textBuild = textBuild + letter.upper()
    return textBuild


def encrypt():
    text = formatTextFunc(text)
    stationary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    
