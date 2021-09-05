from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout
from pyqt5_plugins.examplebutton import QtWidgets

import lzl.src.main as m
from zzr.src.Table_widget import Table_widget


class Search_area(QScrollArea):

    def __init__(self):
        self.central_widget = QWidget()
        self.setViewport(self.central_widget) #设置视口
        self.base_layout = QVBoxLayout()
        self.base_layout.setDirection(QVBoxLayout.TopToBottom)
        self.central_widget.setLayout(self.base_layout)

        self.set_tables()

    def set_tables(self):
        datas = m.giver.give_tables_info()
        for data in datas:
            self.base_layout.addWidget(Table_widget(data))

    def clear(self):
        while self.base_layout.count():
            child = self.base_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()