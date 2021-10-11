from PyQt5.QtWidgets import QWidget, QLabel
import lzl.src.main as m


class User_activity_card(QWidget):

    def __init__(self, data):
        super().__init__()
        name_label = QLabel()
        name_label.linkActivated.connect(lambda : self.on_link_activated())
        user_data = m.giver.give_user_info(data['user_id'])
        if data['type'] == 0:
            name_label.setText(
                f'''<a href="u{user_data['name']}">{user_data['name']}</a> 创建仓库<a href="r{data['repository_name']}''')
        elif data['type'] == 1:
            name_label.setText(
                f'''<a href="u{user_data['name']}">{user_data['name']}</a> 提交到仓库<a href="r{data['repository_name']}''')
        elif data['type'] == 2:
            name_label.setText(
                f'''<a href="u{user_data['name']}">{user_data['name']}</a> 提交pull request到<a href="r{data['repository_name']}''')
        elif data['type'] == 3:
            name_label.setText(f'''<a href="u{user_data['name']}">{user_data['name']}</a>开始跟随你''')

        name_label.setText(name_label.text() + " " + data['date'])

    def on_link_activated(self):
        pass
