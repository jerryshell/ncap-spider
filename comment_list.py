import json

import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

url_template = 'https://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/{}/comments/newList'


def get_comment_list_by_news_id_limit_and_offset(news_id, limit, offset):
    params = (
        ('limit', limit),
        ('offset', offset),
    )

    url = url_template.format(news_id)
    print(url)

    response = requests.get(
        url,
        headers=headers,
        params=params,
        verify=False
    )

    json_response = json.loads(response.text)
    print(json_response)
    message = json_response.get('message', 'NO_ERROR')
    if message == '非法的分页参数':
        return []

    comment_list = json_response['comments']

    result = []
    for comment_id in comment_list:
        comment = comment_list[comment_id]
        result.append(comment)

    return result


def get_comment_list_by_news_id(news_id, init_limit=30, init_offset=0):
    limit = init_limit
    offset = init_offset

    result = []
    while True:
        comment_list = get_comment_list_by_news_id_limit_and_offset(news_id, limit, offset)
        if len(comment_list) <= 0:
            break
        result.extend(comment_list)
        offset += limit

    return result


if __name__ == '__main__':
    news_id = 'FAOL3S3L0001899O'
    result = get_comment_list_by_news_id(news_id)
    print(result)
    print(len(result))
