from gaArgumentum import *  # модуль с данными о программе
from gaCellamGUI_trayIcon import *  # модуль с ресурсами программы


class ga_tray_icon(ga_cellam_tray_icons):

    def __init__(self, icon, parent=None):
        "На вход нужно - приложение(для управления), иконка"
        ga_cellam_tray_icons.__init__(self, icon_tray_png, parent)  # инициализация
# ----------------- пользовательский код
        self.setToolTip(programName + "\na grama App")  # всплывающая подсказка
# ----------------- пользовательский код


if __name__ == "__main__":  # запуск приложения
    app = QtGui.QApplication(sys.argv)
    iconTray = ga_tray_icon(icon_tray_png)  # создать иконку в трее
    app.exec_()
    # sys.exit(app.exec_())
