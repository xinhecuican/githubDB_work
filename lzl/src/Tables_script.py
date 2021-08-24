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

# repository_id可以在仓库主界面的html中搜repository，第一个显示的就是它的id
table_repository = '''
create table Repository(
    repository_id int primary key,
    owner_id int not NULL,
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

# latest_commit是最近相关的提交，使用函数进行修改,就不建立外键
# parent_branch需要进行检查
table_branches = '''
create table Branches(
    branch_id int primary key auto_increment,
    branch_name varchar(255),
    parent_branch int,
    owner_repository int,
    latest_commit char(50),
    commit_num int,
    foreign key fk_owner_repository(owner_repository) references Repository(repository_id)
    on update cascade
    on delete cascade,
    foreign key fk_create_user(create_user) references User_info(user_id)
    on update cascade
    on delete set null
);'''

# comment是提交时的说明
# commit是commit的编号，长度为40位
# commit_directory_address是目录文件地址
table_commits = '''
create table Commits(
    commit_id char(50) primary key,
    repository_id int,
    author int,
    commit_date date,
    message varchar(255),
    commit_directory_address varchar(255),
    add_line int,
    delete_line int,
    commit_branch int,
    
    foreign key fk_repository_id(repository_id) references Repository(repository_id)
    on delete cascade
    on update cascade,
    foreign key fk_commit_user(commit_user) references User_info(user_id)
    on delete set null
    on update cascade, 
    foreign key fk_commit_branch(commit_branch) references Branches(commit_branch)
    on delete set null
    on update cascade
 );'''

# 这只是一个演示，它应该是Branches表table_structure_address对应文件的一项的大致内容
# 如果使用数据库负载太大，并且没有必要
# type=0为目录, type=1为文件，文件的address才有实际意义
# related_commit是这个文件最后被修改的commit键
test_table_files = '''
create table Files(
    file_id int primary key auto_increment,
    owner_branch_id int foreign key references Branches(branch_id)
    on delete cascade
    on update cascade,
    parent_id int,
    type int,
    related_commit varchar(50),
    name varchar(255),
    address varchar(255)
);'''