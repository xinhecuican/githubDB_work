table_user = '''create table User_info{
    user_id int primary key,
    user_name varchar(100),
    follower_num int default 0,
    following_num int default 0,
    star_num int default 0,
    repository_num int default 0，
    project_num int default 0,
    package_num int default 0
};'''

table_followers = '''create table Followers{
    follower_id int primary key,
    following_id int,
    foreign key fk_follower(follower_id) references User_info(user_id),
    foreign key fk_following(following_id) references User_info(user_id)
};'''