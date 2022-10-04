# The script that handles all open commands of gamma

import subprocess

# Application Paths
fusion360_path = "C:\\Users\\ACER\\AppData\\Local\\Autodesk\\webdeploy\\production\\6a0c9611291d45bb9226980209917c3d\\FusionLauncher.exe"
epicgames_path = "F:\\{}\\{}\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe".format('"Epic Games"','"Epic Games"')
arduinoIDE_path = "D:\\Arduino\\{}\\arduino.exe".format('"Arduino IDE"')
vscode_path = "F:\\{}\\Code.exe".format('"Microsoft VS Code"')
codingfolder_path = "C:\\Users\\ACER\\Desktop\\Coding"
collegefolder_path = "C:\\Users\\ACER\\Desktop\\College"


def process(name):
    if name == 'fusion 360':
        subprocess.run('start {}'.format(fusion360_path), shell=True)
    elif name == 'epic games':
        subprocess.run('start {}'.format(epicgames_path), shell=True)
    elif name == 'arduino':
        subprocess.run('start {}'.format(arduinoIDE_path), shell=True)
    elif name == 'code':
        subprocess.run('start {}'.format(vscode_path), shell=True)
    elif name == 'coding folder':
        subprocess.run('start {}'.format(codingfolder_path), shell=True)
    elif name == 'college folder':
        print('dfkd')
        subprocess.run('start {}'.format(collegefolder_path), shell=True)
