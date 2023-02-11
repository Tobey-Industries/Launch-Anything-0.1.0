print("Welcome! Let us set up my program, Launch Anything.")
import os
from cryptography.fernet import Fernet
def env(var):
  try:
    vari = os.environ[var]
    return vari
  except: print("I'm sorry, The command done an illegal operation and was shut down.")
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
# Password Method:
#   1. Encrypt the inputted password(password).
#   2. Send the encrypted password to the user's directory\\pass.txt . 
#   Important Note: The method here must be the same as the method in the main program.
#
# 
# 
# 
print("I Finished Setting Up Your System!")
print("To customize your system, type 'Customizer' in my program's interface.")
os.system("pause")
