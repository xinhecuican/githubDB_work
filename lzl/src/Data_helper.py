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

def resolve_user_info(helper, file):
    lists = csv2list(file)
    for list in lists:
        list[1] = "'" + list[1] + "'"
        for i in range(2, len(list)):
            list[i] = str2num(list[i])
        list[0] = str(list[0])
        list.append('0')
    helper.insert("User_info", lists)

def resolve_repository(helper, file):
    cor = pd.read_csv(file, )
    test = ''
    cor.columns = ['repository_name', 'repository_id', 'owner_name', 'default_branch',
                   'contributor_num', 'star_num', 'fork_num']
    id = cor['repository_id']
    owner_name = cor['owner_name']
    for i in range(len(owner_name)):
        datas = helper.run("select user_id from User_info where user_name = " + "'" + owner_name[i] + "'")
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
        l[-2] = str2num(l[-2])
        l[-1] = str2num(l[-1])
        l[-4] = str2num(l[-4])
        l[0] = str2num(l[0])
        l[2] = "'" + l[2] + "'"
        l[3] = "'" + l[3] + "'"
    helper.insert("repository", lists)

def resolve_followers(helper, file):
    lists = csv2list(file)
    for list in lists:
        list[0] = str(list[0])
        list[1] = str(list[1])
    helper.insert("followers", lists)


