# Download Latest version from github repo
# https://github.com/Streety-1/Flapper-Nought.git

#run updater to launch script 

import os
import subprocess
import sys
import urllib.request
import time
import shutil

gitRepo = 'https://github.com/Streety-1/Flapper.git'

urltocheckwifi = "https://www.google.com/ "

requiredmodules = {'requests','simple-term-menu'}

Flapper_File_Location = os.getcwd() + r"/Flapper" #drive\Flapper

#-------------------Prequisit Installer-------------------#

def systemCmd(command):
    os.system(command)

def pipinstall(package):
    #subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL)
    systemCmd('sudo apt install python3-'+package+'--quiet')

try:
    import requests
    urllib.request.urlopen(urltocheckwifi)

    print('''
    ╔═════════════════════════════════════════════╗  
     
      Getting stuff ready....   
         
    ╚═════════════════════════════════════════════╝
    
    ''')

    #install modules
    print("------------------modules")
    for x in requiredmodules:
        try:
            import x
            print("\033[2J\033[H", end="", flush=false)
        except ImportError:
            pipinstall(x)

    print("------------------dbus")
    systemCmd('sudo apt install python-dbus')

    print("------------------git")
    systemCmd('sudo apt install git')

    print("------------------updating file structure")
    #Delete existing Flapper Folder
    systemCmd('sudo rm -rf '+Flapper_File_Location)

    print("------------------getting repo")
    #Install new repo file
    systemCmd('git clone '+gitRepo)

    #Run main.py in new repo
    print("------------------launching")
    time.sleep(5)
    exec(open(Flapper_File_Location + '/main.py').read())

except urllib.error.URLError:
    print("!!! Error: No wifi connection, cannot get latest version !!!")
    print("         launching")
    time.sleep(3)
    exec(open(Flapper_File_Location + '/main.py').read())

