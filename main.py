import json
from multiprocessing import Process

import requests
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from comment_list import get_comment_list_by_news_id
from news_title import get_title_by_url

# 实例化 FastAPI
app = FastAPI()


class CreateTaskForm(BaseModel):
    news_id: str
    news_url: str
    notify_url: str


@app.post('/createTask')
def main(form: CreateTaskForm):
    print(form)
    # 新进程
    p = Process(target=run_task, args=(form.news_id, form.news_url, form.notify_url))
    p.start()
    return {
        'ok': True
    }


@app.get('/info')
def info():
    return {
        'ok': True
    }


def run_task(news_id, news_url, notify_url):
    comment_list = []
    try:
        title = get_title_by_url(news_url)
        comment_list = get_comment_list_by_news_id(news_id)
        print('len(comment_list) %s' % len(comment_list))
    except Exception as e:
        print(e)
        send_notify(notify_url, {
            'ok': False,
            'title': '无法采集',
            'commentList': comment_list
        })
        return
    send_notify(notify_url, {
        'ok': True,
        'title': title,
        'commentList': comment_list
    })


def send_notify(notify_url: str, data: dict):
    response = requests.post(
        notify_url,
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/json',
        },
        data=json.dumps(data)
    )
    print(response.text)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7070)
