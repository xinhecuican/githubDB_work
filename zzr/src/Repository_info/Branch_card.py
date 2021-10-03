from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QAction


class Branch_card(QAction):
    button_click = pyqtSignal([int], [int], name="button_click")

    def __init__(self, data):
        super().__init__()
        self.data = data

        self.triggered.connect(lambda: self.on_trigger())

    def on_trigger(self):
        self.button_click.emit(self.data['id'], self.data['latest_commit_id'])
