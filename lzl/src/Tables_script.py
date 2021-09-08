# 为了描述user_info的结构加上了password，但是实际上无法获得数据，直接使用default值即可
# status: 状态，可以在主页的用户头像旁设置
table_user_info = '''create table User_info(
    id int primary key,
    user_name varchar(100),
    password char(30) default '',
    email char(50) default '',
    status varchar(50) default '',
    follower_num int default 0,
    following_num int default 0,
    star_num int default 0,
    project_num int default 0,
    repository_num int default 0,
    package_num int default 0
);'''


table_followers = '''
create table followers(
    id int primary key auto_increment,
    follower_id int,
    following_id int
);'''


# user_name是冗余字段，但是一般查用户信息都要用户名
table_user_description = '''
create user_description(
    id int primary key,
    user_name varchar(100),
    nick_name varchar(100) default '',
    company varchar(255) default '',
    location varchar(255) default '',
    comments text default '',
    link varchar(255) default ''
);'''


# 不需要爬数据，只是应该有这个表
table_user_notification = '''
create user_notification(
    id int primary key auto_increment,
    user_id int,
    type int,
    status int,
    contents mediumtext
);'''


"""
repository_id可以在仓库主界面的html中搜repository，第一个显示的就是它的id
visibility只能检索到true的
contributors (Array): 所有contributor的id
"""
table_repository = '''
create table Repository(
    id int primary key,
    user_id int not NULL,
    name varchar(255) default '', 
    visibility bool default true,
    default_branch varchar(255) default 'main',
    latest_commit_id varchar(50),
    contributor_num int default 0,
    watch_num int default 0,
    star_num int default 0,
    fork_num int default 0,
    foreign key fk_owner_id(user_id) references User_info(id)
    on update cascade
    on delete cascade
);'''


"""
code_type (Array): [{
                        'name' (str): 类型名 如c++, python等
                        'percentage' (float)
                    }]
tag: 在描述下面呈现 例如 c-plus-plus c等
"""
table_repository_info = '''
create table repository_info(
    id int primary key,
    description varchar(255) default '',
    website varchar(255) default '',
    licenses_id int,
    tag text,
    code_type text,
    contributors text
);'''


table_licenses = '''
create table licenses(
    id int primary key auto_increment,
    name str(100),
    license_content longtext  
);'''


"""
react (Array): [{
                    'name' (str): 用户名
                    'emoji_type' (int): 表情类型
                }]
# type = 0 related_id=branch_id. type = 1 related_id = commit_id
"""
table_tags = '''
create table tags(
    id int primary key auto_increment,
    repository_id int,
    user_id int,
    name varchar(255),
    type smallint,
    related_id int,
    name varchar(255),
    publish_date date,
    is_pre_release boolean,
    assets mediumtext,
    react mediumtext
);'''


table_tag_files = '''
create table tag_files(
    id int primary key auto_increment,
    tag_id int,
    name varchar(255),
    size int,
    file_link varchar(255)
);'''


# repository中的issue
# status： issue的状态，有open，closed等等
table_issue = '''
create table issue(
    id int primary key auto_increment,
    repository_id int,
    creator_id int,
    labels text,
    status int,
    create_date date,
    comments_sum int,
    question text,
    comments longtext
);'''


# quota_id: 引用评论id
# action: ,操作类型，0表示新建，1表示评论，2表示增加label, 3表示关闭
table_issue_comment = '''
create table issue_comment(
    id int primary key auto_increment,
    issue_id int,
    quota_id int default 0,
    user_id int,
    name varchar(100),
    action tinyint,
    commit_date date,
    content text default ''
);'''


table_pull_request = '''
create table pull_request(
    id int primary key auto_increment,
    repository_id int,
    base_branch_id int,
    from_branch_id int,
    related_commit_id text,
    is_open boolean,
    merge_status boolean,
    check_status boolean
);'''


# 'action': 0-添加评论 1-增加commit 2-review
table_pull_request_action = '''
create table pull_request_action(
    id int primary key auto_increment,
    pull_request_id int,
    user_id int,
    comment text default '',
    action tinyint
);'''


# 需要在repository上建立索引
# table_contributors = '''
# create table Contributors(
#     repository_id int,
#     contributor_id int,
#     foreign key fk_repository_id(repository_id) references Repository(id)
#     on update cascade
#     on delete cascade,
#     foreign key fk_contributor_id(contributor_id) references User_info(id)
#     on update cascade
#     on delete set null
# );'''

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
    foreign key fk_owner_repository(owner_repository) references Repository(id)
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
    id int primary key auto_increment,
    commit_id char(50),
    parent_commit char(50),
    repository_id int,
    commit_date date,
    message varchar(255),
    comments mediumtext,
    contributors text,
    commit_directory_address MediumText,
    add_line int,
    delete_line int,
    foreign key fk_repository_id(repository_id) references Repository(id)
    on delete cascade
    on update cascade
 );'''


# user_action: 0是commit 1是authored
# table_commit_contributor = '''
# create table Commit_contributor
# (
#     commit_id char(50),
#     contributor_id int,
#     user_action int
# );'''
# 用户的活动,在主页面显示
# type =0为创建仓库 =1为commit =2 pull request =3 following
table_activity = '''
create table Activity(
    id int primary key auto_increment,
    type int,
    user_id int,
    owner_repository_id int,
    activity_date date
);'''


"""
每天一次统计activity的记录
related_activities_id (Array): 相关活动id
"""
table_activity_record = '''
create table activity_record(
    id int primary key auto_increment,
    user_id int,
    clear_date date,
    contribution_num int,
    related_activities_id text
);'''


# 文件内容使用二进制存储，最多4G
# file_type是文件后缀
# file_action是该commit对这个文件的动作，create=0，modified=1,remove=2,rename=3
"""
更新： 只需要爬取每次commit更改的文件，然后每个commit构建一个目录，目录格式为
{
    'file_name': {
                    'file_name': commit_id
                }
    'file_name': commit_id
}
数据库中只存文件路径，具体的文件由路径搜索然后从网上载入
"""
table_commit_files = '''
create table commit_files(
    file_id int not null primary key auto_increment,
    commit_id int,
    file_type char(20) default '',
    file_action int,
    file_line int default 0,
    add_lines int default 0,
    remove_lines int default 0,
    file_path text not null,
);'''