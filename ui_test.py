import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

import Ui_main

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_main.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon('img/logo.ico'))
        MainWindow.setWindowTitle('穷人追梦：赌狗争霸')
        MainWindow.show()
        print('running...')
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
    