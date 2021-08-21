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
        signal sqlstate '45000';
    end if;
end;'''

trigger_repository_insert = '''
create trigger on_repository_insert
before insert on Repository
for each row
begin
    if(exists(select * from Repository where new.owner_id = owner_id and new.name = name))then
        signal sqlstate '45000'
    end if;
end'''
