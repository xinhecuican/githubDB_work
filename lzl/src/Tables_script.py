# 为了描述user_info的结构加上了password，但是实际上无法获得数据，直接使用default值即可
# status: 状态，可以在主页的用户头像旁设置
table_user_info = '''create table User_info(
    id int primary key,
    user_name varchar(100),
    password char(30) default '',
    email char(50) default '',
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
create table user_description(
    id int primary key,
    user_name varchar(100),
    nick_name varchar(100) default '',
    status varchar(50) default '',
    company varchar(255) default '',
    location varchar(255) default '',
    comments text,
    link varchar(255) default '',
    avatar_url varchar(255) default ''
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
    type tinyint,
    user_id int,
    commit_id int,
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


# 不需要爬数据，只是应该有这个表
table_user_notification = '''
create table user_notification(
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
default_branch: 默认的分支，爬取时爬取分支名
create_date: 创建时间，如果无法获得可以使用第一个commit的时间
"""
table_repository = '''
create table Repository(
    id int primary key,
    user_id int not NULL,
    name varchar(255) default '', 
    create_date datetime,
    visibility bool default true,
    default_branch int,
    contributor_num int default 0,
    watch_num int default 0,
    star_num int default 0,
    fork_num int default 0
);'''


"""
code_type (Array): [{
                        'name' (str): 类型名 如c++, python等
                        'percentage' (float)
                    }]
contributors (Array): [{
                            id:
                            name:
                      }]
tag (Array): 在描述下面呈现 例如 c-plus-plus c
release_num: 由程序解决
"""
table_repository_info = '''
create table repository_info(
    id int primary key,
    description varchar(255) default '',
    website varchar(255) default '',
    licenses_id int,
    tag text,
    code_type text,
    contributors text,
    release_num int default 0
);'''


table_licenses = '''
create table licenses(
    id int primary key auto_increment,
    name varchar(100),
    license_content longtext,
    permissions text,
    limitations text,
    conditions text
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
    type tinyint,
    related_id int,
    asset_num smallint default 0,
    publish_date date,
    is_pre_release boolean,
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
    question text
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
    commit_date datetime,
    content text
);'''


table_labels = '''
create table labels(
    id int primary key auto_increment,
    repository_id int,
    url varchar(255) default '',
    name varchar(50) default '',
    color varchar(10) default ''
);'''


# question_id: 对应pull_request_action的id，是pull_request的第一个comment
table_pull_request = '''
create table pull_request(
    id int primary key auto_increment,
    repository_id int,
    question_id int,
    base_branch_id int,
    from_branch_id int,
    related_commit_id text,
    is_open boolean,
    merge_status boolean,
    check_status boolean
);'''


# id就是pull_request的id
# labels (Array): 记录label表中的id
# projects： 只是一个占位符，因为没考虑projects表
# milestone: 只是一个占位符
table_pull_request_info = '''
create table pull_request_info(
    id int primary key,
    Assignee_id int,
    labels text,
    projects text,
    milestone text,
    link_pull_request_id int default -1
);'''


# 'action': 0-添加评论 1-增加commit 2-review
table_pull_request_action = '''
create table pull_request_action(
    id int primary key auto_increment,
    pull_request_id int,
    user_id int,
    comment text,
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
    id int primary key auto_increment,
    branch_name varchar(255),
    repository_id int,
    latest_commit int,
    commit_num int default 0
);'''


# comment是提交时的说明
# commit是commit的编号，长度为40位
# longtext最多2^32 - 1个字节
# 如果只有一个人则author就是commit_user
# 不考虑merge的两个parent
table_commits = '''
create table Commits(
    id int primary key auto_increment,
    commit_sha char(41),
    parent_commit int,
    repository_id int,
    author_user_id int default -1,
    commit_user_id int default -1,
    commit_date datetime,
    message varchar(255)
 );'''


# commit_directory_address是目录文件，它的格式为
# {
#     'file_name': {
#                     'dic_commit_id': commit_id
#                     'file_name': file_id
#                 }
#     'file_name': file_id
# }
table_commit_file_info = '''
create table commit_file_info(
    id int primary key,
    commit_directory_address varchar(255),
    add_line int default 0,
    delete_line int default 0,
    change_file_num int default 0
);'''


# 文件内容使用二进制存储，最多4G
# file_type是文件后缀
# file_action是该commit对这个文件的动作，create=0，modified=1,remove=2,rename=3
"""
更新： 只需要爬取每次commit更改的文件，然后每个commit构建一个目录，目录格式为
{
    'file_name': {
                    'dic_commit_id': commit_id
                    'file_name': file_id
                }
    'file_name': file_id
}
commit_comment: 冗余项，减少查询commit表
数据库中只存文件路径，具体的文件由路径搜索然后从网上载入
"""
table_commit_files = '''
create table commit_files(
    id int not null primary key auto_increment,
    commit_id int,
    file_name varchar(255),
    commit_comment varchar(255) default '',
    file_type char(20) default '',
    file_action int,
    file_line int default 0,
    add_lines int default 0,
    remove_lines int default 0,
    file_path text not null
);'''


# 对这个commit的评论
table_commit_comment = '''
create table commit_comment(
    id int primary key auto_increment,
    commit_id int,
    quota_id int default 0,
    comment_date datetime,
    comment_content text
);'''