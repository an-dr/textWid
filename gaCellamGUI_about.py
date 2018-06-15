from PyQt4 import QtGui, uic
from gaBasisGUI_resources import *  # модуль с ресурсами программы

aboutUI = resource_path(pathTofile + "about.ui")
sightPNG = resource_path(pathTofile + "sight.png")

form_about = uic.loadUiType(aboutUI)[0]  # Загрузка графики


class aboutWindows(QtGui.QWidget, form_about):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icon_main))  # задаем иконку
        self.label_pic.setPixmap(QtGui.QPixmap(sightPNG))

    def closeEvent(self, event):
        "Переопределяет closeEvent"
        event.ignore()
        print("hided")
        self.hide()

if __name__ == "__main__":  # запуск приложения
    app = QtGui.QApplication(sys.argv)
    aboutWindow = aboutWindows(None)  # создать окно
    aboutWindow.show()
    app.exec_()
