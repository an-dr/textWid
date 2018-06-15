from gaCellamGUI_mainWindow import *
from gaPrimum_mainActions import *  # основные действия программы


class mainWindow(mainWindows):

    def __init__(self, parent=None):
        mainWindows.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow)  # удаляем рамки | скрываем отображение в таскбаре
        self.plainTextEdit.textChanged.connect(self.writeAllow)
        self.actionTimeout = 5000  # время перед началом записи-чтения
        self.write = False  # разрешение записи
        self.timer_read_write = QtCore.QTimer(parent=None)  # устанавливаем таймер обновления
        self.timer_read_write.timeout.connect(self.read_write)  # СИГНАЛ - переполнение таймера обновления
        # действия:
        self.plainTextEdit.setPlainText(readOrCreateFile())
        self.timer_read_write.start(self.actionTimeout)  # запуск таймера обновления

    def mousePressEvent(self, event):
        'Переопределение события нажатия мыши'
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        'Переопределение события движения мыши'
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

    def writeAllow(self):
        self.timer_read_write.stop  # стоп таймера обновления
        self.write = True  # разрешить запись
        self.timer_read_write.start(self.actionTimeout)  # запуск таймера обновления

    def read_write(self):
        if self.write is True:
            writeToFile(self.plainTextEdit.toPlainText())  # запись в файл из plainTextEdit
            self.write = False  # после завершения записи, запретить ее
        else:
            if pressedMouseButton() is False:  # если не нажата какая-то кнопка мыши
                # обработка старого курсора:
                oldCursor = self.plainTextEdit.textCursor()  # полчаем старый курсор
                startPos = oldCursor.selectionStart()  # начало выделения
                endPos = oldCursor.selectionEnd()  # конец выделения
                # чтение:
                self.plainTextEdit.setPlainText(readOrCreateFile())  # читаем
                # обработка нового курсора:
                newCursor = self.plainTextEdit.textCursor()  # берем новый курсор
                newCursor.setPosition(startPos)  # устанавливаем стартовую позицию
                newCursor.setPosition(endPos, QtGui.QTextCursor.KeepAnchor)  # устанавливаем конечную позицию
                self.plainTextEdit.setTextCursor(newCursor)  # применяем новый курсор
                # конец
                logger.debug('Прочитано')
            else:  # если какая-то кнопка мыши нажата
                pass  # ничего неделаем
                logger.debug('Отмена - нажата кнопка мыши')


def main():
    app = QtGui.QApplication(sys.argv)  # создать объект приложения
    main_window = mainWindow(None)  # создать окно
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
