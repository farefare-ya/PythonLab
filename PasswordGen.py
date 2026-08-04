import random as rd
import sys

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
    result1 = str(letterX[a:b:1]+letterY[a:b:2]+generic[c:d:3]+letterX[a:b]+letterY[a:b]+generic[c:d])
    result2 = str(letterX[a:b:3]+letterY[a:b:1]+generic[c:d:2]+letterX[a:b:3]+letterY[a:b:2]+generic[c:d:1])
    return result1[1:]+result2[:1]


while True:
    print(""" 
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                      
#  Version        : 1.1
#  Project-rep    : https://github.com/farefare-ya/PythonLab
#  Author         : farefare-ya
    
______________________________________________________________

   Select from 1 - 3 :
|
|   1. Generate Single Password
|   2. Generate Multiple Password
|   3. exit
|

    
""")
    answer = int(input("$input : "))
    if answer == 1:
        print(passwordgen())
        print()
        input("press ENTER to continue...")
    elif answer == 2:
        key = int(input("How much... : "))
        i=1
        while i<=key:
            print(i,passwordgen())
            i=i+1
        print()
        input("press ENTER to continue...")
    elif answer == 3:
        sys.exit()
    else:
        print("Argument should be number between 1-3")

