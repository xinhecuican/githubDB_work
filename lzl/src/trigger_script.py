from pymysql import Connection


def delete(connection, table, states):
    cursor = connection.cursor()
    cursor.execute("delete from " + table + " where " + states)
    connection.commit()
    cursor.close()
    return True


def user_info_insert(connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into user_info(
                            id,
                            user_name,
                            password,
                            email,
                            follower_num,
                            following_num,
                            star_num,
                            project_num,
                            repository_num,
                            package_num)
                        values(
                            {data[0]},
                            '{data[1]}',
                            '',
                            '',
                            0,
                            0,
                            {data[2]},
                            {data[3]},
                            {data[4]},
                            {data[5]})
                        ''')
    connection.commit()
    cursor.close()


def user_info_delete(connection: Connection, states):
    cursor = connection.cursor()
    cursor.execute(f"select id from user_info where {states}")
    user_id = cursor.fetchall()
    cursor.execute(f"delete from user_info where {states}")
    for ids in user_id:
        id = ids[0]
        cursor.execute(f"delete from followers where follower_id = {id} or following_id = {id}")
        cursor.execute(f"delete from user_description where id = {id}")
        cursor.execute(f"delete from activity where user_id = {id}")
        cursor.execute(f"delete from activity_record where user_id = {id}")
        cursor.execute(f"delete from user_notification where user_id = {id}")
        delete(connection, "repository", f"user_id = {id}")
    connection.commit()
    cursor.close()


def followers_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f"update user_info set follower_num = follower_num+1 where id = {datas[0]}")
        cursor.execute(f"update user_info set following_num = following_num+1 where id = {datas[1]}")
        cursor.execute(f'''
                        insert into followers(follower_id,
                                            following_id)
                        values(
                                {data[0]},
                                {data[1]})
                        ''')
    connection.commit()
    cursor.close()


def followers_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute(f"select follower_id, following_id from followers where {states}")
    datas = cursor.fetchall()
    cursor.execute(f"delete from followers where {states}")
    for data in datas:
        cursor.execute(f"update user_info set following_num = following_num-1 where id = {data[1]}")
        cursor.execute(f"update user_info set follower_num = follower_num-1 where id = {data[0]}")
    connection.commit()
    cursor.close()


def user_description_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f"select id from user_info where id = {data[0]}")
        res = cursor.fetchall()
        if res is None:
            continue
        cursor.execute("insert into user_description values(" + ','.join(data) + ")")
    connection.commit()
    cursor.close()


def activity_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into activity(
                            type,
                            user_id,
                            owner_repository_id,
                            activity_date)
                        values(
                            {data[0]},
                            {data[1]},
                            {data[2]},
                            {data[3]},
                            '{data[4]}')
                        ''')


def activity_record_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into activity_record(
                            user_id,
                            clear_date,
                            contribution_num,
                            related_activities_id)
                        values(
                            {data[0]},
                            '{data[1]}',
                            {data[2]},
                            '{data[3]}')
                        ''')
    connection.commit()
    cursor.close()


# 更新user_info中repository_num
def repository_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute(f"select id, user_id from repository where {states}")
    datas = cursor.fetchall()
    cursor.execute(f"delete from repository where {states}")
    for data in datas:
        cursor.execute(f"update user_info set repository_num = repository_num - 1 where id = {data[1]}")
        cursor.execute(f"delete from repository_info where id = {data[0]}")
        delete(connection, "tags", f"repository_id = {data[0]}")
        delete(connection, "issue", f"repository_id = {data[0]}")
        delete(connection, "pull_request", f"repository_id = {data[0]}")
        cursor.execute(f"delete from labels where repository_id = {data[0]}")
        cursor.execute(f"delete from branches where repository_id = {data[0]}")
        delete(connection, "commits", f"repository_id = {data[0]}")
    connection.commit()
    cursor.close()


def repository_info_insert(connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into repository_info(
                            id, 
                            description,
                            website,
                            licenses_id,
                            tag,
                            code_type,
                            contributors,
                            release_num)
                        values(
                            {data[0]},
                            {data[1]},
                            {data[2]},
                            {data[3]},
                            {data[4]},
                            {data[5]},
                            {data[6]},
                            {data[7]})
                        ''')
    connection.commit()
    cursor.close()


def licenses_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into licenses(
                            name,
                            license_content,
                            permissions,
                            limitations,
                            conditions
                        )
                        values(
                            "{data[0]}",
                            "{data[1]}",
                            "{data[2]}",
                            "{data[3]}",
                            "{data[4]}")
                        ''')
    connection.commit()
    cursor.close()


def tags_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into tags(
                            repository_id,
                            user_id,
                            name,
                            type,
                            related_id,
                            asset_num,
                            publish_date,
                            is_pre_release,
                            react)
                        values(
                            {data[0]},
                            {data[1]},
                            {data[2]},
                            {data[3]},
                            {data[4]},
                            {data[5]},
                            {data[6]},
                            {data[7]},
                            {data[8]})
                        ''')
        cursor.execute(f"update repository_info set release_num = release_num+1 where id = {data[0]}")
    connection.commit()
    cursor.close()


