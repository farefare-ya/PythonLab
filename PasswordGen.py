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
    result1 = str(letterX[a:b]+letterY[a:b]+generic[c:d])
    result2 = str(letterX[a:b]+letterY[a:b]+generic[c:d])
    return result1[7:]+result2[:7]


while True:
    print(""" 
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                      
#  Version        : 1.0
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
    answer = int(input("$input :"))
    if answer == 1:
        print(passwordgen())
    elif answer == 2:
        print(passwordgen())
    elif answer == 3:
        sys.exit()
    else:
        print("Argument should be number between 1-3")

