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
        if self.pic is not None:
            if self.pic.height() > self.fontMetrics().height():
                print(self.pic.height(), self.fontMetrics().height())
                self.text_loc.setX(self.pic.width() + 10)
                self.text_loc.setY((self.pic.height() + self.fontMetrics().height()) / 2)
                print(self.text_loc.y())
            else:
                self.pic_loc.setY((self.fontMetrics().height() - self.pic.height()) / 2)
                self.text_loc.setX(self.pic.width() + 10)
                self.text_loc.setY((self.fontMetrics().height() + self.pic.height()) / 2)

    def paintEvent(self, a0) -> None:
        painter = QPainter(self)
        if self.pic is not None:
            painter.drawPixmap(self.pic_loc, self.pic)
            painter.drawText(self.text_loc, self.text)
        else:
            painter.drawText(0, 10, self.text)
