table_user_info = '''create table User_info{
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
    foreign key fk_follower(follower_id) references User_info(user_id)
    on delete cascade
    on update cascade,
    foreign key fk_following(following_id) references User_info(user_id)
    on delete cascade
    on update cascade
};'''

table_repository = '''
create table Repository(
    repository_id int primary key auto_increment,
    owner_id int check(owner_id in (select user_id from User_info.user_id),
    default_branch varchar(255),
    contributor_num int,
    watch_num int,
    star_num int,
    fork_num int,
);'''

# 需要在repository上建立索引
table_contributors = '''
create table Contributors(
    repository_id int,
    contributor_id int,
    foreign key fk_repository_id(repository_id) references Repository(repository_id),
    foreign key fk_contributor_id(contributor_id) references User_info(user_id)
);'''

# latest_commit是最近相关的提交，使用函数进行修改
# parent_branch需要进行检查
# file_structure_address是保存文件结构的文件地址，可通过下载整个代码后通过程序解析获得
table_branches = '''
create table Branches(
    branch_id int primary key auto_increment,
    branch_name varchar(255),
    parent_branch int check(parent_branch in (select branch_id from Branches)),
    owner_repository int,
    foreign key fk_owner_repository(owner_repository) references Repository(repository_id)
    on update cascade
    on delete cascade,
    latest_commit char(50),
    commit_num int,
    file_structure_address varchar(255)
);'''

# comment是提交时的说明
table_commits = '''
create table Commits(
    commit_id char(50) primary key,
    repository_id int,
    commit_user int,
    foreign key fk_repository_id(repository_id) references Repository(repository_id)
    on delete cascade
    on update cascade,
    commit_date date,
    comment varchar(255)
    '''