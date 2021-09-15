from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QCommandLinkButton, QLabel, QVBoxLayout, QHBoxLayout

from zzr.src.Widgets.Pic_label import Pic_label


class Repository_info_card(QWidget):

    def __init__(self, data):
        super().__init__()
        self.setFixedHeight(100)
        self.setStyleSheet('''
                QCommandLinkButton:hover{
                    background-color: rgba(98, 230, 230, 0.2);
                }
                QCommandLinkButton:pressed{
                    background-color: rgba(255, 255, 255, 0.3);
                }
                QHeaderView::section, QTableCornerButton::section 
                {
                    padding: 1px;border: none;
                    border-bottom: 1px solid rgb(75, 120, 154);
                    border-right: 1px solid rgb(75, 120, 154);
                    border-bottom: 1px solid gray;
                    background-color:rgba(75, 120, 154, 1);}


                QHeaderView::section
                {
                    font-size:14px;
                    font-family:"Microsoft YaHei";
                    background-color: transparent;
                    border:none;
                    text-align:left;
                    margin-left:0px;
                    padding-left:0px;
                }
                QTableWidget::item
                {
                    border-bottom:1px solid #EEF1F7 ;
                }
                QTableWidget::item::selected
                {
                    color:red;
                    background: rgba(74, 218, 218, 0.2);
                }
                ''')
        self.name = QCommandLinkButton()
        self.name.setText(data['name'])
        self.name.setFixedHeight(40)

        self.author = QLabel()
        self.author.setText("作者: " + data['author'])

        self.base_layout = QVBoxLayout()
        self.base_layout.setDirection(QVBoxLayout.TopToBottom)

        self.description_layout = QHBoxLayout()
        self.description_layout.addWidget(self.name)
        self.description_layout.addWidget(self.author)
        self.base_layout.addLayout(self.description_layout)
        self.star_num = Pic_label(pic=QPixmap("../resources/images/star.png"), text=str(data['star_num']))
        self.fork_num = Pic_label(pic=QPixmap("../resources/images/fork.png"), text=str(data['fork_num']))
        pix = QPixmap("../resources/images/friend.png")
        pix = pix.scaled(24, 24)
        self.contributor_num = Pic_label(pix, str(data['contributor_num']))
        self.sum_layout = QHBoxLayout()
        self.sum_layout.addWidget(self.star_num)
        self.sum_layout.addWidget(self.fork_num)
        self.sum_layout.addWidget(self.contributor_num)

        self.base_layout.addLayout(self.sum_layout)
        self.setLayout(self.base_layout)




