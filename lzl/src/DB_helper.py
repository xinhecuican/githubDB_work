import pymysql
from common import Debug
import trigger_script

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
            Debug.print_traceback()
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
            self.connection.commit()
        except pymysql.err.OperationalError:
            Debug.error_message("没有权限撤销或创建数据库")

        # 选择 students 这个数据库
        cursor.execute("use " + db)
        cursor.close()

    def run_state(self, state, need_commit=False):
        cursor = self.connection.cursor()
        try:
            cursor.execute(state)
            print_sql(cursor.fetchall(), cursor.description)
        except:
            Debug.error_message("执行命令出错")
            Debug.print_traceback()
        if need_commit:
            self.connection.commit()
        cursor.close()

    def show_table(self, name):
        cursor = self.connection.cursor()
        cursor.execute("select * from " + name)
        print_sql(cursor.fetchall(), cursor.description)
        cursor.close()

    def insert(self, table, datas):
        func_name = table.lower() + "_insert"
        if hasattr(trigger_script, func_name):
            getattr(trigger_script, func_name)(self.connection, datas)

        cursor = self.connection.cursor()
        for data in datas:
            cursor.execute("insert into User_info values(" ','.join(data) + ")")

        self.connection.commit()
        cursor.close()


def print_sql(datas, cols=None):
    header_name = []

    if cols is not None:
        for col in cols:
            header_name.append(cols[0])
    print(("{:<15}" * len(header_name)).format(*header_name))
    for data in datas:
        print(("{:<15}"*len(data)).format(*data))