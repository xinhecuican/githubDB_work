table_user_info = '''create table User_info(
    user_id int primary key,
    user_name varchar(100),
    follower_num int default 0,
    following_num int default 0,
    star_num int default 0,
    project_num int default 0,
    repository_num int default 0,
    package_num int default 0
);'''

# 多对多关系，无法建立主键，可以建立索引
table_followers = '''create table Followers(
    follower_id int,
    following_id int,
    foreign key fk_follower(follower_id) references User_info(user_id)
    on delete set null
    on update cascade,
    foreign key fk_following(following_id) references User_info(user_id)
    on delete set null
    on update cascade
);'''

table_repository = '''
create table Repository(
    repository_id int primary key auto_increment,
    owner_id int,
    name varchar(255), 
    default_branch varchar(255),
    contributor_num int,
    watch_num int,
    star_num int,
    fork_num int,
    foreign key fk_owner_id(owner_id) references User_info(user_id)
    on update cascade
    on delete cascade
);'''

# 需要在repository上建立索引
table_contributors = '''
create table Contributors(
    repository_id int,
    contributor_id int,
    foreign key fk_repository_id(repository_id) references Repository(repository_id)
    on update cascade
    on delete cascade,
    foreign key fk_contributor_id(contributor_id) references User_info(user_id)
    on update cascade
    on delete set null
);'''

# latest_commit是最近相关的提交，使用函数进行修改
# parent_branch需要进行检查
# file_structure_address是保存文件结构的文件地址，可通过下载整个代码后通过程序解析获得
table_branches = '''
create table Branches(
    branch_id int primary key auto_increment,
    branch_name varchar(255),
    parent_branch int ,
    owner_repository int,
    create_user int,
    latest_commit char(50),
    commit_num int,
    file_structure_address varchar(255),
    foreign key fk_owner_repository(owner_repository) references Repository(repository_id)
    on update cascade
    on delete cascade,
    foreign key fk_create_user(create_user) references User_info(user_id)
    on update cascade
    on delete set null
);'''

# comment是提交时的说明
# commit是commit的编号，长度为40位
# commit_data_address是可选项，为commit的内容文件，当前不确定是否可以搜集
table_commits = '''
create table Commits(
    commit_id char(50) primary key,
    repository_id int,
    commit_user int,commit_date date,
    comment varchar(255),
    commit_data_address varchar(255),
    foreign key fk_repository_id(repository_id) references Repository(repository_id)
    on delete cascade
    on update cascade,
    foreign key fk_commit_user(commit_user) references User_info(user_id)
    on delete set null
    on update cascade 
 );'''