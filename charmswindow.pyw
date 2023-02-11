import tkinter as tk
import os
usrprofile = os.environ['USERPROFILE']
window = tk.Tk()
def dbg():
  op = open(usrprofile + "\\AppData\\Roaming\\dbginfo.txt")
  re = op.read()
  info = tk.Label(window, text=re)
  info.pack()
def help():
  op = open(usrprofile + "\\AppData\\Roaming\\help.txt")
  re = op.read()
  info = tk.Label(window, text=re)
  info.pack()
def dvinf():
  import socket
  hostName = socket.gethostname()
  hostIP = socket.gethostbyname(hostName)
  re = hostName + " " + hostIP
  info = tk.Label(window, text=re)
  info.pack()  
def about():
  info = tk.Label(window, text="Copyright (C) O.Republic/Tobey Industries|2023 V. 0.1.0/1.0.1")
  info.pack()
def abtwin():
  os.startfile("WINVER.EXE")
scrollbar = tk.Scrollbar(window)
scrollbar.pack( side = tk.RIGHT,  fill = tk.Y)
window.title("Charms Window")
copyright = tk.Label(window, text = "[Copyright (C) O. Republic/Tobey Industries]")
copyright.pack()
dbgin = tk.Button(command=dbg,text="Debug Info",fg= "green",width=25)
dbgin.pack()
hlp = tk.Button(command=help,text="Help",fg= "green",width=25)
hlp.pack()
dvin = tk.Button(command=dvinf,text="Device Info", fg= "green",width=25)
dvin.pack()
abt = tk.Button(command=about, text="About Charms Window",fg = "blue",width=25)
abt.pack()
abtw = tk.Button(command=abtwin, text="About Microsoft Windows New Technology",fg = "blue",width=50)
abtw.pack()
sl = tk.Label(window, text = "---------------------------------------")
sl.pack()

window.mainloop()