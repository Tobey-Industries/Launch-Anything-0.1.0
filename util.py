print("Starting Log-in Manager...")
import os
usrprofile = os.environ['USERPROFILE']
from playsound import playsound
from cryptography.fernet import Fernet
import socket
import platform
import logging
import time
import psutil
def env(var):
  try:
    vari = os.environ[var]
    return vari
  except: print("The command done an illegal operation and was shut down.")
osutildir = env("APPDATA")+"\\..\\LocalLow\\osutil"
logfile = f"{osutildir}\\{socket.gethostname()}.txt"
logpl = logfile
batteryf = psutil.sensors_battery()
battery = batteryf.percent
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
date = time.strftime('%B-%d-%Y %I:%M %p')
userprofile = os.environ ['USERPROFILE']
osn = os.environ ['OS']
windir = os.environ ['WINDIR']
processor = os.environ['PROCESSOR_IDENTIFIER']
architecture = os.environ['PROCESSOR_ARCHITECTURE']
processors = os.environ['NUMBER_OF_PROCESSORS']
allsyspaths = os.environ['Path']
sysusrname = os.environ['USERNAME']
kernbuild = "UTIL Kernel 0.2.0(2023 Kernel)"
copyright = "Copyright(c) O. Republic 2023"
pythoncopyright = "Copyright(c) Python Software Foundation"
mscopyright = "Copyright(c) Microsoft Corporation 2006-2023"
ntfourlogonsoundcopyright = "Copyright(c) Microsoft Corporation"
print("Code Copyright: "+copyright)
print("Interpreter Copyright: "+pythoncopyright)
print("Main Operating System Copyright: "+mscopyright)
print("Default Success Sound Copyright: "+ntfourlogonsoundcopyright)
def do(): 
  time.sleep(float(0.40))
all_info = [sysusrname + "|" + date + "|" + hostName + '|' + hostIP + " " + userprofile + "|" + osn + "|" + windir + "|" + processor + "|" +  architecture + "|" + processors]
shellbuild = "Launch Anything 1.1.0(2023-February Shell)"
print("Initializing Definitions...")
help = """
Commands:
[1] Run Windows Files
[2] Run Python3 Files on Bash
[3] Run Python2 Files on Bash
[4] Run Python2 or Python3 Files on Windows New Technology
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
[31] Display all System Info
[32] Display all the current directory neatly
[33] Play a sound
[34] Log the system environment variables
[35] About Launch Anything 0.1.0-1.1.0
[36] About Utility Kernel 0.2.0-1.0.0
[Ctrl+Z] Exit Launch Anything
"""
def filecontents(filename):
  try:
    op = open(filename)
    return op.read()
  except: print("The command done an illegal operation and was shut down.")
def getsysinfo(currtell):
  try:
    user = os.environ["USERNAME"]
    tmpdir = os.environ["TMP"]
    homedrv = os.environ["HOMEDRIVE"]
    cpucores= os.environ["NUMBER_OF_PROCESSORS"]
    cpugen = os.environ["PROCESSOR_LEVEL"]
    root = os.environ["SystemRoot"]
    ops = platform.system()
    arc = os.environ["PROCESSOR_ARCHITECTURE"]
    info = f"""
A = Object       B = Meaning                                      C = Information from                                         
-------------  --------------------------------------------  ----------------
[A]HostName     = [B]{socket.gethostname()}                      = [C]Socket Library
[A]HostIP       = [B]{socket.gethostbyname(socket.gethostname())}= [C]Socket Library
[A]Operating
System          = [B]{ops}                                       = [C]{os.name}OSKRNL
[A]{ops}
User            = [B]{user}                                      = [C]{os.name}OSKRNL
[A]Kernel Build = [B]{build}                                     = [C]UTILITY Kernel
[A]OS Kernel    = [B]{os.name}                                   = [C]{os.name}OSKRNL
[A]Copyright    = [B]{copyright}                                 = [C]UTILITY Kernel
[A]Temporary Dir= [B]{tmpdir}                                    = [C]{os.name}OSKRNL
[A]HomeDrive    = [B]{homedrv}                                   = [C]{os.name}OSKRNL
[A]Root User's
Directory       = [B]{root}                                      = [C]{os.name}OSKRNL
[A]CPU Cores    = [B]{cpucores}                                  = [C]{os.name}OSKRNL
[A]CPU Gen      = [B]{cpugen}                                    = [C]{os.name}OSKRNL
[A]CPU 
Architecture    = [B]{arc}/AMD64(An Interpreting Flaw in 32-bit) = [C]{os.name}OSKRNL
-----------------------------------------------------------------------------
Caller: {currtell}
  """
    return info
  except: print("The command done an illegal operation and was shut down.")
def writeBINARY(bin, file):
  os.system(f'echo "">"{file}"')
  with open(file, "wb")as f: f.write(bin)
def writeASCII(cont, file):
  os.system(f'echo "">"{file}"')
  with open(file, "w")as f: f.write(cont)
