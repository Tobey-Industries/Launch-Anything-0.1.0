try:
  print("Copyright (C) Tobey Industries 2023")
  import os
  usr = os.environ ['USERPROFILE']
  dir = input("Directory to install in(Do not type your system drive or the Windows directory!): ")
  def copy(fro, to):
  	os.system(f'copy /b "{fro}" "{to}"')
  copy("Dependencies\\RTM.exe", f'"{dir}\\RTM LA.exe"')
  copy("Dependencies\\customize_system.exe", dir + "\\Customizer.exe")
  os.system(f'mkdir "{usr}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\TobeyIndustries"')
  with open (f"{usr}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\TobeyIndustries\\Launch Anything.bat", "w")as f: f.write(f'"{dir}\\RTM LA.exe"')
  with open (f"{usr}\\Desktop\\Launch Anything.bat", "w")as f: f.write(f'"{dir}\\RTM LA.exe"')
  print("Finished! \n Running the Out-Of-Box-Experience...")
  os.startfile("Dependencies\\OOBERTM.exe")
except:
  input("ERROR! Press <ENTER> to exit.")
