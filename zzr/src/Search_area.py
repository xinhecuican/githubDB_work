from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QFrame, QAbstractScrollArea, QLayout
from pyqt5_plugins.examplebutton import QtWidgets

import lzl.src.main as m
from zzr.src.Table_widget import Table_widget


class Search_area(QScrollArea):

    def __init__(self, parent: QWidget = None):
        super().__init__()
        self.central_widget = QWidget(parent)
        self.setFrameShape(QFrame.NoFrame)
        self.base_layout = QVBoxLayout()
        self.base_layout.setDirection(QVBoxLayout.TopToBottom)
        self.central_widget.setStyleSheet("background-color: transparent;")
        self.setStyleSheet("background-color: transparent;")
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.set_tables()
        self.central_widget.setLayout(self.base_layout)
        self.setWidget(self.central_widget)  # 设置视口
        self.setWidgetResizable(True)

    def set_tables(self):
        datas = m.giver.give_tables_info()
        for data in datas:
            self.base_layout.addWidget(Table_widget(data['name'], data['rows'], data['col_info']))

    def clear(self):
        while self.base_layout.count():
            child = self.base_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.update()

    def add_widget(self, widget: QWidget):
        self.base_layout.addWidget(widget)

    def add_layout(self, layout: QLayout):
        self.base_layout.addLayout(layout)
