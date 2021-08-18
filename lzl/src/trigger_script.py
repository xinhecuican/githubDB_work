
def user_info_insert(connection, datas):
    cursor = connection.cursor()
    for data in datas:
        cursor.execute("select count(*) from User_info where user_id = " + data[0] + " limit 1")
        row = cursor.fetchone()
        if row[0] == 1:
            cursor.execute("delete from User_info where user_id = " + data[0])
            cursor.execute("insert into User_info values(" ','.join(data) + ")")
            connection.commit()
    cursor.close()