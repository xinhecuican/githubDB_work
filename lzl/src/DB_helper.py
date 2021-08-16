import pymysql
from common import Debug


class DB_helper():
    def __init__(self, host, username, password, db=""):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        try:
            self.connection = pymysql.connect(host=self.host, user=self.username, password=self.password)
        except:
            Debug.error_message("数据库连接失败")
        if db != "":
            self.connect_db(db)

    def __del__(self):
        self.connection.close()

    def connect_db(self, db):
        cursor = self.connection.cursor()
        cursor.execute("use " + db)
        cursor.close()

    def create_db(self, db):
        cursor = self.connection.cursor()
        try:
            cursor.execute("drop database if exists " + db)
            cursor.execute("create database " + db)
        except pymysql.err.OperationalError:
            Debug.error_message("没有权限撤销或创建数据库")

        # 选择 students 这个数据库
        cursor.execute("use " + db)
        cursor.close()

    def run_state(self, state, need_commit=False):
        cursor = self.connection.cursor()
        try:
            cursor.execute(state)
            datas = cursor.fetchall()
            for data in datas:
                print(data)
        except:
            Debug.error_message("执行命令出错")
        if need_commit:
            self.connection.commit()
        cursor.close()

    def show_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("select * from " + name)
        cursor.close()
