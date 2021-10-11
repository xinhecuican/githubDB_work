from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QLabel

"""
可以同时显示图片和文字的label
"""


class Pic_label(QLabel):

    def __init__(self, pic: QPixmap = None, text=""):
        super().__init__()
        self.pic = pic
        self.text = text
        self.pic_loc = QPoint(0, 0)
        self.text_loc = QPoint(0, 0)
        self.min_height = 0
        self.init_location()

    def init_location(self):
        if self.pic is not None:
            if self.pic.height() > self.fontMetrics().height():
                self.text_loc.setX(self.pic.width() + 10)
                self.text_loc.setY((self.pic.height() + self.fontMetrics().height()) / 2)
                self.min_height = self.pic.height()
            else:
                self.pic_loc.setY((self.fontMetrics().height() - self.pic.height()) / 2)
                self.text_loc.setX(self.pic.width() + 10)
                self.text_loc.setY((self.fontMetrics().height() + self.pic.height()) / 2)
                self.min_height = self.fontMetrics().height()

    def set_pic(self, pic):
        self.pic = pic
        self.init_location()
        self.update()
        self.setMinimumHeight(self.min_height)

    def set_text(self, text):
        self.text = text
        self.init_location()
        self.update()
        self.setMinimumHeight(self.min_height)

    def paintEvent(self, a0) -> None:
        painter = QPainter(self)
        if self.pic is not None:
            painter.drawPixmap(self.pic_loc, self.pic)
            painter.drawText(self.text_loc, self.text)
        else:
            painter.drawText(0, 10, self.text)
