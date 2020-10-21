import random
import datetime
#======================================================================================= object structure
class Encrypt():
    def __init__(self,key,dateTime,lengs,text,tot_length,encrypted_text,enc_type):
        self.key = key
        self.time_made = dateTime
        self.lengs = lengs
        self.text = text
        self.tot_length = tot_length
        self.encrypted_text = encrypted_text
        self.encryption_type = enc_type

#======================================================================================= object structure
#----------------------------------------------
#======================================================================================= object filler

def create_key():
    key = ""
    for i in range(15): key = key + chr(random.randint(0, 25) + 97)
    return key
def create_text():
    words, text = [], ""
    file = open("word_list.txt", "r")
    for line in file: words.append(line[:-1])
    file.close()
    for i in range(15): text = text + words[random.randint(0, (len(words) - 1))] + " "
    text = text[:-1]
    return text
text = create_text()
def find_lengths(text):
    lengths_lst = text.split(" ")
    lengths_lst2 = []
    for i in lengths_lst: lengths_lst2.append(len(i))
    return lengths_lst2

#======================================================================================= object filler
#----------------------------------------------
#======================================================================================= encryption functions

def caesar_shift(text):
    encrypted_letter_list = []
    encrypted_text = ""
    alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(random.randint(0, 25)):
        first = alphabet2[0]
        del alphabet2[0]
        alphabet2.append(first)
    for letter in text:
        try: encrypted_letter_list.append(alphabet2[alphabet1.index(letter)])
        except: encrypted_letter_list.append(" ")
    for build in encrypted_letter_list: encrypted_text = encrypted_text + build
    return encrypted_text
def shuffle(text):
    encrypted_letter_list = []
    encrypted_text = ""
    alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random.shuffle(alphabet2)
    for letter in text:
        try: encrypted_letter_list.append(alphabet2[alphabet1.index(letter)])
        except: encrypted_letter_list.append(" ")
    for build in encrypted_letter_list: encrypted_text = encrypted_text + build
    return encrypted_text

#======================================================================================= encryption functions
#----------------------------------------------
#======================================================================================= defining vars

encryption_types = [caesar_shift(text), shuffle(text)]
encryption_types2 = [caesar_shift, shuffle]
place = random.randint(0, (len(encryption_types) - 1))
encrypted_text = encryption_types[place]
enc_type = encryption_types2[place].__name__
created_key = create_key()
tot_length = len(created_key)
dateTime = datetime.datetime.now()
lengths = find_lengths(text)

#======================================================================================= defining vars
#----------------------------------------------

globals()[created_key] = Encrypt(created_key, dateTime, lengths, text, tot_length, encrypted_text, enc_type)
#================
print("key: ", eval(created_key).key)
print("time made: ", eval(created_key).time_made)
print("lengths of words: ", eval(created_key).lengs)
print("total length: ", eval(created_key).tot_length)
print("text: ", eval(created_key).text)
print("encrypted text: ", eval(created_key).encrypted_text)
print("encryption type: ", eval(created_key).encryption_type)
#   key  time_made   lengs   text   tot_length   encrypted_text   encryption_type
#================

