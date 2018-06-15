# from gaArgumentum import *  # модуль с данными о программе
author = "grama"  # автор
programName = "textWid"  # название программы
version = "0.9.9.160410"  # версия программы
portableMode = False  # режим работы

if __name__ == '__main__':
    info = programName + '\nv.' + version + '\nby ' + author
    print(info)
    if portableMode is True:
        print('Working in a portable mode')
    input()
