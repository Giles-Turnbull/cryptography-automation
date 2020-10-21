import random
import time
import os

def dataHandler(running, root, LoginFrame, start_running, username):
    path, pathx = os.getcwd().split("\\"), ""                       # these lines find the file and put the data into variable info
    for i in path: pathx = pathx + i + "\\"
    pathx = pathx + "\\GUIdata\\var_stop.txt"

    pathy, pathz = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the code
    pathy.pop()
    for i in pathy: pathz = pathz + i + "\\"
    patha = pathz + "\\gui\\userInfo\\"
    pathb = pathz + "\\crypto_modules\\data\\queue.txt"
    pathz = pathz + "\\crypto_modules\\data\\objects.txt"

    pathc, pathd = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the code
    pathc.pop()
    for i in pathc: pathd = pathd + i + "\\"
    pathe = pathd + "\\crypto_modules\\encryption\\encryption_code.py"
    pathDec = pathd + "\\crypto_modules\\decryption\\decryption_code.py"

    import importlib.util
    spec = importlib.util.spec_from_file_location("encryption_code", pathe)     # these lines open the module
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    spec2 = importlib.util.spec_from_file_location("decryption_code", pathDec)     # these lines open the module
    foo2 = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(foo2)

    def queue(patha, pathb, pathc, pathd, pathe, path, pathx, pathy, pathz):       
        file, users, objects, check = open(pathz, "r"), [], [], []  # these lines put all objects from objects.txt in a list
        for line in file:
            if "user: " in line: users.append(line[6:-1])
            if "object: " in line: objects.append(line[8:-1])
        file.close()
        for pl, person in enumerate(users):                         # these lines open the object file in the specific user folder
            tempPath = patha + person + "\\" + str(objects[pl]) + ".txt"
            check.append(tempPath)
        for pathCheck in check:                                     # these lines check if the object has been decrypted
            try:
                file, found = open(pathCheck, "r"), False
                for line in file:
                    if "decrypted: " in line:
                        if line[11:-1] == "no" or line[11:-1] == "in progress":
                            fileTwo = open(pathb, "r")
                            for line in fileTwo:
                                if pathCheck in line: found = True            # if the file hasnt been decrypted and is not in queue then it is added
                            fileTwo.close()
                            if found == False:
                                fileThree = open(pathb, "a")
                                fileThree.write(pathCheck + "\n")
                                fileThree.close()  
                file.close()
            except: print("that file could not be found!! ")
#=========================================================================================================================    
    while running == True:
        root.update()
        file = open(pathx, "r")                                         # these lines get the value of the text file
        for line in file:
            if "stop: " in line: value = line[6:-1]                 # these lines check if the program needs to be stopped
        file.close()
        if value == "True": running = False
        queue(patha, pathb, pathc, pathd, pathe, path, pathx, pathy, pathz)
#-----------------------------------------------------------------
        if os.path.getsize(pathb) <= 1000:
            foo.encrypt_module_run(username)
            print("aaaaa no")
            time.sleep(1)
#-----------------------------------------------------------------
        try:
            file, lines, objectValid = open(pathb, "r"), [], False                              # these lines find the first path in the queue
            validLine = file.readline()[:-1]
            file.close()
            file = open(validLine, "r")                                 # these lines open the object file
            for line in file: lines.append(line[:-1])
            file.close()

            if len(lines[0]) == 28:                                                 # this line checks the primary key
                if lines[9] != "decrypted: yes":                                    # this line checks if the object has already been decrypted
                    if lines[1][5:] != "" and lines[2][5:] != "":                   # this line checks the key and encryption key 
                        if len(lines[3][11:]) == 26:                                # this line checks the date and time are recorded
                            if len(lines[4][6:].split(" ")) == 500:                 # this line checks there are 500 words to be encrypted
                                if int(lines[5][14:]) < 10000:                      # this line checks the length of the text isnt too large
                                    if lines[6][16:] != "" and lines[7][17:] != "": # this line checks the encrypted text and type
                                        if float(lines[8][16:]) < 10000:            # this line checks the estimated time for encryption
                                            objectValid = True
            if objectValid == True:
                #--------------------------
                foo2.decryption_module_run(lines[5],running, root, LoginFrame, start_running, username, pathx, validLine)
                #--------------------------
            else: print("there must have been an error in the object") ### delete the object
        except: print("there must have been an error in the object or no objects in queue")##
    
