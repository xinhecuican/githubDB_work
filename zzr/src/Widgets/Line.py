from PyQt5.QtWidgets import QFrame


class Line(QFrame):

    def __init__(self):
        super().__init__()
        self.setFrameShadow(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
