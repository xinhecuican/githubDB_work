import json
from bs4 import BeautifulSoup
from common import getHTML, get_user_id, get_repo_id, save_sth, trans_date_format


# NEW: 9.29 放在get_branch之后
def get_tags(user_name, repo_name, repo_id, default_branch, lastest_commit):
    user_id = get_user_id(user_name)
    url = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/releases'
    html = getHTML(url)
    js = json.loads(html)  # 每一项代表一个tag/release

    try:
        all_reacts = get_emoji(user_name, repo_name)
    except:
        all_reacts = []

    for i in range(min(len(js), 10)):  # 对于每一个release
        # 主要部分
        t_name = js[i]['tag_name']
        tag_id = js[i]['id']
        if js[i]['target_commitish'] == default_branch:
            type = 0
            related_id = lastest_commit
        else:
            type = 1
            related_id = lastest_commit
        asset_num = len(js[i]['assets'])  # 不包括source code包
        publish_date = trans_date_format(js[i]['published_at'], 1)
        is_pre_release = js[i]['prerelease']

        reacts = []
        for j in range(len(all_reacts)):  # 寻找和name对应的reactname
            if all_reacts[j][0] == t_name:
                reacts.append(all_reacts[j][1])

        single_tags = [repo_id, user_id, t_name, type, related_id, asset_num, publish_date, is_pre_release, reacts]
        save_sth(single_tags, 'tags', 0)
        print(single_tags)

        # 接下来处理asset文件 前提是有 如.exe
        if len(js[i]['assets']) > 0:
            for j in range(len(js[i]['assets'])):
                file_name = js[i]['assets'][j]['name']
                file_link = js[i]['assets'][j]['browser_download_url']
                file_size_url = js[i]['assets'][j]['url']
                file_size_html = getHTML(file_size_url)
                file_size_js = json.loads(file_size_html)
                file_size = file_size_js['size']

                single_tag_files = [tag_id, file_name, file_size, file_link]
                save_sth(single_tag_files, 'tag_files', 0)
                print(single_tag_files)


def get_emoji(user_name, repo_name):  # 返回['1.5.0', {'LiuHX01': 'thumbs up'}]形式的列表
    url = 'https://github.com/' + user_name + '/' + repo_name + '/releases'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    res_react = []

    all_releases = soup.find_all('div',
                                 class_='col-12 col-md-9 col-lg-10 px-md-3 py-md-4 release-main-section commit open '
                                        'float-left')
    for i in range(len(all_releases)):
        tag_name = all_releases[i].find('a').text
        try:
            tag_reacts = all_releases[i].find_all('button', attrs={'style': 'border-radius:100px;font-size:12px;'})
            for j in range(len(tag_reacts)):  # 一个release可能有多个react
                per_emoji = tag_reacts[j].get('aria-label')  # LiuHX01 reacted with thumbs up emoji
                temp_str = per_emoji.replace(' reacted with ', '&&&').replace(' emoji', '').partition('&&&')
                names_part = temp_str[0].replace(' ', '').replace('and', '')  # 多个人则是leynier,FelixTheC,LiuHX01的形式
                emoji_part = temp_str[2]
                tag_react = {names_part: emoji_part}
                res_react.append([tag_name, tag_react])
        except:
            tag_react = {}

    return res_react

# get_emoji('roman-right', 'beanie')
# get_tags('xinhecuican', 'easy-capture', '341677148', 'main', '8108af9')
