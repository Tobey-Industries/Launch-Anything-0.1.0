import os
import time
import socket
os.system("title Launch Anything")
os.system("color 10")
print("""
Welcome to Launch Anything!

Options:

[1] Run Windows Files
[2] Run Python3 Files on Bash
[3] Run Python2 Files on Bash
[4] Run Python2 or Python3 Files on Windows New Technology
[5] Run SccuzMan on Bash or Windows New Technology(With low quality)
[6] Run SccuzMan on Windows New Technology(With high quality)
[7] Run AirMonitor on Windows New Technology
[8] Run Windows Subsystem for Linux
[9] Install PIP-Pyinstaller
[10] Install PIP-Python3 on Bash
[11] Run Pyinstaller
[12] Update PIP
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
""")
while True:
        opt = input("Option: ")
        with open("log", "w")as f:
                osdevice = socket.gethostname()
                ip = socket.gethostbyname(osdevice)
                filedata = open("log")
                usable = filedata.read()
                f.writelines(usable + "\n" + "Date: " + time.strftime("%m/%d/%y") + " OS: " + os.name + " " + "Device: " + osdevice + " IP: " + ip)
                filedata = open("log")
                usable = filedata.read()                  
        if opt == "1":
                run = input("Run: ")
                os.startfile(run)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                	usable = filedata.read()
        if opt == "2":
                fillew = input("File: ")
                os.system("python3 " + filew)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
					filedata = open("log")
					usable = filedata.read()
        if opt == "3":
                filewa = input("File: ")
                os.system("python" + filewa)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "4":
                filewan = input("File: ")
                os.system("python" + filewan)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
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
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "24":
                ping = input("Website: ")
                os.system("ping " + ping)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "25":
                import webbrowser
                web = input("Go to: ")
                webbrowser.web()
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
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
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "13":
                os.system("cmd")
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "16":
                tit = input("Title: ")
                os.system("title " + tit)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "15":
                coc = input("Color: ")
                os.system("color " + coc)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "17":
                os.startfile("Notepad")
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "18":
                os.startfile("explorer")
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "19":
                os.startfile("write")
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "20":
                os.startfile("winver")
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "21":
                os.startfile("REGEDIT")
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "22":
                os.startfile("taskmgr")
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
        if opt == "23":
                kill = input("Kill: ")
                os.system("taskkill /IM " + kill)
                with open("log", "w")as f:
                	f.writelines(usable + "\n" + opt + "\n")
                	filedata = open("log")
                    usable = filedata.read()
                
