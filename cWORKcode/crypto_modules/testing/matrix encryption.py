import random
def matrix_enc():
    text = "quantum oxide indians soma north survival dawn obj gr acknowledged railroad adaptor spots photographers computation"
    encrypted_text = ""
    alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = []
    
    for i in alphabet1: alphabet2.append(ord(i) - 96)
    for pl, i in enumerate(alphabet2): alphabet2[pl] = alphabet2[pl] * -1
    sent = text.split(" ")
    for word in sent:
        for letter in word:
            encrypted_text = encrypted_text + str(alphabet2[alphabet1.index(letter)])
        encrypted_text = encrypted_text + " "

    
    print(encrypted_text)
matrix_enc()
