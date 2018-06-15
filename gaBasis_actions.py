# from gaBasis_actions import *  # для удаления лишних файлов
from gaArgumentum import *  # модуль с данными о программе
import sys  # Для значка в трее
import os  # Для поиска пути до файла
import winreg  # работа с реестром


def removeQtConf():
    'Удаляет файл, который возникает при запуске Qt приложений'
    pathToFile, exeFile = os.path.split(os.path.abspath(sys.executable))
    pathToQtConf = pathToFile + "\qt.conf"
    # print(pathToFile)
    if os.path.isfile(pathToQtConf):
        os.remove(pathToQtConf)
        print("Файл qt.conf удален")
    else:
        print("Нет файла qt.conf")


def startupOff():
    "Удаляем программу из автозагрузки"
    aKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_ALL_ACCESS))  # Ключ реестра
    winreg.DeleteValue(aKey, programName)
    print(programName, "Removed from startup")


def startupOn():
    "Добавляет программу в автозагрузку. На вход, показывать или нет сообщения (True/False)"
    aKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_ALL_ACCESS))  # Ключ реестра
    try:
        # if os.path.dirname(__file__) == os.path.dirname(sys.executable):
        exeFilePath = sys.executable
        exeFileName = os.path.basename(exeFilePath)
        if exeFileName != "python.exe" and exeFileName != "pythonw.exe":
            hEpath = '"' + os.path.abspath(sys.executable) + '"'
            winreg.SetValueEx(aKey, programName, 0, winreg.REG_SZ, hEpath)
            #         print(sys.path)
            #         print(os.path.dirname(__file__))
            print("Добавлен в автозагрузку")
        else:
            hEpath = '"' + os.path.abspath(__file__) + '"'
            winreg.SetValueEx(aKey, programName, 0, winreg.REG_SZ, hEpath)
            print("Добавлен в автозагрузку скрипт")
    except:
        print("Не добавлено в автозагрузку")
