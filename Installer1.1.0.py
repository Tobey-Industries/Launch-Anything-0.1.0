import os
import socket
print("Copyright (C) Tobey Industries 2023")
from playsound import playsound
try: playsound("Dependencies\\bootsound.wav")
except: playsound("bootsound.wav")
os.system("color B0")
def env(var):
  try:
    vari = os.environ[var]
    return vari
  except: print("The command done an illegal operation and was shut down.")
def copy(fro, to):
  try: os.system(f'copy /b "{fro}" "{to}"')
  except: print("The command done an illegal operation and was shut down.")
try: 
  dir = input("Directory to install in(Do not type your system drive or the Windows directory!): ")
  usr = env("USERPROFILE")
  osutildir = env("APPDATA")+"\\..\\LocalLow\\osutil"
  os.system('mkdir "'+osutildir+'"')
  os.system(f'echo "">"'+osutildir+"\\"+socket.gethostname()+".txt"+'"')
  os.system(f'echo "">"'+osutildir+"\\sysUsers.txt"+'"')
  with open(osutildir+"\\" + socket.gethostname()+".txt","w")as f: f.write("")
  with open(osutildir+"\\sysUsers.txt","w")as f: f.write("#Guest")
  copy("Dependencies\\bootsound.wav" ,f"{osutildir}\\bootsound.wav")
  os.system('echo "" > "'+osutildir+"\\bootsound.sys"+'"')
  os.system('echo "" > "'+osutildir+"\\secbootsound.sys"+'"')
  copy("Dependencies\\RTM.exe", f"{dir}\\RTM LA.exe")
  copy("Dependencies\\charmswindow.exe", f'{dir}\\charms.exe')
  copy("Dependencies\\customize_system.exe", dir + "\\Customizer.exe")
  os.system(f'mkdir "{usr}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\TobeyIndustries"')
  with open (f"{usr}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\TobeyIndustries\\Launch Anything.bat", "w")as f: f.write(f'cd "{dir}"\n"{dir}\\RTM LA.exe"')
  with open (f"{usr}\\Desktop\\Launch Anything.bat", "w")as f: f.write(f'"{dir}\\RTM LA.exe"')
  with open(osutildir + "\\bootsound.sys","w")as f: f.write("https://www.winhistory.de/more/winstart/mp3/nt4.mp3") 
  with open(osutildir + "\\secbootsound.sys","w") as f: f.write(f"{osutildir}\\bootsound.wav")
  print("Finished! \n Running the Out-Of-Box-Experience...")
  os.chdir("Dependencies")
  os.startfile("OOBERTM.exe")
except: print("The command done an illegal operation and was shut down.")
