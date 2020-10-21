import itertools
import random
text = "bad bed fab cab hede ece"
texte = "def dhf ced ged ahfh hgh"
count = 0
textev = texte.split(" ")
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # all letters being used

for x in itertools.permutations(my_list):
    count += 1
    build = ""
    for word in textev:
        for letter in word: build = build + my_list[x.index(letter)]
        build = build + " "
    build = build[:-1]
    if build == text: input("fougin found it!!  " + build + "\nyou did that in " + str(count) + " itterations\n and the letters were: " + x)
    print(build)
