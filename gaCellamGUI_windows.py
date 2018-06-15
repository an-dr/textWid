# from gaCellamGUI_windows import *
from PyQt4 import QtGui, uic
from gaBasisGUI_resources import *  # модуль с ресурсами программы

mainUI = resource_path(pathTofile + "main.ui")
form_class = uic.loadUiType(mainUI)[0]  # Загрузка графики из ui


class windows(QtGui.QWidget, form_class):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)  # создать объект приложения
    mainWindow = windows(None)  # создать окно
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
