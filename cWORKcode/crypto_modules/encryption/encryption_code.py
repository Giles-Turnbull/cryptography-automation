import random
import datetime
import os

def encrypt_module_run(username):
    class Encrypt():
        def __init__(self,PrimaryKey,key,decryptionKey,dateTime,text,tot_length,encrypted_text,enc_type, ET):   # these lines create an object with attributes
            self.PrimaryKey = PrimaryKey
            self.key = key
            self.decryptionKey = decryptionKey
    #--------------------------------------------
            self.time_made = dateTime
            self.text = text
            self.tot_length = tot_length
    #--------------------------------------------
            self.encrypted_text = encrypted_text
            self.encryption_type = enc_type
    #--------------------------------------------
            self.estimated_time = ET
    #=========================================================================================================================    
    def create_Primary_Key():               # these lines create a random primary key
        PrimaryKey = ""
        for i in range(15): PrimaryKey = PrimaryKey + chr(random.randint(0, 25) + 97)
        return PrimaryKey
    def create_key():                       # these lines create a random encryption key
        PrimaryKey = ""
        for i in range(6): PrimaryKey = PrimaryKey + chr(random.randint(0, 25) + 97)
        return PrimaryKey

    def create_text():
        words, text = [], ""

        pathy, pathz = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the code######################
        pathy.pop()
        for i in pathy: pathz = pathz + i + "\\"
        patha = pathz + "\\gui\\userInfo\\"
        pathb = pathz + "\\crypto_modules\\data\\word_list.txt"                         ####### add later "\\crypto_modules"

        file = open(pathb, "r")
        for line in file: words.append(line[:-1])                       # these lines put together the text
        file.close()
        for i in range(500): text = text + words[random.randint(0, (len(words) - 1))] + " "
        text = text[:-1]
        return text

    def EstimatedTime():                        # this module estimates the time taken to decrypt the object
        current_efficiency = 1                  # this is just for testing purposes and will be gathered from data later
        EsVar = 26*25*24*23*22*21
        EsVar = EsVar * current_efficiency
        EsVar = EsVar / 180000000              # this calculates the ammount of seconds it will take to complete the task
        return EsVar
    #=========================================================================================================================
    PrimaryKey = create_Primary_Key()           # these lines store the result of earlier functions
    key = create_key()
    decryptionKey = "example"                   # this is just a filler so the code can be tested
    dateTime = datetime.datetime.now()
    text = create_text()
    tot_length = len(text)
    encrypted_text = "example"                  # this is just a filler so the code can be tested
    enc_type = "example"                        # this is just a filler so the code can be tested
    ET = EstimatedTime()
    #=========================================================================================================================
    globals()[PrimaryKey] = Encrypt(PrimaryKey,key,decryptionKey,dateTime,text,tot_length,encrypted_text,enc_type, ET)      # this line passes the attributes to the class to create an object

    path, pathx = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the data
    path.pop()
    for i in path: pathx = pathx + i + "\\"
    pathy = pathx + "\\gui\\userInfo\\" + username + "\\" + PrimaryKey + ".txt"
    file = open(pathy, "w")
    file.write("primary key: " + eval(PrimaryKey).PrimaryKey + "\n")        # these lines write the info of the object to a text file
    file.write("key: " + eval(PrimaryKey).key + "\n")
    file.write("decryption key: " + eval(PrimaryKey).decryptionKey + "\n")
    file.write("time made: " + str(eval(PrimaryKey).time_made) + "\n")
    file.write("text: " + eval(PrimaryKey).text + "\n")
    file.write("total length: " + str(eval(PrimaryKey).tot_length) + "\n")
    file.write("encrypted text: " + eval(PrimaryKey).encrypted_text + "\n")
    file.write("encryption type: " + eval(PrimaryKey).encryption_type + "\n")
    file.write("Estimated time: " + str(eval(PrimaryKey).estimated_time) + "\n")
    file.write("decrypted: no\n")
    file.write("current Key Progress: aaaaaa")
    file.close()
    #=========================================================================================================================
    pathy, pathz = os.getcwd().split("\\"), ""                       # these lines find the path to the file containing the code
    pathy.pop()
    for i in pathy: pathz = pathz + i + "\\"
    pathz = pathz + "\\crypto_modules\\data\\objects.txt"
    file = open(pathz, "a")
    file.write("user: " + username + "\n" + "object: " + PrimaryKey + "\n")
    file.close()
    #=========================================================================================================================
    #print("primary key: ", eval(PrimaryKey).PrimaryKey)     # these lines are to see the output of the object
    #print("key: ", eval(PrimaryKey).key)

    #print("time made: ", eval(PrimaryKey).time_made)
    #print("total length: ", eval(PrimaryKey).tot_length)
    #print("text: ", eval(PrimaryKey).text)

    #print("encrypted text: ", eval(PrimaryKey).encrypted_text)
    #print("encryption type: ", eval(PrimaryKey).encryption_type)
    #print("Estimated time: ", eval(PrimaryKey).estimated_time)
