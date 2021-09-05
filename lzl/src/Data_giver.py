from DB_helper import DB_helper


class Data_giver:

    def __init__(self, helper: DB_helper):
        self.helper = helper

    def give_tables_info(self):
        """
        返回所有表格的大致信息（如果不知道返回的格式可以print查看）
        :return: (Array)
        returnparam: name (str) 表格名
        returnparam: rows (int) 表格的行数
        returnparam: col_info (Array)[{
                                        name (str): 列名
                                        type (str): 列的类型
                                        null_enable (bool): 是否可以是空值
                                        key (str): 如果是pri则是主键，如果是mul则有外键
                                        default: 默认值
                                        is_auto_increment (bool): 是否是自增列
                                    }]
        """
        ans = []
        table_names = self.helper.run("show tables")
        for table_name in table_names:
            name = table_name[0]
            row_count = self.helper.run(f"select count(*) from {name}")[0][0]
            col_infos = self.helper.run(f"desc {name}")
            info_arr = []
            for col_info in col_infos:
                info_arr.append({
                    'name': col_info[0],
                    'type': col_info[1],
                    'null_enable': True if col_info[2] == 'YES' else False,
                    'key': col_info[3],
                    'default': col_info[4],
                    'is_auto_increment': True if col_info[5] == 'auto_increment' else False
                })
            ans.append({
                'name': name,
                'rows': row_count,
                'col_info': info_arr
            })
        return ans

    def give_table(self, table_name):
        """

        :param table_name: 表名
        :return (Array): 返回一个二维列表，第一行是列名，其他行是数据
        """
        cursor = self.helper.connection.cursor()
        cursor.execute(f"select * from {table_name}")
        col_name = []
        for cols in cursor.description:
            col_name.append(cols[0])
        datas = cursor.fetchall()
        ans = []
        ans.append(col_name)
        for data in datas:
            ans.append(data)
        return ans
