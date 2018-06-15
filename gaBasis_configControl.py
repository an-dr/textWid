# from gaBasis_configControl import *  # модуль с ресурсами программы
from gaArgumentum import *  # модуль с данными о программе
import os
import configparser

configFileName = programName + '-config.ini'  # путь до файла
configPsr = configparser.ConfigParser()  # для работы с файлом настроек


def pathForSettings():
    # global portableMode
    if portableMode is False:
        roamingPath = os.getenv('APPDATA')  # положение папки настроек, переносимых на другой компьютер
        roamingPath = os.path.abspath(roamingPath)  # приводим к универсальному виду
        programFolder = roamingPath + "\\gramaApps\\" + programName + "\\"
        if os.path.exists(programFolder) is False:
            os.makedirs(programFolder)
    else:
        programFolder = ""
    return programFolder
    # fistFilePath = roamingPath + "\\gramaApps\\hotEges\\firststart"  # предполагаемое положение файла
    # open(fistFilePath, 'w').close()
    # print("Создан файл первого запуска")


def getConfigFilePath():
    path = pathForSettings()
    configFilePath = path + configFileName
    return configFilePath


def initConfigFile(overwrite=False):
    "Если файл есть, то ничего не делает. Если нет - создает. overwrite - значит, нужно ли перезаписывать имеющийся"
    configFilePath = getConfigFilePath()
    try:
        with open(configFilePath, 'r') as configfile:
            # configfile.close()
            pass
    except:
        configPsr['main'] = {
            'first_start': '0'
        }
        # configPsr['Other'] = {
        #     'lastWindowX': '0',
        #     'lastWindowY': '0'
        # }
        with open(configFilePath, 'w') as configfile:
            configPsr.write(configfile)
            # configfile.close()
    if overwrite is True:
        configPsr['main'] = {
            'first_start': '0'
        }
        with open(configFilePath, 'w') as configfile:
            configPsr.write(configfile)


def read(section, variable):
    # global portableMode
    configFilePath = getConfigFilePath()
    configPsr.read(configFilePath)
    try:
        var = configPsr.get(section, variable)
    except:
        var = 'error'
    print(variable, '=', var)
    return var


def write(section, variable, value):
    # global portableMode
    configFilePath = getConfigFilePath()  # получаем расположение настроек
    configPsr.read(configFilePath)  # читаем настройки
    try:  # пытаемся добавить значение
        configPsr.set(section, variable, value)
    except:  # если не добавляется, создаем новую секцию и вновь пытаемся
        configPsr.add_section(section)
        configPsr.set(section, variable, value)
    with open(configFilePath, 'w') as configfile:  # записываем в файл
        configPsr.write(configfile)
        # configfile.close()


def main():
    initConfigFile(True)
    write('123', 'setting 4', 'C:\\Users\\Андрей\\AppData\\Roaming\\gramaApps\\gramaBlank')
    # write('Main', 'First start', '1', portableMode)
    # print(read('DEFAULT', 'setting 4', portableMode))
    # configPsr.read(configFileName)

if __name__ == '__main__':
    main()
