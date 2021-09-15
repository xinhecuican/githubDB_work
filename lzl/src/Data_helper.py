import datetime

import pandas as pd


def csv2list(file):
    corpus = pd.read_csv(file)
    return corpus.values.tolist()


def str2num(sum):
    data = 0
    if type(sum) != str:
        return str(sum)
    if sum[-1] == 'k':
        data = float(sum[:-1])
        data *= 1000
        data = int(data)
    return str(data)


def resolve_user_info(helper, file="../../lhx/res/user_info.csv"):
    lists = csv2list(file)
    ans = []
    for list in lists:
        temp = []
        temp.append(list[0])
        temp.append(list[1])
        temp.append(str2num(list[4]))
        ans.append(temp)
    helper.insert("User_info", ans)


def resolve_user_description(helper, file="../../lhx/res/user_info.csv"):
    lists = csv2list(file)
    ans = []
    for list in lists:
        temp = []
        temp.append(str(list[0]))
        temp.append("'" + list[1] + "'")
        temp.append("''")
        temp.append("''")
        temp.append("''")
        temp.append("''")
        temp.append("''")
        temp.append("''")
        temp.append("''")
        ans.append(temp)
    helper.insert("user_description", ans)


def resolve_repository(helper, file="../../lhx/res/repository.csv"):
    cor = pd.read_csv(file, )
    test = ''
    cor.columns = ['repository_name', 'repository_id', 'owner_name', 'default_branch',
                   'contributor_num', 'star_num', 'fork_num']
    id = cor['repository_id']
    owner_name = cor['owner_name']
    for i in range(len(owner_name)):
        datas = helper.run("select id from User_info where user_name = " + "'" + owner_name[i] + "'")
        if not datas:
            owner_name[i] = "NULL"
        else:
            owner_name[i] = str(datas[0][0])
    cor.drop(['repository_id', 'owner_name'], axis=1, inplace=True)
    cor.insert(0, 'owner_id', owner_name)
    cor.insert(0, 'repository_id', id)
    lists = cor.values.tolist()
    lists = [x for x in lists if x[1] != "NULL"]
    for l in lists:
        l.insert(-2, '0')
        l.insert(3,  str(datetime.datetime.now()))
        l.insert(4, str(True))
        l[-2] = str2num(l[-2])
        l[-1] = str2num(l[-1])
        l[-4] = str2num(l[-4])
        l[0] = str2num(l[0])
        l[2] = "'" + l[2] + "'"
        l[3] = "'" + l[3] + "'"
        l[5] = str(0)
    helper.insert("repository", lists)


def resolve_followers(helper, file):
    lists = csv2list(file)
    for list in lists:
        list[0] = str(list[0])
        list[1] = str(list[1])
    helper.insert("followers", lists)
