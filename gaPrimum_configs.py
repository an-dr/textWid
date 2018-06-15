# import gaPrimum_configs as gaConfigs  # модуль с настройками
from gaArgumentum import *  # модуль с данными о программе
from gaBasis_configControl import *


def init():
    initConfigFile(False)  # создаем или проверяем наличие файл конфигурации
    # write('main', 'first_start', '1')  # совершен первый запуск
    # write('main', 'autostart', '0')  # автозагрузка

    if read('main', 'first_start') != '1':
        noteTextFilePath = pathForSettings() + 'textWid_note.txt'
        write('main', 'note_text_file', noteTextFilePath)  # автозагрузка
        write('main', 'autostart', '0')  # автозагрузка
        write('main', 'first_start', '1')  # совершен первый запуск


def main():
    init()
    read('main', 'autostart')

if __name__ == '__main__':
    main()
