import datetime
import os
from typing import Dict

import requests as requests
import urllib3
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon, QCloseEvent
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QWidget, QCommandLinkButton, QGridLayout, QLayout, \
    QPushButton, QScrollArea, QTabWidget, QToolButton, QMenu, QWidgetAction, QLineEdit, QListWidget, QListWidgetItem, \
    QListView, QStackedWidget, QTextEdit
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from zzr.src.Helper import Window_manager
from zzr.src.Helper.Base_window import Base_window
from zzr.src.Helper.Register import Registers
import lzl.src.main as m
from zzr.src.Repository_info.Branch_card import Branch_card
from zzr.src.Repository_info.File_item import File_item
from zzr.src.Widgets.Pic_label import Pic_label
import json


@Registers.model.register
class Repository_panel(Base_window):

    def __init__(self, name):
        super().__init__()
        self.dir_link_text = QLabel()
        self.dir_link_text.setTextFormat(Qt.RichText)
        self.dir_link_text.linkActivated.connect(self.on_dir_link_actived)
        self.user_data = {}
        self.parent_dir = ''
        self.directory = {}
        self.now_dir = {}
        self.commit_info_layout = QHBoxLayout()
        self.commit_user_label = Pic_label()
        self.commit_message_label = QLabel()
        self.commit_date_label = QLabel()

        self.stack_widget = QStackedWidget()
        self.file_list = QListWidget()
        self.file_list.itemClicked.connect(self.file_clicked)
        self.code_text = QTextEdit()
        self.stack_widget.addWidget(self.code_text)
        self.stack_widget.addWidget(self.file_list)
        self.stack_widget.setCurrentWidget(self.file_list)
        self.branch_data = []
        self.search_branch_line = QWidgetAction(self)
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setPlaceholderText("请输入分支名")
        self.search_line_edit.returnPressed.connect(lambda: self.on_search_return_pressed())
        self.search_branch_line.setDefaultWidget(self.search_line_edit)
        self.branch_menu = QMenu()
        self.branch_menu.addAction(self.search_branch_line)
        self.branch_button = QToolButton()
        self.branch_button.setPopupMode(QToolButton.InstantPopup)
        self.branch_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.branch_button.setMenu(self.branch_menu)
        self.table_widget = QTabWidget()
        self.code_area = QScrollArea()
        self.code_widget = QWidget()
        self.code_layout = QVBoxLayout()
        self.commit_info_layout.addWidget(self.branch_button)
        self.commit_info_layout.addWidget(self.commit_user_label)
        self.commit_info_layout.addWidget(self.commit_message_label)
        self.commit_info_layout.addWidget(self.commit_date_label, alignment=Qt.AlignRight)
        self.code_layout.addLayout(self.commit_info_layout)
        self.code_layout.addWidget(self.stack_widget)
        self.code_area.setWidget(self.code_widget)  # 设置视口
        self.code_area.setLayout(self.code_layout)
        self.code_area.setWidgetResizable(True)
        self.code_area.setMinimumWidth(500)
        self.table_widget.addTab(self.code_area, "代码")
        self.main_area_layout = QVBoxLayout()
        self.main_area_layout.addWidget(self.dir_link_text)
        self.main_area_layout.addWidget(self.table_widget)
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
        self.description_label.setWordWrap(True)
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
        self.description_widget = QWidget()
        self.description_widget.setMaximumWidth(200)
        self.description_widget.setLayout(self.description_layout)
        self.base_layout.addLayout(self.main_area_layout)
        self.base_layout.addWidget(self.description_widget)
        self.data = []
        self.name = name

    def init_description_panel(self):
        description_data = m.giver.give_repository_description(self.data['id'])
        description = description_data['about']
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
            if description['license_name'] is not None:
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
        for (key, value) in description['code_type'].items():
            label = QLabel()
            label.linkActivated.connect(lambda: self.on_link_activated())
            label.setText(key + ": " + value)
            self.language_layout.addWidget(label, row, col)
            if col + 1 >= 2:
                col = 0
                row = row + 1
            else:
                col = col + 1

    def init_code_layer(self):
        self.branch_data = m.giver.give_repository_branches(self.data['id'])
        self.branch_button.setText(self.branch_data['branches'][str(self.branch_data['default_branch'])]['name'])
        self.branch_menu.clear()
        self.branch_menu.addAction(self.search_branch_line)
        for branch in self.branch_data['branches'].items():
            card = Branch_card(branch)
            card.button_click.connect(self.on_branch_card_click)
            self.branch_menu.addAction(Branch_card(branch))

        default_branch = self.branch_data['branches'][str(self.branch_data['default_branch'])]
        file_data = m.giver.give_commit_file_info(default_branch['latest_commit_id'])
        commit_info = m.giver.give_commit_info(default_branch['latest_commit_id'])
        self.dir_link_text.setText(f'''<a style="color: blue;" href="{self.data['name']}">{self.data['name']}</a>/''')
        pix = QPixmap()
        commit_user_info = m.giver.give_user_info(commit_info['author'])
        if os.path.exists('../../lhx/res/files/' + commit_user_info['name'] + '/avatar.png'):
            pix.load('../../lhx/res/files/' + commit_user_info['name'] + '/avatar.png')
        else:
            url = commit_user_info['description']['avatar_url']
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
            myfile = requests.get(url, headers=headers)
            open('../../lhx/res/files/' + commit_user_info['name'] + '/avatar.png', 'wb').write(myfile.content)
            pix.load('../../lhx/res/files/' + commit_user_info['name'] + '/avatar.png')
        pix = pix.scaled(24, 24)
        self.commit_user_label.set_pic(pix)
        self.commit_user_label.set_text(commit_user_info['name'])
        self.commit_message_label.setText(commit_info['message'])
        self.commit_date_label.setText(str(commit_info['commit_date'].date()))

        self.parent_dir = ''
        self.now_dir = ''
        self.directory = {}
        with open(file_data['directory_address'], "r") as f:
            self.directory = json.load(f)
        self.now_dir = self.directory
        self.set_files(self.directory)

    def on_window_cancel(self, *args):
        pass

    def on_window_select(self, *args):
        self.name = args[0][0]
        self.data = m.giver.give_repository_info(self.name)
        self.user_data = m.giver.give_user_info(self.data['user_id'])
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

    def on_dir_link_actived(self, link:str):
        if link == self.data['name']:
            self.now_dir = self.directory
            self.parent_dir= ''
            self.dir_link_text.setText(
                f'''<a style="color: blue;" href="{self.data['name']}">{self.data['name']}</a>/''')
            self.set_files(self.now_dir)
        else:
            datas = link.split('/')
            self.now_dir = self.directory
            self.parent_dir = ''
            self.dir_link_text.setText(
                f'''<a style="color: blue;" href="{self.data['name']}">{self.data['name']}</a>/''')
            for i in range(len(datas)-1):
                self.now_dir = self.now_dir[datas[i]]
                self.parent_dir += datas[i] + "/"
                self.dir_link_text.setText(
                    self.dir_link_text.text() + f'''<a style="color blue;" href="{self.parent_dir}">{datas[i]}</a>/''')
            self.set_files(self.now_dir)

    def file_clicked(self, item: QListWidgetItem):
        item_widget = self.file_list.itemWidget(item)
        if type(item_widget) == File_item:
            data = m.helper.run(f'''
                                select commit_sha from commits 
                                join commit_files 
                                on commit_files.commit_id = commits.id 
                                where commit_files.id = {item_widget.value}''')
            if not os.path.exists(f"../../lhx/res/files/{self.user_data['name']}/{self.data['name']}/{data[0][0][0:7]}/{item_widget.key if self.parent_dir=='' else self.parent_dir.replace('/', '&') + '&' + item_widget.key}"):
                self.code_text.setText("对应文件未爬取")
            else:
                with open(f"../../lhx/res/files/{self.user_data['name']}/{self.data['name']}/{data[0][0][0:7]}/{item_widget.key if self.parent_dir=='' else self.parent_dir.replace('/', '&') + '&' + item_widget.key}", 'r', encoding='utf-8') as f:
                    self.code_text.setText(f.read())
            self.stack_widget.setCurrentWidget(self.code_text)
        else:
            self.parent_dir += item_widget.text + "/"
            self.now_dir = self.now_dir[item_widget.text]
            self.dir_link_text.setText(self.dir_link_text.text() + f'''<a style="color blue;" href="{self.parent_dir}">{item_widget.text}</a>/''')
            self.set_files(self.now_dir)

    def set_files(self, data: dict):
        self.file_list.clear()
        self.stack_widget.setCurrentWidget(self.file_list)
        for (key, value) in data.items():
            if key == '__parent__':
                continue
            item = QListWidgetItem()
            item.setSizeHint(QSize(100, 45))
            self.file_list.addItem(item)
            if type(value) is dict:
                # item.setData(Qt.EditRole, value)
                # item.setData(Qt.DisplayRole, 0)
                label = Pic_label(QPixmap("../resources/images/folder.png"), key)
                self.file_list.setItemWidget(item, label)
            else:
                list_widget = File_item(key, value)
                # item.setData(Qt.EditRole, value)
                # item.setData(Qt.DisplayRole, 1)
                self.file_list.setItemWidget(item, list_widget)

    def closeEvent(self, a0: QCloseEvent):
        a0.accept()
        Window_manager.change_window("MainWindow")

