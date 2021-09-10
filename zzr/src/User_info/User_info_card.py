from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton, QHBoxLayout


class User_info_card(QWidget):

    def __init__(self, data):
        super().__init__()
        self.name = data['name']
        self.base_layout = QVBoxLayout()

        self.button_name = QToolButton()
        self.button_name.setText(self.name)
        self.button_name.clicked.connect(lambda: self.on_name_button_click())
        self.label_star_num = QLabel('点赞数: ' + str(data['star_num']))
        self.label_follower_num = QLabel('跟随数: ' + str(data['follower_num']))
        self.label_following_num = QLabel('跟随者数: ' + str(data['following_num']))
        self.label_layout = QHBoxLayout()
        self.label_layout.addWidget(self.button_name)
        self.label_layout.addWidget(self.label_follower_num)
        self.label_layout.addWidget(self.label_following_num)

        description = data['description']
        self.comment = QLabel(description['comments'])
        self.email = QLabel(description['email'])
        self.location = QLabel(description['location'])
        self.description_layout = QVBoxLayout()
        self.description_layout.addWidget(self.comment)
        self.description_layout.addWidget(self.email)
        self.description_layout.addWidget(self.location)
        self.base_layout.addLayout(self.label_layout)
        self.base_layout.addLayout(self.description_layout)

    def on_name_button_click(self):
        print(1)
