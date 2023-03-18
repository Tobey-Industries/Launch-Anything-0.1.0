print("Welcome! Let us set up my program, Launch Anything.")
import os
from cryptography.fernet import Fernet
def env(var):
  try:
    vari = os.environ[var]
    return vari
  except: print("I'm sorry, This operation done a wrong command and was stopped.")
os.system("color B0")
from playsound import playsound
playsound("bootsound.wav")
os.startfile("musicman.com")
print("Let's get introduced!")
print("I'm Tobey, what is your name?")
username = input("Your name is: ")
print("Hello, "+username)
def mkdir(dir): os.system('mkdir "' + dir + '"')
osutildir = env("APPDATA")+"\\..\\LocalLow\\osutil"
mkdir(osutildir + "\\" + username)
os.system('echo "">"'+osutildir+"\\"+username+"\\"+"sysUser.txt" + '"')
with open(osutildir+"\\sysUsers.txt","a")as f: f.write(" #"+username)
print("Look! My program needs security, so I need a password to keep things secure.")
password = input("Your Password: ")
os.system(f'echo "">"' + env('tmp')+'\\pass.txt"')
# Make the password a binary
# called password
key = 'your key'
encrypted_password = Fernet(key).encrypt(password)
os.system(f'echo "">"{osutildir}\\{username}\\pass.txt"')
with open(f'{osutildir}\\{username}\\pass.txt', "wb")as f: f.write(encrypted_password)
#
print("I Finished Setting Up Your System!")
print("To customize your system, type 'Customizer' in my program's interface.")
os.system("pause")
