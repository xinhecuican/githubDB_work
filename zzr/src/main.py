import sys
from pyqt5_plugins.examplebutton import QtWidgets
from home import Ui_MainWindow as Home_Ui
from table import Ui_MainWindow as Table_Ui
from PyQt5.QtWidgets import QApplication, QMainWindow


class HomeUi(QtWidgets.QMainWindow, Home_Ui):
    def __init__(self):
        super(HomeUi, self).__init__()
        self.setupUi(self)

class TableUi(QtWidgets.QMainWindow, Table_Ui):
    def __init__(self):
        super(TableUi, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    h = HomeUi()
    h.show()
    t = TableUi()
    # button是你定义的按钮
    h.biaoge.clicked.connect(
        lambda: {h.close(), t.show()}
    )
    t.back.clicked.connect(
        lambda: {t.close(), h.show()}
    )
    sys.exit(app.exec_())