primos = "nt"
print("Primary Operating System is set to New Technology...Done")
oscheck = True
print("System check is set to enabled...Done")
debugsys = True
print("Debugging is set to enabled...Done")
nocolor = False
print("Color is set to enabled...Done")
sysusersinfo = f"{osutildir}\\sysUsers.txt"  
print("Success.")
fsound = filecontents(osutildir + "\\bootsound.sys")
setsound = fsound
secsound = filecontents(osutildir + "\\secbootsound.sys")
try: playsound(setsound)
except: playsound(secsound)
logging.basicConfig(filename =logfile, level =logging.DEBUG)
tiny_info = [battery, osn, architecture, hostName]
unattended = False
try:
  usrs = filecontents(sysusersinfo)
  print("Users: " + usrs)
except: print("The returning value wasn't made.")
while True:
  current_user = input("Username: ")
  current_user_dir = osutildir+"\\"+current_user
  if current_user == "Guest":
    print("Welcome Guest!")
    break
  elif current_user == "guest":
    print("Welcome Guest!")
    break
  else:
    try:
      open(current_user_dir+"\\sysUser.txt")
      # Look! This section is the section for decrypting the password file (Launch Anything directory\\Username\\pass.txt).
      # Requirements for rebuilding this section:
      #   The inputted password must be called inps.
      #   The decrypted password must be called rpswd.
      #   The key (if there is a key) must be called key.
      #   
      #
      #
      if inps == rpswd:
        print(f"Welcome {current_user}!")
        logging.info( current_user_dir)
        key = "Access is denied."
        break
      else:
        print("Invalid Passcode!")
    except FileNotFoundError: print("Invalid User!")
    except TypeError: print("The command done an illegal operation and was shut down.")
    except UnicodeError: print("Numbers+Letters are the only elements supported.")
    except EOFError: print("CTRL+Z/CMD+X/CMD+Z are illegal operations.")
    except NameError: print("The command done an illegal operation and was shut down.")
print("Initialized Definitions...Done")
print("System is starting...")
os.system(f"title {kernbuild}:{shellbuild}")
try: 
  import time
  loc = open("config.util")
  fin = loc.read()
  if fin == "--no-sys-check":
    oscheck = False
    time.sleep(int(10))
  elif fin == "--primary-os-linux":
    primos = "posix"
    time.sleep(int(10))
  elif fin == "--fileopen":
    run = input("Run:")
    try: os.startfile(run)
    except FileNotFoundError:
      logging.basicConfig(filename =logpl,
                          level =logging.DEBUG)
      print("Invalid File")
      logging.error(f" FileNotFoundError at date: {date}. When opening: {run}. Using: StartRun")
      logp = open(logpl) 
    except OSError:
      print("Invalid File Content")
      logging.basicConfig(filename =logpl,
                          level =logging.DEBUG)
      print("Invalid Content")
      logging.error(f" OSError at date: {date}. When opening: {run}. Using: StartRun")
      logp = open(logpl)       
    time.sleep(int(10))
  elif fin == "--display-date":
    import time
    print(time.strftime("%m-%d-%y"))
    time.sleep(int(10))
  elif fin == "--no-color": nocolor = True
  elif fin == "--no-spec": debugsys = False  
  else: unattended = True  
  loc.close() 

except NameError:
  print("X")
except FileNotFoundError:
  print("X")
except TypeError: print("The command done an illegal operation and was shut down.")
except UnicodeError: print("Numbers+Letters are the only elements supported.")
except EOFError: print("CTRL+Z/CMD+X/CMD+Z are illegal operations.")
try: os.startfile("charms.exe")
except: os.startfile("charmswindow.pyw")
writeASCII(help, usrprofile + "\\AppData\\Roaming\\help.txt")
writeASCII(open(logpl).read(), usrprofile + "\\AppData\\Roaming\\dbginfo.txt")
if nocolor: os.system("color")
else: os.system("color B0")
if oscheck:
  if os.name == primos:
    print(f"*{primos}")
  else:
    import time
    print("Operating System Not Supported!")
    time.sleep(int(15))
    print("Exiting...")
    time.sleep(int(20))
    exit()
if debugsys:
  print(platform.system(), os.name)
  print(date)
  print(hostName)
  print(hostIP)
  print(battery)

