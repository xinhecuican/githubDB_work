from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QPushButton, QToolButton, QVBoxLayout, QLabel, QHBoxLayout, QTableView, \
    QHeaderView, QTableWidget, QTableWidgetItem, QCommandLinkButton


class Table_widget(QWidget):

    def __init__(self, table_name, row_count, cols_info):
        super(Table_widget, self).__init__()
        self.cols_info = cols_info
        self.setMinimumSize(30, 30)
        self.base_layout = QVBoxLayout()
        self.base_layout.setDirection(QVBoxLayout.TopToBottom)

        self.setLayout(self.base_layout)
        self.setStyleSheet('''
        QCommandLinkButton:hover{
            background-color: rgba(98, 230, 230, 0.2);
        }
        QCommandLinkButton:pressed{
            background-color: rgba(255, 255, 255, 0.3);
        }
        QHeaderView::section, QTableCornerButton::section 
        {
            padding: 1px;border: none;
            border-bottom: 1px solid rgb(75, 120, 154);
            border-right: 1px solid rgb(75, 120, 154);
            border-bottom: 1px solid gray;
            background-color:rgba(75, 120, 154, 1);}


        QHeaderView::section
        {
            font-size:14px;
            font-family:"Microsoft YaHei";
            background-color: transparent;
            border:none;
            text-align:left;
            margin-left:0px;
            padding-left:0px;
        }
        QTableWidget::item
        {
            border-bottom:1px solid #EEF1F7 ;
        }
        QTableWidget::item::selected
        {
            color:red;
            background: rgba(74, 218, 218, 0.2);
        }
        ''')
        self.name_label = QCommandLinkButton()
        self.name_label.setText(table_name)
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
