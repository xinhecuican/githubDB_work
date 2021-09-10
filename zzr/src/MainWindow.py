from PyQt5.QtCore import Qt, QLine
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QBrush
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QToolButton, QHBoxLayout, QWidget, QSplitter, QFrame

from zzr.src.Search_area import Search_area
import lzl.src.main as m
from zzr.src.Table_widget import Table_widget
from zzr.src.User_info.User_info_card import User_info_card


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.base_layout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.setObjectName("MainWindow")

        self.setStyleSheet(".MainWindow{border-image: url(../resources/images/back2.jpg)}")

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("请输入用户名、仓库名或表名")
        self.search_button = QToolButton(self)
        self.search_button.setIcon(QIcon("../resources/images/search.png"))
        self.search_button.clicked.connect(lambda: self.on_search_button_click())
        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_box, 1)
        self.search_layout.addWidget(self.search_button)
        self.base_layout.addLayout(self.search_layout)
        self.base_layout.addSpacing(10)
        self.main_area = Search_area(self)
        self.base_layout.addWidget(self.main_area)
        # datas = m.giver.give_tables_info()
        # self.base_layout.addWidget(Table_widget(datas[0]['name'], datas[0]['rows'], datas[0]['col_info']))
        self.centralWidget.setLayout(self.base_layout)
        self.resize(600, 400)

        self.table_name = []
        table_names = m.helper.run("show tables;")
        for table_name in table_names:
            self.table_name.append(table_name[0])

    def on_search_button_click(self):
        self.main_area.clear()
        name = self.search_box.text()
        if name == '':
            self.main_area.set_tables()
            return

        data = m.helper.run(f"select id from user_info where user_name = '{name}'")
        if data is not None:
            self.main_area.add_widget(User_info_card(m.giver.give_user_info(name)))

        if name in self.table_name:
            info = m.giver.give_table_info(name)
            self.main_area.add_widget(Table_widget(info['name'], info['rows'], info['col_info']))

        data = m.helper.run(f"select id from repository where name = '{name}'")
        if data is not None:
            print(1)
            # TODO: 先将仓库信息卡片完成


