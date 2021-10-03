import datetime
import json
import math
import re

import numpy as np
import pandas as pd


def csv2list(file):
    corpus = pd.read_csv(file, header=None)
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


def dec_str(string):
    if type(string) == type(1.0) and math.isnan(string):
        return "''"
    else:
        string = string.replace("'", r"\'")
        return "'" + str(string) + "'"


def resolve_user_info(helper, file="../../lhx/res/user_info.csv"):
    lists = csv2list(file)
    ans = []
    for list in lists:
        temp = []
        temp.append(list[0])
        temp.append(list[1])
        temp.append(str2num(list[6]))
        temp.append(str2num(list[7]))
        temp.append(str2num(list[8]))
        temp.append(str2num(list[9]))
        ans.append(temp)
    helper.insert("User_info", ans)


def resolve_user_description(helper, file="../../lhx/res/user_description.csv"):
    lists = csv2list(file)
    ans = []
    for list in lists:
        temp = []
        temp.append(str(list[0]))
        temp.append(dec_str(list[1]))
        temp.append(dec_str(list[2]))
        temp.append(dec_str(list[3]))
        temp.append(dec_str(list[4]))
        temp.append(dec_str(list[5]))
        temp.append(dec_str(list[6]))
        temp.append(dec_str(list[7]))
        temp.append(dec_str(list[8]))
        ans.append(temp)
    helper.insert("user_description", ans)


def resolve_repository(helper, file="../../lhx/res/repository.csv"):
    lists = csv2list(file)
    for list in lists:
        list[0] = str(list[0])
        list[1] = str(list[1])
        list[2] = dec_str(list[2])
        list[3] = dec_str(list[3])
        list[4] = str(list[4])
        data = helper.run(f"select id from branches where repository_id = {list[0]} and branch_name = '{list[5]}'")
        if data:
            list[5] = str(data[0][0])
        else:
            list[5] = str(-1)
        list[6] = str(list[6])
        list[7] = str(list[7])
        list[8] = str(list[8])
        list[9] = str(list[9])
    helper.insert("repository", lists)


def resolve_repository_info(helper, file="../../lhx/res/repository_info.csv"):
    lists = csv2list(file)
    for list in lists:
        list[0] = str(list[0])
        list[1] = dec_str(list[1])
        list[2] = dec_str(list[2])
        list[3] = str(-1)
        list[4] = dec_str(list[4])
        list[5] = dec_str(list[5])
        list[6] = dec_str(list[6])
        list[7] = str(list[7])
    print(lists)
    helper.insert('repository_info', lists)


def resolve_tags(helper, file='../../lhx/res/tags.csv'):
    lists = csv2list(file)
    for list in lists:
        list[0] = str(list[0])
        list[1] = str(list[1])
        list[2] = dec_str(list[2])
        list[3] = '1'
        datas = helper.run('select id, commit_sha from commits')
        found = False
        for data in datas:
            if re.match(list[4], data[1]) is not None:
                found = True
                list[4] = data[0]
                break
        if not found:
            list[4] = -1
        list[4] = str(list[4])
        list[5] = str(list[5])
        list[6] = dec_str(list[6])
        list[7] = str(list[7])
        list[8] = dec_str(list[8])
    helper.insert('tags', lists)


def resolve_tag_files(helper, file='../../lhx/res/tag_files.csv'):
    lists = csv2list(file)
    for list in lists:
        list[0] = str(list[0])
        list[1] = dec_str(list[1])
        list[2] = str(list[2])
        list[3] = dec_str(list[3])
    helper.insert('tag_files', lists)


def resolve_followers(helper, file):
    lists = csv2list(file)
    for list in lists:
        list[0] = str(list[0])
        list[1] = str(list[1])
    helper.insert("followers", lists)


def resolve_licenses(helper, file="licenses.json"):
    data = {}
    with open(file, "r") as f:
        data = f.read()
    ans = []
    data = eval(data)
    for (key, value) in data.items():
        temp = []
        temp.append(key)
        with open(value['contents'], "r") as f:
            temp.append(f.read())
        temp.append(value['Permissions'])
        temp.append(value['Limitations'])
        temp.append(value['Conditions'])
        ans.append(temp)
    helper.insert("licenses", ans)


def resolve_branches(helper, file="../../lhx/res/branches.csv"):
    lists = csv2list(file)
    for list in lists:
        list[1] = str(list[1])
        datas = helper.run(f"select id, commit_sha from commits")
        found = False
        if datas:
            for data in datas:
                if re.match(list[2], data[1]) is not None:
                    found = True
                    list[2] = data[0]
                    break
        if not found:
            list[2] = -1
        list[2] = str(list[2])
        list[3] = str(list[3])
    helper.insert('branches', lists)


def dec_commit(l):
    ans = []
    ans.append(dec_str(l[0]))
    ans.append(str2num(l[1]))
    ans.append(str2num(l[2]))
    ans.append(str2num(l[3]))
    ans.append(str2num(l[4]))
    ans.append(dec_str(l[5]))
    ans.append(dec_str(l[6]))
    return ans


def resolve_commits(helper, file="../../lhx/res/commits.csv"):
    lists = csv2list(file)
    repository_id = lists[0][3]
    begin = 0
    for i in range(len(lists)):
        if repository_id != lists[i][2]:
            for k in range(i-1, begin-1, -1):
                data = helper.run(f"select id from commits where commit_sha = '{lists[k][0]}'")
                if data:
                    continue
                if type(lists[k][1]) == type(1.0) and math.isnan(lists[k][1]):
                    lists[k][1] = '-1'
                    helper.insert("commits", [dec_commit(lists[k])])
                else:
                    for j in range(k+1, i):
                        # print(re.match(lists[k][1], lists[j][0]), lists[k][1], lists[j][0])
                        if re.match(lists[k][1], lists[j][0]) is not None:
                            data = helper.run(f"select id from commits where commit_sha = '{lists[j][0]}'")
                            if data:
                                lists[k][1] = data[0][0]
                                helper.insert("commits", [dec_commit(lists[k])])
                            break
            begin = i
            repository_id = lists[i][2]
    for k in range(len(lists) - 1, begin - 1, -1):
        data = helper.run(f"select id from commits where commit_sha = '{lists[k][0]}'")
        if data:
            continue
        if type(lists[k][1]) == type(1.0) and math.isnan(lists[k][1]):
            lists[k][1] = -1
            helper.insert("commits", [dec_commit(lists[k])])
        else:
            for j in range(k + 1, len(lists)):
                if re.match(lists[k][1], lists[j][1]) is not None:
                    data = helper.run(f"select id from commits where commit_sha = '{lists[j][1]}'")
                    if data:
                        print(lists[k])
                        lists[k][1] = data[0][0]
                        helper.insert("commits", [dec_commit(lists[k])])
                    break


def resolve_commit_file_info(helper, file='../../lhx/res/commits.csv'):
    lists = csv2list(file)
    for list in lists:
