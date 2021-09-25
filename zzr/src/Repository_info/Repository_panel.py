from typing import Dict

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QWidget, QCommandLinkButton, QGridLayout, QLayout, \
    QPushButton, QScrollArea, QTabWidget, QToolButton, QMenu, QWidgetAction, QLineEdit, QListWidget, QListWidgetItem

from zzr.src.Helper.Base_window import Base_window
from zzr.src.Helper.Register import Registers
import lzl.src.main as m
from zzr.src.Repository_info.Branch_card import Branch_card
from zzr.src.Widgets.Pic_label import Pic_label
import json


@Registers.model.register
class Repository_panel(Base_window):

    def __init__(self, name):
        super().__init__()
        self.commit_info_layout = QHBoxLayout()
        self.commit_user_label = Pic_label()
        self.commit_message_label = QLabel()
        self.commit_date_label = QLabel()
        self.commit_info_layout.addWidget(self.commit_user_label)
        self.commit_info_layout.addWidget(self.commit_message_label)
        self.commit_info_layout.addWidget(self.commit_date_label, alignment=Qt.AlignRight)
        self.file_list = QListWidget()
        self.file_list.itemClicked.connect(self.file_clicked)
        self.branch_data = []
        self.search_branch_line = QWidgetAction()
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setPlaceholderText("请输入分支名")
        self.search_line_edit.returnPressed.connect(lambda: self.on_search_return_pressed())
        self.search_branch_line.setDefaultWidget(QLineEdit())
        self.branch_menu = QMenu()
        self.branch_button = QToolButton()
        self.branch_button.setPopupMode(QToolButton.InstantPopup)
        self.branch_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.branch_button.setMenu(self.branch_menu)
        self.table_widget = QTabWidget()
        self.code_area = QScrollArea()
        self.code_widget = QWidget()
        self.code_layout = QVBoxLayout()
        self.code_layout.addWidget(self.branch_button)
        self.code_layout.addLayout(self.commit_info_layout)
        self.code_layout.addWidget(self.file_list)
        self.code_area.setWidget(self.code_widget)  # 设置视口
        self.code_area.setLayout(self.code_layout)
        self.code_area.setWidgetResizable(True)
        self.table_widget.addTab(self.code_area, "代码")
        self.contributors = []
        self.contributors_layout = QVBoxLayout()
        self.language_layout = QGridLayout()
        self.release_button = QCommandLinkButton()
        self.release_button.clicked.connect(lambda: self.on_release_click())
        self.base_layout = QHBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.base_layout)
        pix = QPixmap("../resources/images/balance.png")
        self.license_label = Pic_label(pix)
        self.license_label.setMinimumHeight(pix.height())
        self.tag_label = QLabel()
        self.tag_label.setWordWrap(True)
        self.website_label = QLabel()
        self.description_label = QLabel()
        self.about = QLabel("关于")
        self.about_layout = QVBoxLayout()
        self.about_layout.addWidget(self.about)
        self.about_layout.addSpacing(20)
        self.about_layout.addWidget(self.description_label)
        self.about_layout.addWidget(self.website_label)
        self.about_layout.addWidget(self.tag_label)
        self.about_layout.addWidget(self.license_label)
        self.description_layout = QVBoxLayout()
        self.description_layout.addLayout(self.about_layout)
        self.description_layout.addSpacing(20)
        self.description_layout.addWidget(self.release_button)
        self.description_layout.addSpacing(20)
        self.contributors_layout.addLayout(self.contributors_layout)
        self.description_layout.addSpacing(20)
        self.description_layout.addLayout(self.language_layout)
        self.base_layout.addWidget(self.table_widget)
        self.base_layout.addLayout(self.description_layout)
        self.data = []
        self.name = name

    def init_description_panel(self):
        description_data = m.giver.give_repository_description(self.data['id'])
        description = description_data['description']
        if description['description'] == "" and description['website'] == "" and description['tag'][0] == "":
            self.description_label.setText("没有任何描述、网站或标签")
            self.website_label.setText("")
            self.tag_label.setText("")
            self.license_label.setText("")
        else:
            self.description_label.setText(description['description'])
            self.website_label.setText(description['website'])
            self.tag_label.setText("")
            for tag in description['tag']:
                self.tag_label.setText(self.tag_label.text() + f'''<span style="font-size: 12px;font-color:#80ccff;
                font-weight: 500;border-radius: 2em;padding-right: 10px;padding-left: 10px;
                line-height: 22px;margin: 0 .125em .333em 0;">{tag}</span>''')
            self.license_label.setText(description['license_name'])

        self.contributors = description_data['contributors']
        self.clear_layout(self.contributors_layout)
        if len(self.contributors) >= 2:
            num = 0
            for contributor in self.contributors:
                num = num + 1
                if num > 10:
                    more_button = QPushButton()
                    more_button.setText("更多")
                    more_button.clicked.connect(lambda: self.on_more_button_clicked())
                    self.contributors_layout.addWidget(more_button)
                    break
                self.contributors_layout.addWidget(QLabel(contributor['name']))

        self.release_button.setText("Releases " + str(description_data['release_num']))
        self.clear_layout(self.language_layout)
        col = 0
        row = 0
        for code in description_data['code_type']:
            label = QLabel()
            label.linkActivated.connect(lambda: self.on_link_activated())
            label.setText(code['code'] + ": " + code['percentage'])
            self.language_layout.addWidget(label)
            if col + 1 >= 2:
                col = 0
                row = row + 1
            else:
                col = col + 1

    def init_code_layer(self):
        self.code_layout.removeWidget(self.branch_button)
        self.branch_data = m.giver.give_repository_branches(self.data['id'])
        self.branch_button.setText(self.branch_data['default_branch'])
        self.branch_menu.clear()
        self.branch_menu.addAction(self.search_branch_line)
        for branch in self.branch_data['branches']:
            card = Branch_card(branch)
            card.button_click.connect(self.on_branch_card_click)
            self.branch_menu.addAction(Branch_card(branch))
        self.code_layout.addWidget(self.branch_button)

        file_data = m.giver.give_commit_file_info(self.data['latest_commit_id'])
        commit_info = m.giver.give_commit_info(self.data['latest_commit_id'])
        commit_user_info = m.giver.give_user_info(commit_info['author'])
        self.commit_user_label.set_pic(QPixmap(commit_user_info['description']['avatar_url']))
        self.commit_user_label.set_text(commit_user_info['name'])
        self.commit_message_label.setText(commit_info['message'])
        self.commit_date_label.setText(commit_info['commit_date'])

        directory = {}
        with open(file_data['directory'], "r") as f:
            directory = json.load(f)
        self.set_files(directory)

    def on_window_cancel(self, *args):
        pass

    def on_window_select(self, *args):
        self.name = args[0][0]
        self.data = m.giver.give_repository_info(self.name)
        self.init_description_panel()
        self.init_code_layer()

    def clear_layout(self, layout: QLayout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.update()

    def on_release_click(self):
        pass

    def on_link_activated(self):
        pass

    def on_more_button_clicked(self):
        pass

    def on_search_return_pressed(self):
        pass

    def on_branch_card_click(self, id, latest_commit_id):
        pass

    def file_clicked(self, item: QListWidgetItem):
        if item.data(Qt.DisplayRole) == 0:
            self.set_files(item.data(Qt.EditRole))
        else:  # 如果是文件
            pass

    def set_files(self, data: dict):
        self.file_list.clear()
        for (key, value) in data:
            if value is dict:
                item = QListWidgetItem(QIcon("../resources/images/folder.png", key))
                item.setData(Qt.EditRole, value)
                item.setData(Qt.DisplayRole, 0)
            else:
                item = QListWidgetItem(key)
                item.setData(Qt.EditRole, value)
                item.setData(Qt.DisplayRole, 1)
