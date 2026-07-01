import random

snippets = ["ar","an","am","at","er","en","em","et","ir","in","im","it","or","on","om","ot","ur","un","um","ut","aw","ew","iw","ow"]
consonants = ["c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","ch","cr","fr","br","cl","gl","dr"]

def fakeword():
    snippetcount = random.randint(2,5)
    dumbword = ""
    conschance = 0.7
    for x in range(snippetcount):
        if random.random() < conschance:
            dumbword += random.choice(consonants)
            if conschance > 0.1: conschance -= 0.1
        dumbword += random.choice(snippets)
    return dumbword

