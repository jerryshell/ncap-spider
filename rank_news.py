import requests
from bs4 import BeautifulSoup

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}


def get_rank_news():
    response = requests.get(
        'http://news.163.com/special/0001386F/rank_whole.html',
        headers=headers,
        verify=False
    )

    soup = BeautifulSoup(response.text, features='html.parser')
    a_element_list = soup.select('.active a')

    result = []
    for a_element_item in a_element_list:
        title = a_element_item.text
        href = a_element_item['href']
        html_id = href.split('/')[-1].replace('.html', '')

        result_item = {
            'id': html_id,
            'title': title,
            'href': href
        }
        result.append(result_item)

    return result


if __name__ == '__main__':
    result = get_rank_news()
    print(result)
