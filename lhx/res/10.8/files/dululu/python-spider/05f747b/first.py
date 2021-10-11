# BeautifulSoup实战
# 爬取三国演义所有的章节和标题https://www.shicimingju.com/book/sanguoyanyi.html
import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    headers = {
        'User - Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML,'
                        ' like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.text','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://m.shicimingju.com'+li.a['href']
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        #解析出详情页中的内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功')



