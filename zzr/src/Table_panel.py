from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QTableWidget, QTableWidgetItem

from zzr.src.Helper import Window_manager
from zzr.src.Helper.Base_window import Base_window
import lzl.src.main as m
from zzr.src.Helper.Register import Registers


@Registers.model.register
class Table_panel(Base_window):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.base_layout = QVBoxLayout()
        self.name_label = QLabel(self.name)
        self.base_layout.addWidget(self.name_label)
        self.table = QTableWidget()
        self.base_layout.addWidget(self.table)
        self.central_widget.setLayout(self.base_layout)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)

    def on_window_select(self, *args):
        self.name = args[0][0]
        self.name_label.setText(self.name)
        datas = m.giver.give_table(self.name)
        self.table.clear()
        self.table.setColumnCount(len(datas[0]))
        row = 0
        for data in datas:
            col = 0
            self.table.insertRow(row)
            for item in data:
                widget = QTableWidgetItem()
                widget.setText(item)
                self.table.setItem(row, col, widget)
                col = col + 1
            row = row + 1

    def on_window_cancel(self, *args):
        pass

    def closeEvent(self, a0: QCloseEvent):
        Window_manager.change_window("MainWindow")
        a0.accept()
