import os
import sys
from PySide2 import QtWidgets, QtGui


class SystemTray(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Download Manager')
        menu = QtWidgets.QMenu(parent)
        close_app = menu.addAction("Encerrar Download Manager")
        close_app.triggered.connect(self.close_application)
        menu.addSeparator()
        self.setContextMenu(menu)

    def close_application(self):
        os.system("TASKKILL /F /IM download_cleaner.exe")
        sys.exit()


def start():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTray(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('Download Manager', 'Criado por: Everton Silva')
    app.exec_()


start()
