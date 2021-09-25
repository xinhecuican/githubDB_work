import datetime
from abc import ABC

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QLayout, QGridLayout, \
    QScrollArea, QLayoutItem, QFrame
import lzl.src.main as m
from zzr.src.Helper.Base_window import Base_window
from zzr.src.Helper.Register import Registers
from zzr.src.Repository_info.Repository_info_card import Repository_info_card
from zzr.src.User_info.User_activity_card import User_activity_card
from zzr.src.Widgets.Line import Line
from zzr.src.Widgets.Pic_label import Pic_label


@Registers.model.register
class User_info_panel(Base_window):

    def __init__(self, name):
        super().__init__()
        self.activity_layout = QVBoxLayout()
        self.repository_card_layout = QGridLayout()
        self.repository_label_layout = QHBoxLayout()
        self.repository_label_layout.addWidget(QLabel("热门仓库: "), 2)
        self.repository_label_layout.addWidget(Line(), 8)
        self.repository_layout = QVBoxLayout()
        self.repository_layout.addLayout(self.repository_label_layout)
        self.repository_layout.addLayout(self.repository_card_layout)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.base_layout = QHBoxLayout()
        self.central_widget.setLayout(self.base_layout)

        self.info_location_layout = QHBoxLayout()
        self.info_description_layout = QVBoxLayout()
        pix = QPixmap("../resources/images/company.png")
        self.company = Pic_label(pic=pix)
        pix = QPixmap("../resources/images/location.png")
        self.location = Pic_label(pic=pix)
        self.description_label = QLabel()
        self.description_label.setWordWrap(True)
        self.info_honor_layout = QHBoxLayout()
        self.following_num = QToolButton()
        self.following_num.clicked.connect(lambda: self.on_following_num_clicked())
        self.follower_num = QToolButton()
        self.follower_num.clicked.connect(lambda: self.on_follower_num_clicked())
        self.follower_num.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.follower_num.setIcon(QIcon("../resources/images/friend.png"))
        star_num_pix = QPixmap("../resources/images/star.png")
        self.star_num = Pic_label(pic=star_num_pix)
        self.info_name_layout = QHBoxLayout()
        self.nick_label = QLabel()
        self.name_label = QLabel()
        self.avatar_url = ""
        self.name = name
        self.info_layout = QVBoxLayout()
        self.info_panel = QWidget()
        self.info_panel.setLayout(self.info_layout)
        self.info_panel.setFixedWidth(340)
        self.base_layout.addWidget(self.info_panel)
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.addLayout(self.repository_layout)
        self.scroll_layout.addLayout(self.activity_layout)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setAutoFillBackground(True)
        self.scroll_area.setWidgetResizable(True)
        self.base_layout.addWidget(self.scroll_area)
        self.pic = Pic_label()
        self.data = {}

        self.info_layout.addWidget(self.pic, alignment=Qt.AlignCenter)
        self.info_layout.addSpacing(20)
        self.info_name_layout.addWidget(self.name_label)
        self.info_name_layout.addWidget(self.nick_label)
        self.info_layout.addLayout(self.info_name_layout)
        self.info_description_layout.addWidget(self.description_label)
        self.info_location_layout.addWidget(self.location)
        self.info_location_layout.addWidget(self.company)
        self.info_description_layout.addLayout(self.info_location_layout)
        self.info_layout.addLayout(self.info_description_layout)
        self.info_layout.addSpacing(10)
        self.info_honor_layout.addWidget(self.follower_num)
        self.info_honor_layout.addWidget(self.following_num)
        self.info_honor_layout.addWidget(self.star_num)
        self.info_layout.addLayout(self.info_honor_layout)
        self.info_layout.addSpacing(10)
        self.info_layout.addStretch()
        self.setMinimumWidth(1300)

    def init_info_panel(self):
        # TODO: layout最後全部要放到__init__中
        self.data = m.giver.give_user_info(self.name)
        self.avatar_url = self.data['description']['avatar_url']

        pix = QPixmap("../resources/images/avatar.png")
        self.pic.set_pic(pix)
        self.pic.setMinimumWidth(pix.width())

        if self.data['description']['nick_name'] != "":
            self.nick_label.setText(self.data['description']['nick_name'])
        self.name_label.setText(self.name)

        self.description_label.setText(self.data['description']['comments'])
        self.location.set_text(self.data['description']['location'])
        self.company.set_text(self.data['description']['company'])

        self.follower_num.setText(str(self.data['follower_num']) + " followers")
        self.following_num.setText(str(self.data['following_num']) + " followings")
        self.star_num.set_text(str(self.data['star_num']))

    def init_main_panel(self):
        repository_data = m.giver.give_user_repository(self.name, limit=True)
        self.clear_layout(self.repository_card_layout)
        row = 0
        col = 0
        for repository in repository_data:
            self.repository_card_layout.addWidget(Repository_info_card(repository), row, col)
            if col + 1 >= 2:
                col = 0
                row = row + 1
            else:
                col = col + 1
        now = datetime.datetime.now()
        to_str = now.strftime('%Y-%m-%d')
        now = now - datetime.timedelta(days=30)
        from_str = now.strftime('%Y-%m-%d')
        activity_data = m.giver.give_user_activity(self.data['id'], from_str, to_str)
        self.clear_layout(self.activity_layout)
        for data in activity_data:
            self.activity_layout.addWidget(User_activity_card(data))

    def clear(self):
        while self.base_layout.count():
            child = self.base_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.update()

    def clear_layout(self, layout: QLayout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.update()

    def on_window_cancel(self, *args):
        pass

    def on_window_select(self, *args):
        self.name = args[0][0]
        self.init_info_panel()
        self.init_main_panel()

    def on_follower_num_clicked(self):
        pass

    def on_following_num_clicked(self):
        pass