print("System Started... Done")
logging.debug(" System Started Successfully at "+date)
os.system("ver")
print("""Options:
[1] Run Windows Files
[2] Run Python3 Files on Bash
[3] Run Python2 Files on Bash
[4] Run Python2 or Python3 Files on Windows New Technology
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
[31] Display all System Info
[32] Display all the current directory neatly
[33] Play a sound
[34] Log the system environment variables
[35] About Launch Anything 0.1.0-1.1.0
[36] About Utility Kernel 0.2.0-1.0.0
[Ctrl+Z] Exit Launch Anything
""")   
while True:
  try:
        if unattended:
            opt = open("config.util").read()
            unattended = False
        else: opt = input(f"{current_user}@{hostName}: ")
        logging.debug(f" {tiny_info} {date} {sysusrname} {current_user_dir} Ran option: {opt}")
        if opt == "27": os.system("cls")
        elif opt == "36": print("Utility Kernel 0.2.0-1.0.0\nCopyright (C) TE 2023")
        elif opt == "33":
          sound = input("File or Website: ")
          if sound[0] == '"' and sound[int(len(sound))-1] == '"': sound = sound[1:int(len(sound))-1]
          else: sound = sound
          playsound(sound)
        elif opt == "34": 
          inf = getsysinfo(current_user)
          logging.info(inf)
        elif opt == "35":
          import tkinter
          window = tkinter.Tk()
          tkinter.Label(window,text = "Copyight (C) Tobey Enterprises\nCopyright (C) Tobey Industries\n 2022-2023").pack()
          tkinter.Label(window,text="Shell Version: "+shellbuild).pack()
          tkinter.Label(window,text="Kernel Version: "+kernbuild).pack()
          tkinter.Button(window,text="OK", command = window.destroy).pack()
          window.title("About Launch Anything")
          window.geometry("400x400")
          window.mainloop()
        elif opt == "32": os.system("dir /w")  
        elif opt == "31": print(all_info)          
        elif opt == "1": 
                try:
                  run = input("Run: ")
                  os.startfile(run)
                except FileNotFoundError:
                  print("Invalid File!")
                except OSError:
                  print("Invalid win32 user mode executable!")
        elif opt == "print(tiny_info)": print(tiny_info)
        elif opt == "print(all_info)": print(all_info)
        elif opt == "print(osn)": print(osn)
        elif opt == "print(hostIP)": print(hostIP)
        elif opt == "do()": do()
        elif opt == "os": print(os)
        elif opt == "print(battery)": print(battery)
        elif opt == "winver": opt = "winver"
        elif opt == "29":
          import webbrowser
          webbrowser.open("youtube.com")
        elif opt == "30":
          import webbrowser
          webbrowser.open("bing.com")      
        elif opt == "28":
                dot = 0
                while dot < 9:
                  dot = dot + 1
                  os.system("cls")
                  os.system("color 00")
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
                  os.system("color B0")
        elif opt == "2":
                fillew = input("File: ")
                os.system("python3 " + filew)
        elif opt == "3":
                filewa = input("File: ")
                os.system("python" + filewa)
        elif opt == "4":
                filewan = input("File: ")
                os.system("python" + filewan)      
        elif opt == "9":
                os.system("pip install pyinstaller")
                os.system("color 10")
        elif opt == "14":
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
        elif opt == "24":
                ping = input("Website: ")
                os.system("ping " + ping)
        elif opt == "25":
                import webbrowser
                web = input("Go to: ")
                webbrowser.open(web)
        elif opt == "26":
                print("Please wait... D o  n o t  i n t e r r u p t !")
                os.system("pip install requests")
                os.system("color 10")
                print("""
                ██╗██████╗░░░░░░░██████╗░██╗██████╗░░█████╗░████████╗███████╗
                ██║██╔══██╗░░░░░░██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                ██║██████╔╝█████╗██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░
                ██║██╔═══╝░╚════╝██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
                ██║██║░░░░░░░░░░░██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗
                ╚═╝╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
                """)
                try:
                  import requests
                  ip = input("Enter IP To Scan: ")
                  url = f"https://ipinfo.io/{ip}?token=89eb984d917dd5"
                  response = requests.get(url).json
                  print("IP: " + ip)
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
                  logging.debug(f" IP: (ip) Location: {response['loc']} Country: {response['country']} Postal Code: {response['postal']}")
                except KeyError:
                  print("Invalid IP Address")
                  logging.error(f" KeyError (Invalid IP Address) Using IP-Pirate |{date} {hostIP} {userprofile} {current_user} {os.name}")                  
                except ImportError:
                  print("A dll or python pip file is corrupted!")
                  logging.error(f" ImportError Using IP-Pirate |{date} {hostIP} {userprofile} {current_user} {os.name}")
                except TypeError:
                  print("Python Build Is too old! or A .dll file is corrupted")
                  logging.error(all_info + " Old system data")
        elif opt == "13":
                os.system("cmd")
        elif opt == "16":
                tit = input("Title: ")
                os.system("title " + tit)
        elif opt == "15":
                coc = input("Color: ")
                os.system("color " + coc)
        elif opt == "17":
                filnam = input("New File: ")
                os.system(f"notepad {filnam}")
        elif opt == "18":
                os.system(f"explorer {current_user_dir}")
        elif opt == "19":
                os.startfile("write")
        elif opt == "20":
                os.startfile("winver")
        elif opt == "21":
                os.startfile("REGEDIT")
        elif opt == "22":
                os.startfile("taskmgr")
        else: os.system(opt)
  except EOFError:
    logging.debug(" Shutdown (expected)")
    print("Shutting Down...")
    os.system("del config.util")
    do()
    exit()
  except TypeError: print("An error occurred.(TypeError)")
  except NameError: print("An error occurred.(NameError)")
  except UnicodeError: print("An error occurred.(UnicodeError)")
  except PlaysoundException: print("An error occurred.(PlaysoundException)")
  except FileNotFoundError: print("An error occurred.(FileNotFoundError)")
  except OSError: print("An error occurred.(OSError)")
  except PermissionError: print("An error occurred.(PermissionError)")
