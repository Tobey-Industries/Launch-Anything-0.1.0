import os
if os.name == "nt":
  print("*nt")
else:
  import time
  print("Operating System Not Supported!")
  time.sleep(int(150))
  print("Exiting...")
  time.sleep(int(20))
  os.system("exit")
import time
import socket
import platform as system
date = time.strftime("%m-%d-20%y")
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
print(system, os.name)
print(date)
print(hostName)
print(hostIP)
print("Welcome to Launch Anything!")
os.system("title Launch Anything")
print("Please Wait...")
os.system("color 10 && @echo off && pip install psutil && color 10 && @echo off && pip install wolframalpha && color 10")

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
[28] Run Dreamco
[29] Go to youtube.com
[30] Go to bing.com
[31] Display IP & Device Name
[Ctrl+Z] Exit Launch Anything
""")
while True:
        opt = input("Option: ")  
        if opt == "27":
            os.system("cls")
            print("""

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
[27] Clear Screen
[28] Run Dreamco
[29] Go to youtube.com
[30] Go to bing.com
[31] Display IP & Device Name
[Ctrl+Z] Exit Launch Anything
            """)      
        if opt == "31":
          print(hostName + " " + hostIP)          
        if opt == "1":
                try:
                  run = input("Run: ")
                  os.startfile(run)
                except FileNotFoundError:
                  print("Invalid File!")
                except OSError:
                  print("Invalid win32 user mode executable!")
        if opt == "29":
          import webbrowser
          webbrowser.open("youtube.com")
        if opt == "30":
          import webbrowser
          webbrowser.open("bing.com")      
        if opt == "28":
                dot = 0
                while dot < 9:
                  dot = dot + 1
                  os.system("cls")
                  os.system("color 00")
                  def do(): 
                    time.sleep(float(0.40))
                  do()
                  os.system("color 10")
                  do()
                  os.system("color 20")
                  do()
                  os.system("color 30")
                  do()
                  os.system("color 40")
                  do()
                  os.system("color 50")
                  do()
                  os.system("color 60")
                  do()
                  os.system("color 70")
                  do()
                  os.system("color 80")
                  do()
                  os.system("color 90")
                  do()
                  os.system("color A0")
                  do()
                  os.system("color B0")
                  do()
                  os.system("color C0")
                  do()
                  os.system("color D0")
                  do()
                  os.system("color E0")
                  do()
                  os.system("color F0")
                  do()
                  os.system("color 03")
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
                os.system("pip install pyinstaller")
                os.system("color 10")
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
                print("Please wait... D o  n o t  i n t e r r u p t !")
                os.system("pip install requests")
                os.system("color 10")
                import requests
                print("""
                ██╗██████╗░░░░░░░██████╗░██╗██████╗░░█████╗░████████╗███████╗
                ██║██╔══██╗░░░░░░██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                ██║██████╔╝█████╗██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░
                ██║██╔═══╝░╚════╝██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
                ██║██║░░░░░░░░░░░██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗
                ╚═╝╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
                """)
                try:
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
                except KeyError:
                  print("Invalid IP Address")
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
        if opt != "23" or "22" or "21" or "20" or "24" or "25" or "26" or "27" or "19" or "18" or "17" or "16" or "15" or "14" or "13" or "12" or "11" or "10" or "9" or "8" or "7" or "6" or "5" or "4" or "3" or "2" or "1":
                os.system(opt)