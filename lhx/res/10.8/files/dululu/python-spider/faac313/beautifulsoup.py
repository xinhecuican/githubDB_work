from bs4 import BeautifulSoup
if __name__ == "__main__":
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    print(soup)
