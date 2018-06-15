# from gaPrimum_mainActions import *  # основные действия программы
from gaArgumentum import *  # модуль с данными о программе
import gaPrimum_configs as gaConfigs  # модуль с настройками
import logging
from ctypes import windll  # Для получения положения курсора


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def readOrCreateFile():
    "Читает, либо создает файл"

    # workpath = getWorkPath()
    text_file = gaConfigs.read('main', 'note_text_file')
    # logger.debug(text_file)
    try:
        f = open(text_file, 'r')
        text = f.read()
        f.close()
        return text
    except:
        f = open(text_file, 'w')
        text = ''
        f.close()
        return text
    # logger.debug(os.path.abspath(text_file))
    # print(os.path.abspath(f))


def writeToFile(textToWrite):
    text_file = gaConfigs.read('main', 'note_text_file')
    f = open(text_file, 'w')
    f.write(textToWrite)
    f.close()


def pressedMouseButton():
    "Проверяет, нажата ли одна из пяти кнопок мыши"
    mouseButton1 = windll.user32.GetAsyncKeyState(1)
    mouseButton2 = windll.user32.GetAsyncKeyState(2)
    mouseButton3 = windll.user32.GetAsyncKeyState(3)
    mouseButton4 = windll.user32.GetAsyncKeyState(4)
    mouseButton5 = windll.user32.GetAsyncKeyState(5)
    if mouseButton1 != 0 or mouseButton2 != 0 or mouseButton3 != 0 or mouseButton4 != 0 or mouseButton5 != 0:
        someButtonIsPressed = True
    else:
        someButtonIsPressed = False
    return someButtonIsPressed


def main():
    gaConfigs.init()
    readOrCreateFile()

if __name__ == '__main__':
    main()
    input()
