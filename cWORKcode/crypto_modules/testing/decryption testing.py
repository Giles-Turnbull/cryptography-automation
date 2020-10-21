import itertools
text = "south match resolve mine slides visa shareware involvement sometimes stranger restricted consulting subscription applicant nikon"
texte = "uoghp vjhsp wkuoafk vtxk uatdku ftuj upjwkljwk txfoafkvkxh uovkhtvku uhwjxmkw wkuhwtshkd soxugahtxm ugiuswtehtox jeeatsjxh xtbox"
textev = texte.split(" ")
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for x in itertools.permutations(my_list):
    build = ""
    for word in textev:
        for letter in word: build = build + alpha[x.index(letter)]
        build = build + " "
    if build == text: print("fougin found it!!")
    print(build)
