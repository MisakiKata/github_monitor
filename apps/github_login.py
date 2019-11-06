import requests
from lxml import etree
from bs4 import BeautifulSoup


class github_login(object):

    def __init__(self, word, num):
        self.session = requests.Session()
        self.cookie = ''
        self.word = word
        self.num = num


    def get_cookie(self, username, passwd):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'text/html',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer': 'https://github.com/login',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        self.session.post('https://github.com/session', headers = headers, data=self.get_token(username, passwd))
        r = self.session.get('https://github.com/search?q='+self.word+'&type=Code', headers=headers)
        if r.status_code == 200:
            self.cookie = self.session.cookies
            return self.search()
        elif r.status_code == 401:
            self.get_cookie(username, passwd)

    def search(self):

        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept':'text/html',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer':'https://github.com/search?q=google.com&type=Code',
            'X-PJAX':'true',
            'X-PJAX-Container':'#js-pjax-container',
            'X-Requested-With':'XMLHttpRequest',
        }
        list_name, list_addr, list_time = [], [], []
        for i in range(1, self.num + 1):
            r = self.session.get(
                'https://github.com/search?o=desc&p=' + str(i) + '&q=' + self.word + '&s=indexed&type=Code',
                headers=headers)
            print(r.status_code)
            html = etree.HTML(r.text)
            name = html.xpath("//div/a[@class='link-gray']/@href")  #author
            list_name.append(name)
            addr = html.xpath("//div[@class='f4 text-normal']/a/@href")   #url
            list_addr.append(addr)
            time = html.xpath("//span[@class='updated-at mr-3']/relative-time/text()")   #更新时间
            list_time.append(time)

        return [list_name, list_addr, list_time]


    def get_token(self, username, passwd):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept':'text/html',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer':'https://github.com',
        }
        post_data = {}
        r = self.session.get('https://github.com/login', headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        input = soup.find_all('input')
        for item in input:
            post_data[item.get('name')] = item.get('value')
        post_data['login'], post_data['password'] = username, passwd
        return post_data
