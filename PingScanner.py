import subprocess as sp
import time
import sys
from concurrent.futures import ThreadPoolExecutor

def ping(a, b, x, y):
    ip = [str(a), str(b), str(x), str(y)]
    result = ".".join(ip)
    sp.run(["ping", "-c", "1", result])

def scan(a, b, x, target):
    with ThreadPoolExecutor(max_workers=target) as executor:
        for y in range(target):
            executor.submit(ping, a, b, x, y)


print(""" 
░█████████  ░██████░███    ░██   ░██████       ░██████     ░██████     ░███    ░███    ░██ ░███    ░██ ░██████████ ░█████████  
░██     ░██   ░██  ░████   ░██  ░██   ░██     ░██   ░██   ░██   ░██   ░██░██   ░████   ░██ ░████   ░██ ░██         ░██     ░██ 
░██     ░██   ░██  ░██░██  ░██ ░██           ░██         ░██         ░██  ░██  ░██░██  ░██ ░██░██  ░██ ░██         ░██     ░██ 
░█████████    ░██  ░██ ░██ ░██ ░██  █████     ░████████  ░██        ░█████████ ░██ ░██ ░██ ░██ ░██ ░██ ░█████████  ░█████████  
░██           ░██  ░██  ░██░██ ░██     ██            ░██ ░██        ░██    ░██ ░██  ░██░██ ░██  ░██░██ ░██         ░██   ░██   
░██           ░██  ░██   ░████  ░██  ░███     ░██   ░██   ░██   ░██ ░██    ░██ ░██   ░████ ░██   ░████ ░██         ░██    ░██  
░██         ░██████░██    ░███   ░█████░█      ░██████     ░██████  ░██    ░██ ░██    ░███ ░██    ░███ ░██████████ ░██     ░██ 
                                                                                                                               

#   Version         : 1.0.0
#   Project-rep     : https://github.com/farefare-ya/PythonLab       
#   Author          : farefare-ya
__________________________________________________________________________________________

    Select from 1 - 3 :
|
|   1. scan ip range
|   2. exit
|
""")

answer = input("$input : ")
if answer.isdigit():
    answer = int(answer)
    if answer == 1:
        a = input("oktet 1 : ")
        b = input("oktet 2 : ")
        x = input("oktet 3 : ")
        y = input("oktet 4 (up to): ")
        scan(a,b,x,int(y))
    elif answer == 2:
        sys.exit()
    else:
        print("huh")
else:
    print("Input should be number")