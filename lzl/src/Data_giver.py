# from lzl.src.DB_helper import DB_helper

class Data_giver:

    def __init__(self, helper):
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
            if res:
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
        if res:
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

    def give_user_info(self, user_info):
        """
        未找到返回None
        :param user_info: 可以使id或name
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
                                                'link',
                                                'avatar_url'
                            }
        """
        cursor = self.helper.connection.cursor()
        if type(user_info) is str:
            cursor.execute(f'''select id, user_name, follower_num, following_num,
                       star_num, repository_num from user_info where user_name = '{user_info}';''')
        elif type(user_info) is int:
            cursor.execute(f'''select id, user_name, follower_num, following_num,
                                   star_num, repository_num from user_info where user_name = {user_info};''')
        info = cursor.fetchall()
        if not info:
            return None
        ans = {}
        for data in info:
            ans['id'] = data[0]
            ans['name'] = data[1]
            ans['follower_num'] = data[2]
            ans['following_num'] = data[3]
            ans['star_num'] = data[4]
            ans['repository_num'] = data[5]
            cursor.execute(f'''select nick_name, status, company, location, comments, link, avatar_url
                            from user_description where id = {data[0]}''')
            res = cursor.fetchall()
            if not res:
                return None
            res = res[0]
            ans['description'] = {
                'nick_name': res[0],
                'status': res[1],
                'company': res[2],
                'location': res[3],
                'comments': res[4],
                'link': res[5],
                'avatar_url': res[6]
            }
        cursor.close()
        return ans

    def give_user_activity(self, user_id, from_date, to_date):
        """

        :param user_id:
        :param from_date: 格式YY-MM-DD
        :param to_date:
        :return: (Array): [{
                                type: 活动类型
                                user_id
                                commit_id
                                repository_name: 活动关联仓库名
                                date:
                            }]

        """
        sql = f'''
        select type, activity.user_id, activity.commit_id, repository.name, activity.activity_date
        from activity
        join repository on repository.id = activity.owner_repository_id
        where activity.user_id = {user_id} and Date(activity_date) between '{from_date}' and '{to_date}'
        order by activity_date;'''
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        res = []
        for data in datas:
            res.append({
                'type': data[0],
                'user_id': data[1],
                'commit_id': data[2],
                'repository_name': data[3],
                'date': data[4]
            })
        cursor.close()
        return res

    def give_repository_info(self, name):
        """

        :param name:
        :return: （Object){
            name (str): 仓库名
            id (int): 仓库id
            author (str): 仓库创作者名字
            star_num (int)
            fork_num
            contributor_num (int): 贡献者数量
            description:{
                            code_type (str): 仓库代码类型
                            description (str)
                        }
        }
        """
        sql = f'''
        select repository.name, repository.id, user_description.user_name, repository.star_num, 
        repository.fork_num, repository.contributor_num
        from repository
        join user_description
        on repository.user_id = user_description.id
        where repository.name = '{name}';'''
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        ans = {}
        for data in datas:
            ans['name'] = data[0]
            ans['id'] = data[1]
            ans['author'] = data[2]
            ans['star_num'] = data[3]
            ans['fork_num'] = data[4]
            ans['contributor_num'] = data[5]
        sql = f'''select code_type, description
        from repository_info
        where id = {ans['id']}'''
        cursor.execute(sql)
        datas = cursor.fetchall()
        for data in datas:
            ans['description'] = {
                'code_type': data[0],
                'description': data[1]
            }
        cursor.close()
        return ans

    def give_user_repository(self, user_name: str, limit=False):
        """

        :param limit: 只显示前十个
        :param user_name:
        :return: (Array)[
            所有在give_repository_info中的属性
        ]
        """
        sql = f'''
        select repository.name
        from user_info
        join repository
        on user_info.id = repository.user_id
        where user_info.user_name = '{user_name}'
        '''
        if limit:
            sql += " order by repository.star_num limit 10"
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        ans = []
        for data in datas:
            ans.append(self.give_repository_info(data[0]))
        cursor.close()
        return ans

    def give_repository_description(self, id):
        """

        :param id:
        :return:{
                    release_num:
                    contributors:[{
                                    id:
                                    name
                                }]
                    about {
                                description
                                website
                                license_name
                                license_content
                                tag
                                code_type
                                [{
                                    code:
                                    percentage
                                }]
                        }
                }
        """
        sql = f'''
                select release_num, contributors, description, website, licenses.name, license_content, tag, code_type
                from repository_info
                join licenses
                on repository_info.licenses_id = licenses
                where repository_info.id = {id}
                '''
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        ans = {}
        for data in datas:
            ans['release_num'] = data[0]
            ans['contributors'] = eval(data[1])
            ans['about'] = {
                'description': data[2],
                'website': data[3],
                'license_name': data[4],
                'license_content': data[5],
                'tag': eval(data[6]),
                'code_type': eval(data[7])
            }
        cursor.close()
        return ans

    def give_repository_branches(self, id):
        """

        :param id:
        :return: (Object){
                            default_branch:
                            branches[{
                                        id:
                                        name:
                                        latest_commit_id
                                    }]
                        }
        """
        sql = f'''
        select default_branch
        from repository
        where repository.id = {id}'''
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        ans = {'default_branch': cursor.fetchall()[0][0], 'branches': []}
        sql = f'''
        select branches.id, branch_name, latest_commit
        from branches
        where branches.repository_id = {id}
        '''
        cursor.execute()
        datas = cursor.fetchall()
        for data in datas:
            ans['branches'].append({
                'id': data[0],
                'name': data[1],
                'latest_commit_id': data[2]
            })
        cursor.close()
        return ans

    def get_commit_file_info(self, id):
        """

        :param id:
        :return: (Object){
                            directory_address:
                            add_line:
                            delete_line:
                            change_file_num
        """
        sql = f'''
        select commit_file_address, add_line, delete_line, change_file_num
        from commit_file_info
        where id = {id}
        '''
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        ans = {
            'directory_address': data[0],
            'add_line': data[1],
            'delete_line': data[2],
            'change_file_num': data[3]
        }
        cursor.close()
        return ans

    def get_commit_info(self, id):
        """

        :param id:
        :return: (Object){
                            message:
                            parent_commit_id:
                            author:
                            commit_user:
                            commit_date:
        """
        sql = f'''
            select message, parent_commit, author_user_id, commit_user_id, commit_date
            from commits
            where id = {id}
            '''
        cursor = self.helper.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        cursor.close()
        ans = {
            'message': data[0],
            'parent_commit_id': data[1],
            'author': data[2],
            'commit_user': data[3],
            'commit_date': data[4]
        }
        return ans
