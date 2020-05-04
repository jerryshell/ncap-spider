import requests
from bs4 import BeautifulSoup

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.163.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}


def get_title_by_url(url: str):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, features='html.parser')
    title = soup.select('head > title')[0]
    return title.text


if __name__ == '__main__':
    title = get_title_by_url('https://ent.163.com/20/0423/19/FAU2B0QA00038FO9.html')
    print(title)
    title = get_title_by_url('https://news.163.com/20/0423/20/FAU5M35C000189FH.html')
    print(title)
    title = get_title_by_url('https://war.163.com/20/0423/15/FATIHP4E000181KT.html')
    print(title)
