from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QCommandLinkButton, QLabel, QVBoxLayout, QHBoxLayout

from zzr.src.Helper import Widget_style, Window_manager
from zzr.src.Widgets.Pic_label import Pic_label


class Repository_info_card(QWidget):

    def __init__(self, data):
        super().__init__()
        self.setStyleSheet(Widget_style.commandlink_button_style)
        self.name = QCommandLinkButton()
        self.name.setText(data['name'])
        self.name.clicked.connect(lambda: self.on_button_click())

        self.author = QLabel()
        self.author.setText("作者: " + data['author'])

        self.base_layout = QVBoxLayout()
        self.base_layout.setDirection(QVBoxLayout.TopToBottom)

        self.description_layout = QHBoxLayout()
        self.description_layout.addWidget(self.name)
        self.description_layout.addWidget(self.author)
        self.base_layout.addLayout(self.description_layout)
        self.base_layout.addSpacing(10)
        # self.description = QLabel()
        # self.description.setText(data['description']['description'])
        # self.base_layout.addWidget(self.description)
        self.base_layout.addSpacing(10)

        self.star_num = Pic_label(pic=QPixmap("../resources/images/star.png"), text=str(data['star_num']))
        self.fork_num = Pic_label(pic=QPixmap("../resources/images/fork.png"), text=str(data['fork_num']))
        pix = QPixmap("../resources/images/friend.png")
        pix = pix.scaled(24, 24)
        self.contributor_num = Pic_label(pix, str(data['contributor_num']))
        self.contributor_num.setMinimumHeight(pix.height())
        self.sum_layout = QHBoxLayout()
        self.sum_layout.addWidget(self.star_num)
        self.sum_layout.addWidget(self.fork_num)
        self.sum_layout.addWidget(self.contributor_num)

        self.base_layout.addLayout(self.sum_layout)
        self.setLayout(self.base_layout)

    def on_button_click(self):
        Window_manager.change_window("Repository_panel", [self.name.text()])



