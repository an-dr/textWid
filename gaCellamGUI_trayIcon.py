import sys
from gaBasisGUI_resources import *  # модуль с ресурсами программы
from PyQt4 import QtGui, QtCore

icon_tray_png = resource_path(pathTofile + "icon_tray.png")


class ga_cellam_tray_icons(QtGui.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        "На вход нужно - приложение(для управления), иконка"
        qIcon = QtGui.QIcon(icon)  # иконка
        QtGui.QSystemTrayIcon.__init__(self, qIcon, parent)  # инициализация родителя
        self.qApp = QtCore.QCoreApplication.instance()  # - это доступ к главному экземляру приложения Qt
        self.trayMenu = QtGui.QMenu(parent)  # создать объект контекстного меню
        self.setContextMenu(self.trayMenu)  # привязать контекстное меню к иконке в трее
        self.setToolTip("a grama App")  # всплывающая подсказка
        # Настройка меню:
        self.exitAction = self.trayMenu.addAction("Exit")  # добавить в контекстное меню
        self.exitAction.triggered.connect(self.closeApp)  # СИГНАЛ - нажатие на строку выхода
        # пуск:
        self.show()  # отобразить иконку

    def closeApp(self):
        print("Closing...")
        self.qApp.exit()  # выход


if __name__ == "__main__":  # запуск приложения
    app = QtGui.QApplication(sys.argv)
    iconTray = ga_cellam_tray_icons(icon_tray_png)  # создать иконку в трее
    app.exec_()
    # sys.exit(app.exec_())
