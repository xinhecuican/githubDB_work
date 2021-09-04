# 为了描述user_info的结构加上了password，但是实际上无法获得数据，直接使用default值即可
# description (Object):{
#    'email': 在首页提供的邮箱
#    'location': 首页提供的地址
#    'comments': 首页提供的评论
#     'link'： 首页提供的链接
# }
# followers和followings的格式相同 [{'id': 用户id, 'description': 用户简介}]
table_user_info = '''create table User_info(
    user_id int primary key,
    user_name varchar(100),
    password char(30) default '',
    email char(50) default '',
    follower_num int default 0,
    following_num int default 0,
    star_num int default 0,
    project_num int default 0,
    repository_num int default 0,
    package_num int default 0,
    description text,
    followers text,
    followings text
);'''

# repository_id可以在仓库主界面的html中搜repository，第一个显示的就是它的id
# visibility只能检索到true的
table_repository = '''
create table Repository(
    repository_id int primary key,
    owner_id int not NULL,
    name varchar(255), 
    visibility bool default true,
    default_branch varchar(255),
    contributor_num int,
    watch_num int,
    star_num int,
    fork_num int,
    foreign key fk_owner_id(owner_id) references User_info(user_id)
    on update cascade
    on delete cascade
);'''

# repository中的issue
# status： issue的状态，有open，closed等等
# comments: 是一个json文档，格式为
# {
#     id: comment的id
#     quota: 引用评论的id
#     user_id: 用户id
#     name: 用户名字
#     action: str,操作类型，new表示新建，comment表示评论，label表示增加label, close表示关闭
#     commit_date: 提交时间
#     text: 提交内容
# }
table_issue = '''
create table issue(
    issue_id int primary key auto_increment,
    owner_repository int,
    creator_id int,
    labels text,
    status int,
    create_date date,
    comments_sum int,
    question text,
    comments longtext
};'''

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
    on delete cascade
);'''

# comment是提交时的说明
# commit是commit的编号，长度为40位
# commit_directory_address是目录文件，它的格式为
# {"directory_name":{
#     "file_name": file_id
# }}
# longtext最多2^32 - 1个字节
# comments和issue表中的内容类似，但是没有action
table_commits = '''
create table Commits(
    commit_id char(50) primary key,
    parent_commit char(50),
    repository_id int,
    commit_date date,
    message varchar(255),
    comments longtext,
    contributors text,
    commit_directory_address MediumText,
    add_line int,
    delete_line int,
    foreign key fk_repository_id(repository_id) references Repository(repository_id)
    on delete cascade
    on update cascade
 );'''

# user_action: 0是commit 1是authored
table_commit_contributor = '''
create table Commit_contributor
(
    commit_id char(50),
    contributor_id int,
    user_action int  
);'''

# 用户的活动,在主页面显示
# type =0为创建仓库 =1为commit =2 pull request
table_activity = '''
create table Activity(
    activity_id int primary key auto_increment,
    type int,
    owner_repository_id int,
    activity_date date
);'''

# 文件内容使用二进制存储，最多4G
# file_type是文件后缀
# file_action是该commit对这个文件的动作，create=0，modified=1,remove=2,rename=3
# 只记录每个commit进行修改的文件必须要从最初的commit开始爬取，每次爬取时还要获得它的目录结构并重建为json格式
table_commit_files = '''
create table commit_files(
    file_id int not null primary key auto_increment,
    file_type char(20),
    file_action int,
    int add_lines,
    int remove_lines,
    file_name varchar(255) not null,
    file_content longblob
);'''