
import os, sys

appPath =  os.getcwdb().decode('utf-8');


config ={
    "thisAppPort": 999,
    "passKey": "liderdewally",
    "appPath": appPath,
    "templatesDir": appPath + "\\templates",
    "dataDir": appPath + "\\data",
    "tempDir": appPath + "\\temp",
    "phpDir" : appPath + "\\servers\\php-8.2.6-Win32-vs16-x64",
    "width" : 800,
    "length" : 800
    }

print(config["templatesDir"])