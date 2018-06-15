# from gaBasis_resources import *  # модуль с ресурсами программы
import sys
import os

pathTofile = "resources\\"


def resource_path(relative_path):
    "Get absolute path to resource, works for dev and for PyInstaller"
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASSicon_tray.png
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

icon_main = resource_path(pathTofile + "icon_main.png")
