from lzl.src.DB_helper import DB_helper

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
            row_count = 0
            res = self.helper.run(f"select count(*) from {name}")
            if res is not None:
                row_count = res[0][0]
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

    def give_table_info(self, table_name):
        ans = {}
        row_count = 0
        res = self.helper.run(f"select count(*) from {table_name}")
        if res is not None:
            row_count = res[0][0]
        col_infos = self.helper.run(f"desc {table_name}")
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
        ans['name'] = table_name
        ans['rows'] = row_count
        ans['col_info'] = info_arr
        return ans

    def give_table(self, table_name):
        """

        :param table_name: 表名
        :return (Array): 返回一个二维列表，第一行是列名，其他行是数据
        """
        cursor = self.helper.connection.cursor()
        cursor.execute(f"select * from '{table_name}'")
        col_name = []
        for cols in cursor.description:
            col_name.append(cols[0])
        datas = cursor.fetchall()
        cursor.close()
        ans = []
        ans.append(col_name)
        for data in datas:
            ans.append(data)
        return ans

    def give_user_info(self, user_name):
        """
        未找到返回None
        :param user_name:
        :return: (Object){
                        'id': 用户id
                        'name' 用户名
                        'follower_num':
                        'following_num':
                        'star_num':
                        'repository_num':
                        'description' (Object):{
                                                'nick_name'
                                                'status':
                                                'company'
                                                'location':
                                                'comments'
                                                'link'
                            }
        """
        cursor = self.helper.connection.cursor()
        cursor.execute(f"select id, user_name, follower_num, following_num,"
                       f"star_num, repository_num from user_info where user_name = '{user_name}'")
        info = cursor.fetchall()
        if info is None:
            return None
        ans = {}
        for data in info:
            ans['id'] = data[0]
            ans['name'] = data[1]
            ans['follower_num'] = data[4]
            ans['following_num'] = data[5]
            ans['star_num'] = data[6]
            ans['repository_num'] = data[8]
            cursor.execute(f'''select nick_name, status, company, location, comments, link 
                            from user_description where id = {data[0]}''')
            res = cursor.fetchall()[0]
            ans['description'] = {
                'nick_name': res[0],
                'status': res[1],
                'company': res[2],
                'location': res[3],
                'comments': res[4],
                'link': res[5]
            }
        return ans

    def give_user_activity(self, user_id, from_date, to_date):
        """

        :param user_id:
        :param from_date: 格式YY-MM-DD
        :param to_date:
        :return: (Array): [[是一个二维数组
                            type: 活动类型
                            repository_name: 活动关联仓库名

        """
        sql = f'''
        select type, repository.name, activity.date
        from activity
        join repository on repository.id = activity.owner_repository_id
        where user_id = {user_id} and Date(activity_date) between '{from_date}' to '{to_date}'
        order by activity_date;'''
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
