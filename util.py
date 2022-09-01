#604 (3)
import os
import time
import socket
import platform as system
print(system, os.name)
print(time.strftime("%m-%d-20%y"))
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
print("Welcome to Launch Anything!")
os.system("title Launch Anything && color 10")
print("""

Options:

[1] Run Windows Files
[2] Run Python3 Files on Bash
[3] Run Python2 Files on Bash
[4] Run Python2 or Python3 Files on Windows New Technology
[9] Install PIP-Pyinstaller
[13] Run Command Prompt
[14] Set Color
[15] Set Color Code
[16] Set Title of the Running Windows Command Processor
[17] Run Notepad
[18] Run Windows Explorer
[19] Run Write
[20] Run WINVER
[21] Run REGEDIT
[22] Run Task Manager
[23] Kill any process
[24] Diagnose websites
[25] Go to websites
[26] Hack websites
[27] Clear Screen
""")
while True:
        opt = input("Option: ")  
        if opt == "27":
            os.system("cls")                
        if opt == "1":
                run = input("Run: ")
                os.startfile(run)
        if opt == "2":
                fillew = input("File: ")
                os.system("python3 " + filew)
        if opt == "3":
                filewa = input("File: ")
                os.system("python" + filewa)
        if opt == "4":
                filewan = input("File: ")
                os.system("python" + filewan)
        if opt == "9":
                os.system("pip install pyinstaller && color 10")
        if opt == "14":
                out = input("""
0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
                """)
                os.system("color " + out + "0")
        if opt == "24":
                ping = input("Website: ")
                os.system("ping " + ping)
        if opt == "25":
                import webbrowser
                web = input("Go to: ")
                webbrowser.open(web)
        if opt == "26":
                import requests
                print("""
                ██╗██████╗░░░░░░░██████╗░██╗██████╗░░█████╗░████████╗███████╗
                ██║██╔══██╗░░░░░░██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                ██║██████╔╝█████╗██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░
                ██║██╔═══╝░╚════╝██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
                ██║██║░░░░░░░░░░░██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗
                ╚═╝╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
                """)
                ip = input("Enter IP To Scan: ")
                url = f"https://ipinfo.io/{ip}?token=89eb984d917dd5"
                response = requests.get(url).json()

                print("IP:", response['ip'])
                print("\n")
                print("ADDRESS:")
                print("Country Code:", response['country'])
                print("Region Name:", response['region'])
                print("City:", response['city'])
                print("\n")
                print("POSTAL/TIMEZONE:")
                print("Postal Code:", response['postal'])
                print("Timezone:", response['timezone'])
                print("\n")
                print("LAT/LONG")
                print("Location:", response['loc'])
        if opt == "13":
                os.system("cmd")
        if opt == "16":
                tit = input("Title: ")
                os.system("title " + tit)
        if opt == "15":
                coc = input("Color: ")
                os.system("color " + coc)
        if opt == "17":
                os.startfile("Notepad")
        if opt == "18":
                os.startfile("explorer")
        if opt == "19":
                os.startfile("write")
        if opt == "20":
                os.startfile("winver")
        if opt == "21":
                os.startfile("REGEDIT")
        if opt == "22":
                os.startfile("taskmgr")
        if opt == "23":
                kill = input("Kill: ")
                os.system("taskkill /IM " + kill)
