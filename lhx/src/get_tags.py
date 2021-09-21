from bs4 import BeautifulSoup
from common import getHTML, get_user_id, get_repo_id, save_sth

# 目前只爬第一页
def get_repo_tags(user_name, repo_name):
    user_id = get_user_id(user_name)
    repo_id = get_repo_id(user_name, repo_name)
    url = 'https://github.com/' + user_name + '/' + repo_name + '/tags'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    all_tags = soup.find_all('div', class_='commit js-details-container Details')
    for each in range(len(all_tags)):
        name = all_tags[each].find('a').text.replace(' ', '').replace(r'\n', '')
        tag_type = 1
        related_id = all_tags[each].find('a', class_='Link--muted').text.replace(r'\n', '').strip()
        # TODO: asset_num, react, is_pre_release, size
        publish_date = all_tags[each].find('relative-time').text
        is_pre_release = True

        single_tag = [repo_id, user_id, name.strip('\n'), tag_type, related_id, '0', publish_date, is_pre_release, '']
        save_sth(single_tag, 'tags', 0)
        print(single_tag)
        # ['\n1.12.3\n', 1, 'e87453e', 'Jul 22, 2019', True]

        tag_id = related_id
        file_name = repo_name + '-' + name # wily-1.19.0
        file_link = 'https://github.com/' + all_tags[each].find('a', attrs={'class': 'Link--muted', 'rel': 'nofollow'}).get('href')

        single_tag_file = [tag_id, file_name.replace('\n', ''), '99', file_link]
        save_sth(single_tag_file, 'tag_files', 0)
        print(single_tag_file)
        # ['e87453e', 'wily\n1.12.3\n', '/tonybaloney/wily/archive/refs/tags/1.12.3.zip']


# get_repo_tags('tonybaloney', 'wily')
