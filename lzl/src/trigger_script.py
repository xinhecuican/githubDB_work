import DB_helper


def user_info_insert(connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute("select * from User_info where user_id = " + data[0] + " limit 1")
        row = cursor.fetchone()
        d = cursor.description
        if row is not None:
            description = ""
            for i in range(1, len(row)):
                description += d[i][0] + "=" + data[i] + ","
            cursor.execute("update User_info set " + description[:-1])
            connection.commit()
        else:
            cursor.execute("insert into User_info values(" + ','.join(data) + ")")
            connection.commit()
    cursor.close()


def followers_delete(connection, states):
    cursor = connection.cursor()
    sql = f'''update user_info set follower_num = follower_num-1
    where user_id in
        {{
            select following_id from followers
            where {states}
        }}'''

    cursor.execute(sql)
    sql = f'''update user_info set following_num = following_num - 1
    where user_id in
    {{
        select follower_id from followers
        where {states}
    }}'''
    cursor.execute(sql)
    cursor.execute(f"delete from followers where {states}")
    connection.commit()
    cursor.close()


# 更新user_info中repository_num
def repository_delete(connection, states):
    sql = f'''update user_info set repository_num = repository_num - 1
    where user_id in
        {{
            select owner_id from repository
            where {states} 
        }}'''
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.execute(f"delete from repository where {states}")
    connection.commit()
    cursor.close()


def branches_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute("select branch_id from branches where " + states)
    datas = cursor.fetchall()
    for data in datas:
        cursor.execute(f"select parent_branch from branches where branch_id='{data[0]}'")
        parent_branch = cursor.fetchone()[0]
        cursor.execute(f"update branches set parent_branch= '{parent_branch}' where parent_branch='{data[0]}'")

    cursor.execute("delete from branches where " + states)
    connection.commit()
    cursor.close()


def commits_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute("select commit_id from Commits where " + states)
    datas = cursor.fetchall()
    for data in datas:
        cursor.execute(f"select commit_id from Commits where parent_commit ='{data[0]}'")
        child_datas = cursor.fetchall()
        cursor.execute(f"select parent_commit from Commits where commit_id='{data[0]}'")
        parent_commit = cursor.fetchone()[0]
        for child_data in child_datas:  # 更新commit的parent
            cursor.execute(f"update Commits set parent= '{parent_commit}' where commit_id = '{child_data[0]}'")
        cursor.execute(f"update Branches set latest_commit='{parent_commit}' where "
                       f"latest_commit = '{data[0]}'")
    cursor.execute("delete from Commits where " + states)
    connection.commit()
    cursor.close()


trigger_user_info_delete = '''
create trigger on_user_info_delete
after delete on User_info
for each row
begin
    delete from Repository where owner_id = old.user_id;
end;'''

trigger_branches_insert = '''
create trigger on_branches_insert
before insert on Branches
for each row
begin
    if(not exists(select * from Branches where new.branch_id = branch_id))then
        signal sqlstate '45000' set message_text = 'parent branches don't exists';
    end if;
end;'''

trigger_branches_delete = '''
create trigger on_branches_delete
after delete on Branches
for each row
begin
    if(exists(select * from repository 
    where repository_id = old.owner_repository and default_branch = old.branch_name))then
        signal sqlstate '45000' set message_text = 'can't delete default branches';
    end if;
end;'''

# 检测是否有重复的库
trigger_repository_insert = '''
create trigger on_repository_insert
before insert on Repository
for each row
begin
    if(exists(select * from Repository where new.owner_id = owner_id and new.name = name))then
        signal sqlstate '45000' set message_text = 'data have already been inserted';
    end if;
end'''
