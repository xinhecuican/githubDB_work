from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton, QHBoxLayout, QAction

from zzr.src.Helper import Window_manager
from zzr.src.Widgets.Line import Line
from zzr.src.Widgets.Pic_label import Pic_label


class User_info_card(QWidget):

    def __init__(self, data):
        super().__init__()
        self.name = data['name']
        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

        self.label_star_num = QLabel('点赞数: ' + str(data['star_num']))
        self.label_follower_num = QLabel('跟随数: ' + str(data['follower_num']))
        self.label_following_num = QLabel('跟随者数: ' + str(data['following_num']))

        description = data['description']
        self.nick_name = QLabel(description['nick_name'])

        self.comment = QLabel(description['comments'])
        self.comment.setWordWrap(True)

        self.location = Pic_label(QPixmap("../resources/images/location.png"), description['location'])
        self.company = Pic_label(QPixmap("../resources/images/company.png"), description['company'])

        self.link = QLabel(description['link'])

        self.location_layout = QHBoxLayout()
        success = False
        if description['company'] != '':
            success = True
            self.location_layout.addWidget(self.company)
        if description['location'] != '':
            success = True
            self.location_layout.addWidget(self.location)

        self.button_name = QToolButton()
        if description['nick_name'] != '':
            self.button_name.setText(description['nick_name'] + "   " + self.name)
        else:
            self.button_name.setText(self.name)
        self.button_name.clicked.connect(lambda: self.on_name_button_click())

        self.description_layout = QVBoxLayout()
        self.description_layout.addWidget(self.button_name)
        self.description_layout.addWidget(self.comment)
        if success:
            self.description_layout.addLayout(self.location_layout)

        self.avatar = QLabel()
        pix = QPixmap("../resources/images/avatar.png")
        pix = pix.scaled(100, 100, Qt.KeepAspectRatio)
        self.avatar.setPixmap(pix)

        if description['status'] != '':
            self.base_layout.addWidget(QLabel("状态: " + description['status']))
            self.base_layout.addWidget(Line())

        self.center_layout = QHBoxLayout()
        self.center_layout.addWidget(self.avatar, 2)
        self.center_layout.addLayout(self.description_layout, 5)
        self.base_layout.addLayout(self.center_layout)

    def on_name_button_click(self):
        Window_manager.change_window("User_info_panel", [self.name])
