from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
import lzl.src.main as m


class File_item(QWidget):

    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        list_layout = QHBoxLayout()
        name_label = QLabel(key)
        comment_label = QLabel()
        metrics = comment_label.fontMetrics()
        str = metrics.elidedText(m.helper.run(f'select commit_comment from commit_files where id = {value}')[0][0]
                                 , Qt.ElideRight, 300)
        comment_label.setText(str)
        list_layout.addWidget(name_label)
        list_layout.addWidget(comment_label)
        self.setLayout(list_layout)
