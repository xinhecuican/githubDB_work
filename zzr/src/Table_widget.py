from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QToolButton, QVBoxLayout, QLabel, QHBoxLayout, QTableView, \
    QHeaderView, QTableWidget, QTableWidgetItem, QCommandLinkButton

from zzr.src.Helper import Widget_style, Window_manager


class Table_widget(QWidget):

    def __init__(self, table_name, row_count, cols_info):
        super(Table_widget, self).__init__()
        self.name =  table_name
        self.cols_info = cols_info
        self.setMinimumSize(30, 30)
        self.base_layout = QVBoxLayout()
        self.base_layout.setDirection(QVBoxLayout.TopToBottom)

        self.setLayout(self.base_layout)
        self.setStyleSheet(Widget_style.commandlink_button_style)
        self.name_label = QCommandLinkButton()
        self.name_label.setText(table_name)
        self.name_label.clicked.connect(self.on_button_click)
        self.count_label = QLabel()
        self.count_label.setText("行数: " + str(row_count))

        self.label_layout = QHBoxLayout()
        self.label_layout.addWidget(self.name_label)
        self.label_layout.addWidget(self.count_label)
        self.base_layout.addLayout(self.label_layout)

        self.tableview = QTableWidget()
        self.tableview.setColumnCount(6)
        self.tableview.setFrameShape(QHeaderView.NoFrame)
        self.tableview.verticalHeader().setVisible(False)
        self.tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableview.setHorizontalHeaderLabels(['列名', '类型', '是否为空', '键值', '默认值', '自增'])
        self.tableview.setBackgroundRole(QPalette.Light)
        self.tableview.setShowGrid(False)
        for i in range(len(self.cols_info)):
            self.append_row(i)
        self.base_layout.addWidget(self.tableview)

        # 显示全部按钮
        # self.show_button = QPushButton()
        # self.show_state = False
        # self.hide_button.setIcon() 添加向下箭头，需要一张图片
        # self.show_button.clicked.connect(lambda: self.on_show_button_click())
        # self.base_layout.addWidget(self.show_button)
        self.adjustSize()

    def on_button_click(self):
        Window_manager.change_window("Table_panel", [self.name])

    def on_show_button_click(self):

        if self.show_state:
            self.tableview.setRowCount(1)  # 没试过，可能有问题，就是只显示一行
            # self.show_button.setIcon()更换图标
            self.show_state = False
        else:
            for i in range(1, len(self.cols_info)):
                self.append_row(i)
            # self.show_button.setIcon()
            self.show_state = True

    def append_row(self, index):
        data = self.cols_info[index]
        self.tableview.setRowCount(self.tableview.rowCount() + 1)
        col_name = QTableWidgetItem()
        col_name.setText(data['name'])
        self.tableview.setItem(index, 0, col_name)

        col_type = QTableWidgetItem()
        col_type.setText(data['type'])
        self.tableview.setItem(index, 1, col_type)

        col_null_enable = QTableWidgetItem()
        col_null_enable.setData(Qt.DisplayRole, data['null_enable'])
        self.tableview.setItem(index, 2, col_null_enable)

        col_key = QTableWidgetItem()
        col_key.setText(data['key'])
        self.tableview.setItem(index, 3, col_key)

        col_default = QTableWidgetItem()
        col_default.setData(Qt.DisplayRole, data['default'])
        self.tableview.setItem(index, 4, col_default)

        col_is_auto_increment = QTableWidgetItem()
        col_is_auto_increment.setData(Qt.DisplayRole, data['is_auto_increment'])
        self.tableview.setItem(index, 5, col_is_auto_increment)
