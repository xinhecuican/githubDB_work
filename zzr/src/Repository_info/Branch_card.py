from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QAction


class Branch_card(QAction):
    button_click = pyqtSignal(int, int)

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setText(self.data[1]['name'])

        self.triggered.connect(lambda: self.on_trigger())

    def on_trigger(self):
        self.button_click.emit(self.data[0], self.data[1]['latest_commit_id'])
