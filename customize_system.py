
import os
os.system("color B0 && Title Add-on")
print("Welcome To The Settings Editor For Launch Anything")
opt_one = input("[1]Delete Old Settings | [2]Make a New Setting")
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
def update_sys_pass():
  with open(confdir, "w")as f: f.writelines("--update-sys-pass")
def update_sys_username():
  with open(confdir, "w")as f: f.writelines("update-sys-username")
if opt_one == "1":
  os.system("del config.util")
  input("Press<ENTER>To Exit.")

  