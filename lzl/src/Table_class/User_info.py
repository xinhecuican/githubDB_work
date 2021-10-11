from abc import ABC

from lzl.src.Table_class.Base_table import Base_table


class User_info(Base_table, ABC):
    def __init__(self, col_name, datas):
        self.user_id = 0
        self.user_name = ''
        self.follower_num = 0
        self.following_num = 0
        self.star_num = 0
        self.repository_num = 0
        self.project_num = 0
        self.package_num = 0
        self.read(col_name, datas)

    def read(self, col_name, datas):
        d = User_info
        for i in range(len(col_name)):
            d[col_name[i]] = datas[i]

    def write(self, file):
        pass

