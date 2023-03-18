import os
os.system("color B0 && Title Add-on")
print("Welcome To The Settings Editor For Launch Anything")
opt_one = input("[1]Delete Old Settings | [2]Make a New Setting: ")
confdir = "config.util"
def linux_mode():
  with open(confdir, "w")as f: f.writelines("--primary-os-linux")
def file_open():
  with open(confdir, "w")as f: f.writelines("--fileopen")
def no_sys_check():
  with open(confdir, "w")as f: f.writelines("--no-sys-check")
def display_date():
  with open(confdir, "w")as f: f.writelines("--display-date")
def no_color():
  with open(confdir, "w")as f: f.writelines("--no-color")
def no_spec():
  with open(confdir, "w")as f: f.writelines("--no-spec")
if opt_one == "1":
  os.system("del config.util")
  input("Press<ENTER>To Exit.")
if opt_one == "2":
  opt_two = input("""
[1]No System Check
[2]Linux Mode
[3]Open a File When Starting System
[4]Display The Date When Starting
[5]No Color
[6]No Showing Specs
  """)
  if opt_two == "1": no_sys_check()
  if opt_two == "2": linux_mode()
  if opt_two == "3": file_open()
  if opt_two == "4": display_date()
  if opt_two == "5": no_color()
  if opt_two == "6": no_spec()