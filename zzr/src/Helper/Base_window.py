import abc
from abc import ABCMeta

from PyQt5.QtWidgets import QMainWindow


class Base_window(QMainWindow):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def on_window_select(self, *args):
        pass

    @abc.abstractmethod
    def on_window_cancel(self, *args):
        pass
