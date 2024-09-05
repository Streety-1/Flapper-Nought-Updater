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

requiredmodules = {'requests'}

Flapper_File_Location = os.getcwd() + r"/Flapper" #drive\Flapper

BLUE = '\033[1;34;40m'
YELLOW = '\033[93m'
RED = '\033[91m'

#-------------------Prequisit Installer-------------------#

def systemCmd(command):
    os.system(command)

def pipinstall(package):
    systemCmd('sudo apt install python3-'+package)

try:
    import requests
    urllib.request.urlopen(urltocheckwifi)

    print(BLUE+'''
    ╔═══════════════════╗  
     
       Flapper Nought  
         
    ╚═══════════════════╝
    
    ''')

    #install modules
    print(YELLOW+"------------------modules")
    for x in requiredmodules:
        try:
            import x
            print("\033[2J\033[H", end="", flush=false)
        except ImportError:
            pipinstall(x)

    print(YELLOW+"------------------file structure")
    #Delete existing Flapper Folder
    systemCmd('sudo rm -rf '+Flapper_File_Location)

    print(YELLOW+"------------------getting repo")
    #Install new repo file
    systemCmd('git clone '+gitRepo)

    #Run main.py in new repo
    print(YELLOW+"------------------launching")
    time.sleep(3)
    exec(open(Flapper_File_Location + '/main.py').read())

except urllib.error.URLError:
    print(RED+"!!! Error: No wifi connection, cannot get latest version !!!")
    print(YELLOW + "------------------launching")
    time.sleep(3)
    exec(open(Flapper_File_Location + '/main.py').read())

