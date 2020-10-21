def decryption_module_run(encrypted_text,running, root, LoginFrame, start_running, username, pathx, validLine):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  'l',  'm', 'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']
    pointerOne = -1
    pointerTwo = -1
    pointerThree = -1
    pointerFour = -1
    pointerFive = -1
    pointerSix = -1
    guessKey =["a", "a", "a", "a", "a", "a"]

    def fileChanges(validLine, genKey):
        file, toWrite = open(validLine, "r"), []             # these lines change the attributes in the object file
        for line in file:
            if "current Key Progress" in line: toWrite.append("current Key Progress: " + genKey + "\n")
            elif "decrypted: " in line: toWrite.append("decrypted: in progress\n")
            else: toWrite.append(line)
        file.close()
        file = open(validLine, "w")             # these lines write the changes to the file
        for line in toWrite: file.write(line)
        file.close()
        

    for a in range(26):                             # these lines create the key
        pointerSix +=1
        for b in range(26):
            pointerFive += 1
            for c in range(26):
                pointerFour +=1
                for d in range(26):
                    pointerThree +=1
                    for e in range(26):
                        pointerTwo +=1
                        for a in range(26):
                            genKey = ""
                            #------------------------------------------
                            root.update()           # this line updates the GUI
                            file = open(pathx, "r")                                         # these lines get the value of the text file
                            for line in file:
                                if "stop: " in line: value = line[6:-1]                 # these lines check if the program needs to be stopped
                            file.close()
                            if value == "True":
                                break
                            #------------------------------------------
                            pointerOne +=1          # these lines create the key in a list
                            guessKey[0], guessKey[1], guessKey[2], guessKey[3], guessKey[4], guessKey[5] = alphabet[pointerOne], alphabet[pointerTwo], alphabet[pointerThree], alphabet[pointerFour], alphabet[pointerFive], alphabet[pointerSix]
                            for letter in guessKey: genKey = genKey + letter        # this line creates the key
                            print(guessKey)
                            #------------------------------------------
                            fileChanges(validLine, genKey)      # this line makes the changes to the text file
                            #------------------------------------------
                        pointerOne = -1             # these lines reset the value of the pointers back to 0 and break if return is pressed
                        if value == "True": break
                    pointerTwo = -1
                    if value == "True": break
                pointerThree = -1
                if value == "True": break
            pointerFour = -1
            if value == "True": break
        pointerFive = -1
        if value == "True": break
        
                        
    