def tags_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute(f"select id from tags where {states}")
    datas = cursor.fetchall()
    cursor.execute(f"delete from tags where {states}")
    for data in datas:
        cursor.execute(f"delete from tag_files where tag_id = {data[0]}")
    connection.commit()
    cursor.close()


def tag_files_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into tag_files(
                            tag_id,
                            name,
                            size,
                            file_link)
                        values(
                            {data[0]},
                            {data[1]},
                            {data[2]},
                            {data[3]})
                        ''')
    connection.commit()
    cursor.close()


def issue_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into issue(
                            repository_id,
                            creator_id,
                            labels,
                            status,
                            create_date,
                            comments_sum,
                            question)
                        values(
                            {data[0]},
                            {data[1]},
                            '{data[2]}',
                            {data[3]},
                            '{data[4]}',
                            {data[5]},
                            '{data[6]}')
                        ''')
    connection.commit()
    cursor.close()


def issue_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute(f"select id from issue where {states}")
    datas = cursor.fetchall()
    cursor.execute(f"delete from issue where {states}")
    for data in datas:
        cursor.execute(f"delete from issue_comment where issue_id = {data[0]}")
    connection.commit()
    cursor.close()


def issue_comment_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into issue_comment(
                            issue_id,
                            quota_id,
                            user_id,
                            name,
                            action,
                            commit_date,
                            content)
                        values(
                            {data[0]},
                            {data[1]},
                            {data[2]},
                            '{data[3]}',
                            {data[4]},
                            '{data[5]}',
                            '{data[6]}')
                        ''')
    connection.commit()
    cursor.close()


def labels_inset(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into labels(
                            repository_id,
                            url,
                            name,
                            color)
                        values(
                            {data[0]},
                            '{data[1]}',
                            '{data[2]}',
                            '{data[3]}')
                        ''')
    connection.commit()
    cursor.close()


def pull_request_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into pull_request(
                            repository_id,
                            question_id,
                            base_branch_id,
                            from_branch_id,
                            related_commit_id,
                            is_open,
                            merge_status,
                            check_status)
                        values(
                            {data[0]}, {data[1]}, {data[2]}, {data[3]},
                            {data[4]}, {data[5]}, {data[6]}, {data[7]})
                        ''')
    connection.commit()
    cursor.close()


def pull_request_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute(f"select id from pull_request where {states}")
    datas = cursor.fetchall()
    cursor.execute(f"delete from pull_request where {states}")
    for data in datas:
        cursor.execute(f"delete from pull_request_info where id = {data[0]}")
        cursor.execute(f"delete from pull_request_action where pull_request_id = {data[0]}")
    connection.commit()
    cursor.close()


def pull_request_action_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into pull_request_action(
                            pull_request_id,
                            user_id,
                            comment,
                            action)
                        values(
                            {data[0]},
                            {data[1]},
                            '{data[2]}',
                            {data[3]})
                        ''')
    connection.commit()
    cursor.close()


def branches_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into branches(
                            branch_name,
                            repository_id,
                            latest_commit,
                            commit_num)
                        values(
                            '{data[0]}',
                            {data[1]},
                            {data[2]},
                            {data[3]})
                        ''')
    connection.commit()
    cursor.close()


def commits_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into commits(
                            commit_sha,
                            parent_commit,
                            repository_id,
                            author_user_id,
                            commit_user_id,
                            commit_date,
                            message)
                        values(
                            {data[0]},
                            {data[1]},
                            {data[2]},
                            {data[3]},
                            {data[4]},
                            {data[5]},
                            {data[6]})
                        ''')
    connection.commit()
    cursor.close()


def commits_delete(connection, states):
    cursor = connection.cursor()
    cursor.execute(f"select id, parent_commit from commits where {states}")
    datas = cursor.fetchall()
    for data in datas:
        cursor.execute(f"update commits set parent_commit = {data[2]} where parent_commit = {data[0]}")
        cursor.execute(f"delete from commits where id = {data[0]}")
        cursor.execute(f"delete from commit_file_info where id = {data[0]}")
        cursor.execute(f"delete from commit_files where commit_id = {data[0]}")
        cursor.execute(f"delete from commit_comment where commit_id = {data[0]}")
    connection.commit()
    cursor.close()


def commit_files_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into commit_files(
                            commit_id,
                            file_name,
                            commit_comment,
                            file_type,
                            file_action,
                            file_line,
                            add_lines,
                            remove_lines,
                            file_path)
                        values(
                            {data[0]},
                            {data[1]},
                            {data[2]},
                            {data[3]},
                            {data[4]},
                            {data[5]},
                            {data[6]},
                            {data[7]},
                            {data[8]})
                        ''')
    connection.commit()
    cursor.close()


def commit_comment_insert(connection: Connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute(f'''
                        insert into commit_comment(
                            commit_id,
                            quota_id,
                            comment_date,
                            comment_content)
                        values(
                            {data[0]},
                            {data[1]},
                            '{data[2]}',
                            '{data[3]}')
                        ''')
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
