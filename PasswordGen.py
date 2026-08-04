import random as rd

def passwordgen():
    Alphabet_Undercase = 'abcdefghijklmnopqrstuvwxyz'
    Alphabet_Uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    generic = "!@#$%^&*().><?/][{]}|\=+_-:;"
    letterX = Alphabet_Undercase
    letterY = Alphabet_Uppercase
    gen1 = (rd.randint(0,25))
    gen2 = (rd.randint(0,25))
    gen3 = (rd.randint(0,27))
    gen4 = (rd.randint(0,27))
    a = min(gen1,gen2)
    b = max(gen1,gen2)
    c = min(gen3,gen4)
    d = max(gen3,gen4)
    result1 = str(letterX[a:b]+letterY[a:b]+generic[c:d])
    result2 = str(letterX[a:b]+letterY[a:b]+generic[c:d])
    return result1[7:]+result2[:7]


