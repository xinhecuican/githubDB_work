from _ctypes import PyObj_FromPtr

import pymysql
from common import Debug
from lzl.src import test_data, Tables_script


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

    def drop_all_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("show tables")
        datas = cursor.fetchall()
        for data in datas:
            cursor.execute("drop table " + data[0])
        self.connection.commit()
        cursor.close()

    def create_all_tables(self):
        names = [e for e in dir(Tables_script) if not e.startswith("_")]
        cursor = self.connection.cursor()
        cursor.execute("show tables")
        datas = cursor.fetchall()
        cursor.close()
        tables = []
        for data in datas:
            tables.append(data[0])
        for name in names:
            contains = False
            for table in tables:
                if table.lower() == name.lower()[6:] and not name.startswith("test"):
                    contains = True
                    break
            if not contains:
                self.run(getattr(Tables_script, name), True)

    def run(self, state, need_commit=False, need_print = False):
        cursor = self.connection.cursor()
        try:
            cursor.execute(state)
            datas = cursor.fetchall()
            if need_print:
                print_sql(datas)
            return datas
        except:
            Debug.error_message("执行命令出错")
            Debug.print_traceback()
            cursor.close()
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
            try:
                getattr(trigger_script, func_name)(self.connection, datas)
            except pymysql.err.OperationalError as e:
                print(e)
                return False
        else:
            cursor = self.connection.cursor()
            for data in datas:
                try:

                    cursor.execute("insert into " + table + " values(" + ','.join(data) + ")")
                except:
                    Debug.print_traceback()
            self.connection.commit()
            cursor.close()
        return True

    def delete(self, table, state):
        func_name = table.lower() + "_delete"
        if hasattr(trigger_script, func_name):
            try:
                getattr(trigger_script, func_name)(self.connection, state)
            except pymysql.err.OperationalError as e:
                print(e)
                return False
        else:
            cursor = self.connection.cursor()
            cursor.execute("delete from " + table + " where " + state)
            self.connection.commit()
            cursor.close()
        return True


    def insert_all_trigger(self):
        trigger_name = [e for e in dir(trigger_script) if not e.startswith("_") and e.startswith("trigger")]
        for trigger in trigger_name:
            self.run(getattr(trigger_script, trigger), True)

    def insert_all_data(self):
        datas = [e for e in dir(test_data) if not e.startswith("_")]
        for data in datas:
            self.insert(data[:-5], getattr(test_data, data))




def print_sql(datas, cols=None):
    header_name = []
    if cols is not None:
        for col in cols:
            header_name.append(col[0])
    print(("{:<15}" * len(header_name)).format(*header_name))
    for data in datas:
        data =  [str(x) for x in data]
        print(("{:<15}" * len(data)).format(*data))


# 获得列名与值的字典
def get_row_dict(cols, data):
    ans = {}
    for i in range(len(data)):
        if isinstance(type(data[i]), str):
            ans[cols[i][0]] = "'" + data[i] + "'"
        else:
            ans[cols[i][0]] = data[i]
    return ans
