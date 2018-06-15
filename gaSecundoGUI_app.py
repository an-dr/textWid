import sys
from PyQt4 import QtGui
from gaArgumentum import *  # модуль с данными о программе
from gaBasis_actions import *  # для удаления лишних файлов
import gaPrimum_configs as config
from gaPrimumGUI_trayIcon import *
from gaPrimumGUI_mainWindow import *
from gaCellamGUI_about import *


class ga_app(QtGui.QApplication):

    def __init__(self, args):
        QtGui.QApplication.__init__(self, args)  # инициализация предка
# ----------------- пользовательский код (инициализация) ----------------------------------------------
        # > настройки:
        removeQtConf()  # удалить qt.conf
        config.init()

        # > главное окно:
        self.mainWindow = mainWindow(None)  # создать окно
        self.setWindowPosition()
        self.mainWindow.show()

        # > окно "О приложении":
        self.aboutWindow = aboutWindows(None)
        self.aboutWindow.setWindowTitle(programName + " " + version)  # меняем заголовок
        # lastAct = self.mainTrayIcon.trayMenu.actions()[0]  # получаем последний элемент из списка трей-меню
        # self.mainTrayIcon.aboutAction = QtGui.QAction('About', self)  # создаем элемент меню
        # aboutAct = self.mainTrayIcon.aboutAction  # называем - для удобства
        # aboutAct.triggered.connect(self.aboutWindow.show)  # СИГНАЛ - нажатие на строку о программе
        # self.mainTrayIcon.trayMenu.insertAction(lastAct, aboutAct)  # добавляем элемент меню

        # > иконка в трее:
        self.mainTrayIcon = ga_tray_icon(icon_tray_png)  # создать иконку в трее
        self.mainTrayIcon.activated.connect(self.trayActivated)  # СИГНАЛ - щелчок на иконке трея
        # контекстное меню
        self.newTrayMenu = QtGui.QMenu()  # создать объект контекстного меню
        self.mainTrayIcon.setContextMenu(self.newTrayMenu)  # привязать контекстное меню к иконке в трее
        # элемент меню About
        aboutAction = QtGui.QAction('About', self)  # создаем элемент меню
        aboutAction.triggered.connect(self.aboutWindow.show)  # СИГНАЛ - нажатие на строку о программе
        self.newTrayMenu.addAction(aboutAction)  # добавить в контекстное меню
        # элемент меню Exit
        exitAction = QtGui.QAction('Exit', self)  # создаем элемент меню
        exitAction.triggered.connect(self.closeApp)  # СИГНАЛ - нажатие на строку выхода
        self.newTrayMenu.addAction(exitAction)  # добавить в контекстное меню

        # > сообщение в конце инициализации:
        print(' > Загружено приложение:', programName, '\n',
              '  Версия:', version, '\n',
              '  Автор:', author)

# ----------------- пользовательский код (функции) ---------------------------------------------------

    def setWindowPosition(self):
        'Пытается считать положение окна из файла настроек.'
        try:
            x = int(config.read('stuff', 'x_pos'))
            y = int(config.read('stuff', 'y_pos'))
            self.mainWindow.move(x, y)
        except:
            pass

    def trayActivated(self, reason):
        "Показ приложения при нажатии на трей"
        if reason == 3:  # если нажата левая кнопка мыши
            # self.listView.clearSelection()  # очистить выделение в listView
            if self.mainWindow.isVisible() is True:
                # if self.mainWindow.isActiveWindow() is True:
                self.mainWindow.hide()  # скрыть окно
                # else:
                # self.mainWindow.activateWindow()  # сделать его активным
            else:
                self.mainWindow.show()  # показать окно
                self.mainWindow.activateWindow()  # сделать его активным

    def closeApp(self):
        p = self.mainWindow.pos()
        # x = p.x()
        # y = p.y()
        # print('x = ', x)
        # print('y = ', y)
        print("Closing...")
        config.write('stuff', 'y_pos', str(p.y()))
        config.write('stuff', 'x_pos', str(p.x()))
        qApp = QtCore.QCoreApplication.instance()  # - это доступ к главному экземляру приложения Qt
        qApp.exit()
# ----------------- пользовательский код (конец) -----------------------------------------------------


if __name__ == '__main__':
    app = ga_app(sys.argv)
    app.exec_()
